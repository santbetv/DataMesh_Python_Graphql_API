import graphene
import json
from ..databricksdb.connectiondbHR import DatabaseConnection
from logging import getLogger
logger = getLogger(__name__)

#Se crea el objeto con los campos que se quieren retornar en la funcion
class HistoriaRadiacionPub(graphene.ObjectType):
    idEstacion = graphene.ID(required=True)
    fechaMedida = graphene.DateTime(required=True)
    calidadValor = graphene.Int()
    valorRadiacion = graphene.Float()

class GenericData(graphene.ObjectType):
    status =graphene.String(required=True)
    message=graphene.String(required=True)
    results=graphene.List(HistoriaRadiacionPub)

#Clase donde se hace el llamado a la conexion de la base de datos
class Query(graphene.ObjectType):
    readItems = graphene.List(GenericData, idEstacion=graphene.ID(default_value=None), fechaInicio=graphene.DateTime(default_value=None), fechaFin=graphene.DateTime(default_value=None))

    def resolve_readItems(self, info, idEstacion, fechaInicio, fechaFin):
        return DatabaseConnection().read_items(idEstacion, fechaInicio, fechaFin)

#Clase basica de GraphQL
class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query
        )
        pass

    def query(self, query):
        results = self.schema.execute(query)
        return json.dumps(results.data)

    def queryWithContext(self, query, context):
        results = self.schema.execute(query, context=context)
        return results
import graphene
import json
from ..databricksdb.connectiondbHF import DatabaseConnection
from logging import getLogger
logger = getLogger(__name__)

#Se crea el objeto con los campos que se quieren retornar en la funcion
class HistoriaFronterasPub(graphene.ObjectType):
    idFrontera = graphene.ID(required=True)

class GenericData(graphene.ObjectType):
    status =graphene.String(required=True)
    message=graphene.String(required=True)
    results=graphene.List(HistoriaFronterasPub)

#Clase donde se hace el llamado a la conexion de la base de datos
class Query(graphene.ObjectType):
    readItems = graphene.List(GenericData, fechaInicio=graphene.DateTime(default_value=None), fechaFin=graphene.DateTime(default_value=None), minHistoria=graphene.Int(default_value=672))

    def resolve_readItems(self, info, fechaInicio, fechaFin, minHistoria):
        return DatabaseConnection().read_items(fechaInicio, fechaFin, minHistoria)

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
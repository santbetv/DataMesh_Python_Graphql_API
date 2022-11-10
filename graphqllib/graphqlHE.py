import graphene
import json
from ..databricksdb.connectiondbHE import DatabaseConnection
from logging import getLogger
logger = getLogger(__name__)

#Se crea el objeto con los campos que se quieren retornar en la funcion
class HistoriaEnergiaPub(graphene.ObjectType):
    idFrontera = graphene.ID(required=True)
    fechaMedida = graphene.DateTime(required=True)
    constanteEnergia = graphene.Int(required=True)
    energiaActiva = graphene.Float()
    capacidadInstalada = graphene.Float()
    latitud = graphene.String()
    longitud = graphene.String()

class GenericData(graphene.ObjectType):
    status =graphene.String(required=True)
    message=graphene.String(required=True)
    results=graphene.List(HistoriaEnergiaPub)

#Clase donde se hace el llamado a la conexion de la base de datos
class Query(graphene.ObjectType):
    readItems = graphene.List(GenericData, esGeneracion=graphene.Boolean(default_value=None), idFrontera=graphene.ID(default_value=None), fechaInicio=graphene.DateTime(default_value=None), fechaFin=graphene.DateTime(default_value=None))

    def resolve_readItems(self, info, esGeneracion, idFrontera, fechaInicio, fechaFin):
        res = DatabaseConnection().read_items(esGeneracion, idFrontera, fechaInicio, fechaFin)
        return res

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
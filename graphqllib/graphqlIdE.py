import graphene
import json
from ..databricksdb.connectiondbIdE import DatabaseConnection
from logging import getLogger
logger = getLogger(__name__)

#Se crea el objeto con los campos que se quieren retornar en la funcion
class IdEstacionPub(graphene.ObjectType):
    EstacionRadiacion = graphene.String()

class GenericData(graphene.ObjectType):
    status =graphene.String(required=True)
    message=graphene.String(required=True)
    results=graphene.List(IdEstacionPub)

#Clase donde se hace el llamado a la conexion de la base de datos
class Query(graphene.ObjectType):
    readItems = graphene.List(GenericData, idFrontera=graphene.ID(default_value=None))

    def resolve_readItems(self, info, idFrontera):
        return DatabaseConnection().read_items(idFrontera)

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
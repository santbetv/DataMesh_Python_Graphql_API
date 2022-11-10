import os
from graphql import GraphQLError
from databricks import sql
from .config import config
from ..exception import exceptions
from logging import getLogger
logger = getLogger(__name__)

#Clase donde se realiza la conexion a la base de datos y se obtiene la informacion del query 
class DatabaseConnection():

    def __init__(self):
        # Se inicializa Databricks
        self.client = sql.connect(server_hostname=config['SERVER_HOSTNAME'],
                http_path=config['HTTP_PATH'],
                access_token=os.getenv("AccessTokenDatabricks"))

        self.cursor = self.client.cursor()

    #Se construye el query usando los parametros y se ejecuta
    def read_items(self, idFrontera): 
        q = f"SELECT \
                EstacionRadiacion \
            FROM autogeneradores_db.frontera \
            WHERE Id = '{idFrontera}'"

        query = {'query': q}

        try:
            self.cursor.execute(query['query'])
            itemList =  list(self.cursor.fetchall())
            dato = exceptions.validator(self.client._transport.code, self.client._transport.message, itemList)
            self.cursor.close()
            self.client.close()
            return dato
        except Exception as e:
            self.cursor.close()
            self.client.close()
            logger.error('Error ---->' + e)
            raise GraphQLError(e.args)
    
    def close_conne(self):
        self.cursor.close()
        self.client.close()
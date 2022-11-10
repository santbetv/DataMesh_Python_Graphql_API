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
    def read_items(self, fechaInicio, fechaFin, minHistoria): 
        q = 'SELECT \
                COUNT(1) AS medidas, \
                idFrontera, \
                generacion \
            FROM autogeneradores_db.medida'

        if(fechaInicio is None and fechaFin is None):
            q = q 
        elif(fechaInicio is None and fechaFin is not None):
            q = q + f" WHERE fechaMedida <= '{fechaFin}'"
        elif(fechaInicio is not None and fechaFin is None):
            q = q + f" WHERE fechaMedida >= '{fechaInicio}'"
        elif(fechaInicio is not None and fechaFin is not None):
            q = q + f" WHERE fechaMedida >= '{fechaInicio}' AND fechaMedida <= '{fechaFin}'"
        
        q = q + ' GROUP BY idFrontera, generacion'

        if(minHistoria is not None):
            q = "SELECT DISTINCT idFrontera \
                 FROM ( " + q + f" ) \
                 WHERE medidas > {minHistoria}"

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
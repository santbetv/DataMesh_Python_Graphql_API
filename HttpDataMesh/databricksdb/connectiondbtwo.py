from functools import cache
import os
from typing_extensions import Self
from graphql import GraphQLError
from databricks import sql
from .config import config
from ..exception import exceptions
from datetime import date, datetime, time
from graphene.types.datetime import Date, DateTime, Time
from logging import getLogger
logger = getLogger(__name__)

class DatabaseConnection():

    def __init__(self):
        ## Initialize the databricks

        self.client = sql.connect(server_hostname=config['SERVER_HOSTNAME'],
                http_path=config['HTTP_PATH'],
                access_token=os.getenv("AccessTokenDatabricks"))

        self.cursor = self.client.cursor()

        

    def read_codInstalacion(self, codInstalacion):
        query = {'query': 'SELECT NOMENCLATURA as nomenclatura, COD_INSTALACION as codInstalacion, COORDENADAX as longitud, COORDENADAY as latitud, NOMENCLATURA_SUI as nomenclaturaSui FROM marcopolo_db.marco_polo WHERE COD_INSTALACION=' +"'{0}'".format(codInstalacion) }
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

    def read_info(self, longitud, latitud):

        q = 'SELECT ppal.COD_UNICO_DIRECCION as codigoUnicoDireccion, \
                    ppal.NOMENCLATURA as nomenclatura, \
                    ppal.COD_INSTALACION as codInstalacion, \
                    ppal.Longitud as longitud, \
                    ppal.Latitud as latitud, \
                    ppal.NOMENCLATURA_SUI as nomenclaturaSui, \
                    ppal.TIPO_DIRECCION as tipoDireccion, \
                    ppal.REFERENCIA_DIRECCION as referenciaDireccion, \
                    ppal.COD_CATASTRO as codigoCatastro, \
                    ppal.MATRICULA_INMOBILIARIA as matriculaInmobiliaria, \
                    ppal.ESTRATO as estrato, \
                    ppal.ESTADO_ as estado, \
                    ppal.ESTADO_PROV_ESTRATO as estadoProvEstrato, \
                    ppal.ESTADO_PROV_COORDENADAS as estadoProvCoordenadas, \
                    ppal.ESTADO_PROV_NOMENCLATURA as estadoProvNomenclatura, \
                    ppal.ESTADO_PROV_CICLO_LECTURA as estadoProvCicloLectura, \
                    ppal.ESTADO_PROV_CICLO_REPARTO as estadoProvCicloReparto, \
                    ppal.ESTADO_PROV_CORRERIA_LECTURA as estadoProvCorreriaLectura, \
                    ppal.ESTADO_PROV_CORRERIA_REPARTO as estadoProvCorreriaReparto, \
                    ppal.CICLO_LECTURA as cicloLectura, \
                    ppal.CICLO_REPARTO as cicloReparto, \
                    ppal.TIPO_CORRERIA as tipoCorreria, \
                    ppal.CORRERIA_LECTURA as correriaLectura, \
                    ppal.CORRERIA_REPARTO as correriaReparto, \
                    ppal.INI_RUTA_LECTURA as iniRutaLectura, \
                    ppal.RUTA_LECTURA as rutaLectura, \
                    ppal.RUTA_REPARTO as rutaReparto, \
                    ppal.PAIS as pais, \
                    ppal.DIV_TERRITORIAL1 as divTerritorial1, \
                    ppal.DIV_TERRITORIAL2 as divTerritorial2, \
                    ppal.DIV_TERRITORIAL3 as divTerritorial3, \
                    ppal.DIV_TERRITORIAL4 as divTerritorial4, \
                    ppal.DIV_TERRITORIAL5 as divTerritorial5, \
                    ppal.DIV_TERRITORIAL6 as divTerritorial6, \
                    ppal.ZONA_POSTAL as zonaPostal, \
                    ppal.ESTADO_GEOCODIFICACION as estadoGeocodificacion, \
                    ppal.DESCRIPCION as descripcion, \
                    ppal.ESTADO as estado, \
                    ppal.ZONA_OPERATIVA as zonaOperativa, \
                    ppal.LOCALIDAD_OPERATIVA as localidadOperatica, \
                    ppal.ACOPIO as acopio, \
                    ppal.COD_DIRECCION_ACOPIO as codDireccionAcopio, \
                    ppal.COD_ESTANDARIZACION as codEstandarizacion, \
                    ppal.ESTADO_HOMOLOGACION as estadoHomologacion, \
                    ppal.TIPO_CRUCE as tipoCruce, \
                    ppal.COORDENADAZ as coordenadaZ, \
                    ppal.CEDULA_CATASTRAL as cedulaCatastral, \
                    ppal.SECTOR_OPERATIVO as sectorOperativo \
                    FROM marcopolo_db.marcopolo_view ppal '
                    
        query = {'query': q+'WHERE ppal.Longitud={0} and ppal.Latitud={1} LIMIT 10'.format(longitud, latitud) }
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
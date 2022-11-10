import graphene
import json
from ..databricksdb import connectiondb
from ..databricksdb.connectiondbtwo import DatabaseConnection
from logging import getLogger
logger = getLogger(__name__)

# type MarcoPoloDireccionPub
class MarcoPoloDireccionPub(graphene.ObjectType):
    codigoUnicoDireccion = graphene.String(required=True)
    nomenclatura = graphene.String(required=True)
    codInstalacion = graphene.ID(required=True)
    longitud = graphene.Decimal(required=True)
    latitud = graphene.Decimal(required=True)
    nomenclaturaSui = graphene.String(required=True)
    tipoDireccion = graphene.String(required=True)
    referenciaDireccion = graphene.String(required=True)
    tipoDireccion = graphene.String(required=True)
    referenciaDireccion = graphene.String(required=True)
    codigoCatastro = graphene.String(required=True)
    matriculaInmobiliaria = graphene.String(required=True)
    estrato = graphene.String(required=True)
    estado = graphene.String(required=True)
    estadoProvEstrato = graphene.String(required=True)
    estadoProvCoordenadas = graphene.String(required=True)
    estadoProvNomenclatura = graphene.String(required=True)
    estadoProvCicloLectura = graphene.String(required=True)
    estadoProvCicloReparto = graphene.String(required=True)
    estadoProvCorreriaLectura = graphene.String(required=True)
    estadoProvCorreriaReparto = graphene.String(required=True)
    cicloLectura = graphene.String(required=True)
    cicloReparto = graphene.String(required=True)
    tipoCorreria = graphene.String(required=True)
    correriaLectura = graphene.String(required=True)
    correriaReparto = graphene.String(required=True)
    iniRutaLectura = graphene.String(required=True)
    rutaLectura = graphene.String(required=True)
    rutaReparto = graphene.String(required=True)
    pais = graphene.String(required=True)
    divTerritorial1 = graphene.String(required=True)
    divTerritorial2 = graphene.String(required=True)
    divTerritorial3 = graphene.String(required=True)
    divTerritorial4 = graphene.String(required=True)
    divTerritorial5 = graphene.String(required=True)
    divTerritorial6 = graphene.String(required=True)
    zonaPostal = graphene.String(required=True)
    estadoGeocodificacion = graphene.String(required=True)
    descripcion = graphene.String(required=True)
    estado = graphene.String(required=True)
    zonaOperativa = graphene.String(required=True)
    localidadOperatica = graphene.String(required=True)
    acopio = graphene.String(required=True)
    codDireccionAcopio = graphene.String(required=True)
    codEstandarizacion = graphene.String(required=True)
    estadoHomologacion = graphene.String(required=True)
    tipoCruce = graphene.String(required=True)
    coordenadaZ = graphene.String(required=True)
    cedulaCatastral = graphene.String(required=True)
    sectorOperativo = graphene.String(required=True)

class GenericData(graphene.ObjectType):
    status =graphene.String(required=True)
    message=graphene.String(required=True)
    results=graphene.List(MarcoPoloDireccionPub)

    
# type Query
class Query(graphene.ObjectType):
    hello = graphene.String(value=graphene.String(default_value="world."))
    getSampleItem = graphene.Field(MarcoPoloDireccionPub)
    readItems = graphene.List(MarcoPoloDireccionPub)
    readItemsTwo = graphene.List(MarcoPoloDireccionPub, valorCoorX=graphene.String(), valorCoorY=graphene.String())
    readCoordenadas = graphene.List(GenericData, longitud=graphene.String(), latitud=graphene.String())
    readCodInstalacion = graphene.List(GenericData, codInstalacion=graphene.String())


    def resolve_hello(self, info, value):
        return 'Hello ' + value + '\n'
    
    def resolve_getSampleItem(self, info):
        item = MarcoPoloDireccionPub(nomenclatura="CL 12 C SUR CR 53 -73", codInstalacion="041512303000730000",
    longitud="-75.59284067", latitud="6.19676160")
        return item

    def resolve_readItems(self, info):
        results = connectiondb.DB_DATA
        return results

    def resolve_readCodInstalacion(self, info, codInstalacion):
        results = DatabaseConnection().read_codInstalacion(codInstalacion)
        return results

    def resolve_readCoordenadas(self, info, longitud, latitud):
        results = DatabaseConnection().read_info(longitud, latitud)
        return results
        
class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query
            # auto_camelcase=True
            # mutation=Mutation
        )
        pass

    def query(self, query):
        # results = self.schema.execute(query, middleware=[timing_middleware,AuthorizationMiddleware()]) #authorization_middleware])
        results = self.schema.execute(query)
        return json.dumps(results.data)
        
    def queryWithContext(self, query, context):
        results = self.schema.execute(query, context=context)
        return results
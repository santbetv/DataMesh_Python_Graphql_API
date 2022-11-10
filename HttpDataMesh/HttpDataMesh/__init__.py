import re
import azure.functions as func
import json
from logging import getLogger
from ..exception import exceptions
from ..graphqllib.graphql import GraphQL, Query
logger = getLogger(__name__)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.info('Python HTTP trigger function processed a request.')

    query = req.params.get('query')
    if not query:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            query = req_body.get('query')

    try:
        print(req.headers)
        results = GraphQL().query(query)
    except Exception as e:
        logger.error('Error 500 ---->'+e)
        return exceptions.errorServer()

    if results:
        if results != "null":
            return exceptions.generic(results)
        else:
            logger.error('Error in query ---->')
            return exceptions.errorNOTFOUND()
    else:
        logger.error('Error in query ---->')
        return exceptions.errorNOTFOUND()

import azure.functions as func
import json
from graphql import GraphQLError
from enum import Enum

from logging import getLogger
logger = getLogger(__name__)

class MessageError(Enum):
    serverError = "Internal Server Error",
    failedQuery = "Error in Query"

def errorServer():
    return func.HttpResponse(
             MessageError.serverError.value,
             status_code=500,
             mimetype="application/json"
    )

def errorNOTFOUND():
    return func.HttpResponse(
             MessageError.failedQuery.value,
             status_code=400,
             mimetype="application/json"
        )

def Ok(results):
    return func.HttpResponse(f"{results}",
             status_code=200,
             mimetype="application/json"
             )

def generic(results):
    countAttributes =3
    ini_string = json.loads(results)

    for item in ini_string:
        if len(ini_string[item][0]) != countAttributes:
            return errorNOTFOUND()
        else:
            value=ini_string[item][0]['status']
            
    return func.HttpResponse(f"{results}",
             status_code=value,
             mimetype="application/json"
             )        

def validator(status, message, results):
    thisData = [{"message": message,"results": results, "status": status}]
    if status < 500:
        if status >= 400 and status <= 499:
            logger.error('Error 400 ---->' +message)
            return thisData
        else:
            return thisData
    else:
        logger.error('Error 500 ---->' +message)
        return thisData

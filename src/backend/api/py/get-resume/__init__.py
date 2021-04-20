import logging
import json

import azure.functions as func
import resume_data as rdata


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = rdata.get_resume()
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})

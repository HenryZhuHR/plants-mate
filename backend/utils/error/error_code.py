ERROR_DICT = {}
import json
from django.http import HttpResponse


def ReturnHttpResponse(code: int, message: str):
    return HttpResponse(json.dumps({
        "code": code,
        "message": message,
    }), content_type="application/json")


class ErrorResponse:
    """
        Custom Error Response encapsulated from `django.http.HttpResponse`
        ---
    """

    class Request:
        @staticmethod
        def ErrorMethod(method: str = ""):
            return ReturnHttpResponse(101, "Error Request method: " + method)
    
    class Data:
        @staticmethod
        def ErrorType(type: str = ""):
            return ReturnHttpResponse(110, "Error Data type: " + type)
    
    class Parameter:
        @staticmethod
        def Missing(param: str = ""):
            return ReturnHttpResponse(120, "Missing Parameter. " + f"Please check parameter <{param}> if in your data")
        @staticmethod
        def Error(Message: str = ""):
            return ReturnHttpResponse(121, "Error Parameter. " + Message)
        @staticmethod
        def Invalid(Message: str = ""):
            return ReturnHttpResponse(122, "Invalid Parameter. " + Message)


    # process from 2__
    # network from 3__

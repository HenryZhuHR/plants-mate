ERROR_DICT = {}
import json
from django.http import HttpResponse


def ReturnHttpResponse(Code: int, Message: str):
    return HttpResponse(json.dumps({"Error": {
        "Code": Code,
        "Message": Message,
    }}), content_type="application/json")


class ErrorResponse:
    """
        Custom Error Response encapsulated from `django.http.HttpResponse`
        ---
    """
    # request 1__
    RequestMethod_Code = 110
    RequestMethod_Mesg = "This request must send a json like data. Please check your data"

    NoJsonContentType_Code = 110
    NoJsonContentType_Mesg = "This request must send a json like data. Please check your data"

    class Parameter:
        @staticmethod
        def Missing(param: str = ""):
            return ReturnHttpResponse(120, "Missing Parameter. " + f"Please check parameter <{param}> if in your data")
        def Error(Message: str = ""):
            return ReturnHttpResponse(121, "Error Parameter. " + Message)
        def Invalid(Message: str = ""):
            return ReturnHttpResponse(122, "Invalid Parameter. " + Message)


    # process from 2__
    # network from 3__

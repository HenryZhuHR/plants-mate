ERROR_DICT={

}

class ERROR_CODES:
    NoJsonContentType_Code=110
    NoJsonContentType_Mesg="This request must send a json like data. Please check your data"
    MissingParameter_Code=110
    @staticmethod
    def MissingParameter_Mesg(param:str):
        return "Missing Parameter. Please check parameter '%s' if in your data"%param



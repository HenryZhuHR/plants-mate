from typing import List

import re

from datetime import datetime


class TIME_MATCH:
    class VALID:
        YYYY = r"\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3}"
        DATE_TIME = r"((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))"

    DATE = r"(\d{4}-\d{1,2}-\d{1,2})"
    TIME = r"(\d{1,2}:\d{1,2}:\d{1,2})"
    DATETIME = r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})"


class CHECK_DATETIME:
    @staticmethod
    def is_valid_date(date_str: str):
        ret = re.search(TIME_MATCH.DATE, date_str)
        return True if ret else False

    @staticmethod
    def is_valid_time(time_str: str):
        ret = re.search(TIME_MATCH.TIME, time_str)
        return True if ret else False


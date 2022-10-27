from typing import List


def check_key(given_dict:dict,keys:List[str]):
    is_exist=True
    for key in keys:
        if key not in given_dict:
            is_exist=False
    return is_exist
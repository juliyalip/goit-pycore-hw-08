import re

def is_valid_date_format(date:str)->bool:
    
    if not isinstance(date, str):
        return False
    pattern = r"\d{2}\.\d{2}\.\d{4}"  
    return bool(re.fullmatch(pattern, date)) 





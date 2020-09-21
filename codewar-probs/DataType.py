# Codewar check data type
import datetime
def data_type(value):
    if isinstance(value, list):
        return "list"
    elif isinstance(value, dict):
        return "dictionary"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value,float):
        return "float"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, datetime.date):
        return "date"
    else:
        return type(value)

'''
def data_type(value):
    types = {list: 'list', dict: 'dictionary', str: 'string', int: 'integer',
             float: 'float', bool: 'boolean', datetime.date: 'date'}

    t = type(value)
    return types[t]
'''
print(data_type(datetime.date(2018,1,1)))

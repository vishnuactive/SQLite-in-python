import os
import json
from tabulate import tabulate

DATA_DIR = "data"

def load_file_path(tablename):
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    return os.path.join(DATA_DIR,f"{tablename}.json")

def load_table(tablename):
    file_path = load_file_path(tablename)
    db_data = None
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            db_data = json.load(file)
    else:
        raise Exception(f"Table does not exist : {tablename}")
    return db_data

def create_table(tablename,columns):
    try:
        file_path = load_file_path(tablename=tablename)
        if os.path.exists(file_path):
            raise Exception(f"Table '{tablename}' already exist")
        schema = {
            "schema":columns,
            "rows" : []
        }
        save_table(tablename,schema)
    except Exception as ex:
        raise ex

def load_columns_with_type(records):
    db_data = {}
    for record in records:
        db_data[record['name']] = record['type']
    return db_data

def insert_into_table(tablename,data):
    try:
        table = load_table(tablename)
        db_data = load_columns_with_type(table["schema"])
        if set(db_data.keys()) != set(data.keys()):
            raise Exception(f"Column mismatch. Expected : {set(db_data.keys())} Got : {set(data.keys())}")
        record = {}
        for key,value in data.items():
            if db_data[key] == "int":
                try:
                    record[key] = int(value)
                except Exception:
                    raise Exception(f"Data type mismatch for '{key}' Expected integer type")
            elif db_data[key] == "text":
                try:
                    record[key] = str(value)
                except Exception:
                    raise Exception(f"Data type mismatch for '{key}' Expected text type")
            elif db_data[key] == "float":
                try:
                    record[key] = float(value)
                except Exception:
                    raise Exception(f"Data type mismatch for '{key}' Expected float type")
        table['rows'].append(record)
        save_table(tablename,table)
    except Exception as ex:
        raise ex

def select_data(tablename):
    try:
        table = load_table(tablename)
        print(tabulate(table['rows'], headers="keys", tablefmt="grid"))
    except Exception as ex:
        raise ex
def save_table(tablename,schema):
    try:
        with open(load_file_path(tablename),"w") as file:
            json.dump(schema,file,indent=4)
        print(f"Query ok. {len(schema['rows'])} rows affected ✅ ")
    except Exception as ex:
        raise ex
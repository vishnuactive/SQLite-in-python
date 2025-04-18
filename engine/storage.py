import os
import json

DATA_DIR = "data"

def load_file_path(tablename):
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    return os.path.join(DATA_DIR,f"{tablename}.json")

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
        print("Query ok. 0 rows affected ✅ ")
    except Exception as ex:
        raise ex

def save_table(tablename,schema):
    try:
        with open(load_file_path(tablename),"w") as file:
            json.dump(schema,file,indent=4)
    except Exception as ex:
        raise ex
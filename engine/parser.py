def parse_query(sql_query):
    try:
        if not sql_query.endswith(';'):
            sql_query += ';'
        if sql_query.upper().startswith("CREATE TABLE"):
            return parse_create_table_statement(sql_query)
        elif sql_query.upper().startswith("SELECT"):
            return parse_select_statement(sql_query)
        elif sql_query.upper().startswith("INSERT INTO"):
            return parse_insert_into_statement(sql_query)
        elif sql_query.upper().startswith("UPDATE"):
            return parse_update_statement(sql_query) 
        elif sql_query.upper().startswith("DELETE FROM"):
            return parse_delete_statement(sql_query)
        else:
            raise Exception("Unknown SQL Statement Encountered")
    except Exception as ex:
        print({"type":"ERROR","error":str(ex)})

    
def parse_create_table_statement(sql_query):
    try:
        query_data = sql_query.strip(';').split("(")
        tablename = query_data[0].split()[2]
        table_args = query_data[1].rstrip(")").split(",")
        create_table_data = {"type":"CREATE",'columns':[]}
        create_table_data['table'] = tablename
        for argument in table_args:
            create_table_data['columns'].append({"name":argument.split()[0].lower(),"type":argument.split()[1].lower()})
        return create_table_data
    except Exception as ex:
        raise Exception("You have an error in your SQL Syntax.Please double-check your query")

def parse_select_statement(sql_query):
    try:
        tokens = sql_query.strip(';').split()
        if tokens[1] != "*":
            raise Exception("Only * supported as of now")
        tablename = tokens[3]
        return {"type":"SELECT","table":tablename}
    except Exception as ex:
        if "Only * supported as of now" in str(ex):
            raise ex
        else:
            raise Exception("You have an error in your SQL Syntax.Please double-check your query")

def parse_insert_into_statement(sql_query):
    try:
        tokens = sql_query.strip(';').split()
        tablename,args = tokens[2].split("(")[0],tokens[2].split("(")[1].strip(')').split(",")
        values = [element.replace("\"","").replace("\'","") for element in tokens[3].split("(")[1].strip(')').split(",")]
        return {"type":"INSERT","table":tablename,"values":dict(zip(args,values))}
    except Exception as ex:
        raise Exception("You have an error in your SQL Syntax.Please double-check your query")

def parse_update_statement(sql_query):
    try:
        tokens = sql_query.strip(';').split()
        tablename = tokens[1]
        if tokens[2].lower() != "set":
            raise Exception(f"INCORRECT Keyword : {tokens[2]}")
        update_data = {}
        for record in tokens[3].split(","):
            key,value = record.split("=")[0],record.split("=")[1]
            update_data[key] = value.replace("\"","").replace("\'","")
        return {'type':'UPDATE','table':tablename,'values':update_data}
    except Exception as ex:
        if "INCORRECT Keyword" in str(ex):
            raise ex
        raise Exception("You have an error in your SQL Syntax.Please double-check your query")

def parse_delete_statement(sql_query):
    try:
        tokens = sql_query.strip(';').split()
        tablename = tokens[2]
        return {"type":"DELETE","table":tablename}
    except Exception as ex:
        raise Exception("You have an error in your SQL Syntax.Please double-check your query")
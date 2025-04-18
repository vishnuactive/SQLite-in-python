import sys
from engine import parser
from engine import storage

def run_interpreter():
    print("Welcome to PySQLite, A 'Scaled-down' version of SQLite. Type '.exit' or '.quit' to Exit")
    while True:
        try:
            command = input("PySQLite >").strip()
            if not command: # If user did not type anything
                continue
            elif command.lower() in (".exit",".quit"):
                print("Exiting From SQLite.Goodbye!")
                break
            
            output = parser.parse_query(command)
            if output:
                if output['type'] == "CREATE":
                    storage.create_table(output['table'],output['columns'])
                elif output['type'] == "INSERT":
                    storage.insert_into_table(output['table'],output['values'])
                elif output['type'] == "SELECT":
                    storage.select_data(output['table'])
        except KeyboardInterrupt:
            print("\nExiting from PySQLite.Goodbye!")
            sys.exit()
        except Exception as ex:
            print(f"Error : {str(ex)} ❌ ")


if __name__ == '__main__':
    run_interpreter()
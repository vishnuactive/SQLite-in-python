import sys

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
            
            print(f"Received Command : {str(command)}")
        except KeyboardInterrupt:
            print("\nExiting from pySQLite.Goodbye!")
            sys.exit()
        except Exception as ex:
            print(f"Error : {str(ex)}")


if __name__ == '__main__':
    run_interpreter()
'''
File: create_database.py
Purpose:
    Create the database, create tables, then populate rows.
'''
import os

# current directory
build_dir = os.path.dirname(os.path.abspath(__file__))

# connect to schema directory
schema_dir = os.path.join(build_dir, "..", "schema")

# list of files in schema
scripts = os.listdir(schema_dir)

def create_database():
    """This will pull all the functions together and act as the main"""

    pass


def parse_script_folder():
        
    pass
    



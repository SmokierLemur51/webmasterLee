'''
File: create_database.py
Purpose:
    Create the database, create tables, then populate rows.
'''
import os
import subprocess

# current directory
build_dir = os.path.dirname(os.path.abspath(__file__))

# connect to schema directory
schema_dir = os.path.join(build_dir, "..", "schema")

# list of files in schema
scripts = os.listdir(schema_dir)

# absolute path of scritps
abs_path_scripts = [os.path.join(schema_dir, s) for s in scripts]


def create_database(schema_file):
    """This will pull all the functions together and act as the main"""
    subprocess.run(f"sqlite3 testing.db < {schema_file}", shell=True)
    

create_database(abs_path_scripts[0])

def parse_script_folder():
    """
    List files in directory, user selects which to execute.
    """
    pass
    

def write_log():
    """
    Write actions to log file so it is easy to pick back up or get 
    a newbie up to speed quickly.
    """
    pass



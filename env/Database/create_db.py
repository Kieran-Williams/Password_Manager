import sqlite3
from sqlite3 import Error
from pathlib import Path
from Database import create_tables

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print('DB Version' + e)
    finally:
        if conn:
            conn.close()

def create_db():
    create_connection(r'Database/password_manager.db')
    db = Path(str(Path().absolute()) + '/Database/password_manager.db')
    if db.exists():
        create_tables.main()
        return(1)
    else:
        return(0)
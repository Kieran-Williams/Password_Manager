import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"password_manager.db"

    users_table = """CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL,
                        password text NOT NULL
                    ); """

    passwords_table = """CREATE TABLE IF NOT EXISTS passwords (
                            id integer PRIMARY KEY,
                            user_id integer NOT NULL,
                            password text NOT NULL,
                            app_name text NOT NULL,
                            app_url text,
                            created_date text NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES people (id)
                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, users_table)

        # create tasks table
        create_table(conn, passwords_table)
    else:
        print("Error! cannot create the database connection.")

main()
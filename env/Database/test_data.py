import sqlite3
from sqlite3 import Error
import datetime

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_user(conn, users):
    sql = ''' INSERT INTO users(username,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, users)
    conn.commit()
    return cur.lastrowid

def create_password(conn, password):
    sql = ''' INSERT INTO passwords(user_id,password,app_name,app_url,created_date)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, password)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"password_manager.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new user
        user = ('Kieran', 'Password');
        user_id = create_user(conn, user)
        date = datetime.date.today().strftime('%Y-%m-%d')

        # passwords
        password_1 = (user_id, 'Password1', 'App1', 'App1.com', date)
        password_2 = (user_id, 'Password2', 'App2', 'App2.com', date)

        # create passwords
        #create_password(conn, password_1)
        #create_password(conn, password_2)

main()
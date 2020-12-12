import sqlite3
import datetime
from sqlite3 import Error
import hashing

database = r"Database/password_manager.db"


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def check_if_users_empty():
    # create a database connection
    conn = create_connection(database)

    sql = ''' SELECT count(*) 
                FROM users; '''
    cur = conn.cursor()
    cur.execute(sql)
    count = cur.fetchone()[0]
    return count


def check_if_username_exists(username):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = ?", (username, ))
    data = cur.fetchone()
    if data is None:
        return 0
    else:
        return 1


def create_new_user(username, password):
    # create a database connection
    conn = create_connection(database)
    user_id = hashing.generate_random_user_id()
    salt = hashing.generate_salt()
    user = (user_id, username, password, salt)
    sql = ''' INSERT INTO users(id, username, password, salt)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    created = cur.lastrowid
    if created == 0:
        return("An error has occured")
    else:
        return("User created successfully")


def create_new_password(user_id, encrypted_password, plain_text_password, app_name, app_url):
    # create a database connection
    conn = create_connection(database)
    created_date = datetime.date.today().strftime('%Y-%m-%d')
    insert = (user_id, encrypted_password, app_name, app_url, created_date)
    sql = ''' INSERT INTO passwords(user_id, password, app_name, app_url, created_date)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, insert)
    conn.commit()
    created = cur.lastrowid
    if created == 0:
        return("An error has occured")
    else:
        return("Password created successfully", app_name, app_url, plain_text_password)


def hash_login(username):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (username, ))
    data = cur.fetchone()
    if data is None:
        return 0
    else:
        return(data[0])


def hash_login_id(user_id):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE id = ?", (user_id, ))
    data = cur.fetchone()
    if data is None:
        return 0
    else:
        return(data[0])


def db_login(username, password):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE username = ? AND password = ?", (username, password, ))
    data = cur.fetchone()
    if data is None:
        cur.execute("SELECT username FROM users WHERE username = ?", (username, ))
        result = cur.fetchone()
        if result is None:
            return 1
        else:
            return 2
    else:
        return 0


def get_user_id(username):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = ?", (username, ))
    data = cur.fetchone()
    return(data[0])


def get_password_app_name(app_name, user_id):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT password FROM passwords WHERE app_name = ? and user_id = ?", (app_name, user_id, ))
    data = cur.fetchone()
    if data is None:
        return(0)
    else:
        return(data)[0]


def get_password_app_url(app_url, user_id):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT password FROM passwords WHERE app_url = ? and user_id = ?", (app_url, user_id, ))
    data = cur.fetchone()
    if data is None:
        return(0)
    else:
        return(data)[0]


def update_password_app_name(user_id, encrypted_password, app_name):
    # create a database connection
    conn = create_connection(database)
    created_date = datetime.date.today().strftime('%Y-%m-%d')
    insert = (encrypted_password, created_date, user_id, app_name)
    sql = ''' UPDATE passwords SET password = ?, created_date = ?
              WHERE user_id = ? AND app_name = ?;'''
    cur = conn.cursor()
    cur.execute(sql, insert)
    created = cur.rowcount
    if created == 0:
        return(0)
    else:
        conn.commit()
        return(1)


def update_password_app_url(user_id, encrypted_password, app_url):
    # create a database connection
    conn = create_connection(database)
    created_date = datetime.date.today().strftime('%Y-%m-%d')
    insert = (encrypted_password, created_date, user_id, app_url)
    sql = ''' UPDATE passwords SET password = ?, created_date = ?
              WHERE user_id = ? AND app_url = ?;'''
    cur = conn.cursor()
    cur.execute(sql, insert)
    created = cur.rowcount
    if created == 0:
        return(0)
    else:
        conn.commit()
        return(1)


def delete_password_app_name(user_id, app_name):
    # create a database connection
    conn = create_connection(database)
    insert = (user_id, app_name)
    sql = ''' DELETE FROM passwords WHERE user_id = ? AND app_name = ? '''
    cur = conn.cursor()
    cur.execute(sql, insert)
    created = cur.rowcount
    if created == 0:
        return(0)
    else:
        conn.commit()
        return(1)


def delete_password_app_url(user_id, app_url):
    # create a database connection
    conn = create_connection(database)
    insert = (user_id, app_url)
    sql = ''' DELETE FROM passwords WHERE user_id = ? AND app_url = ? '''
    cur = conn.cursor()
    cur.execute(sql, insert)
    created = cur.rowcount
    if created == 0:
        return(0)
    else:
        conn.commit()
        return(1)


def get_all_passwords(user_id):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE user_id = ?", (user_id, ))
    data = cur.fetchall()
    if data is None:
        return(0)
    else:
        return(data)


def get_user_salt(user_id):
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT salt FROM users WHERE id = ?", (user_id, ))
    data = cur.fetchone()
    if data is None:
        return(0)
    else:
        return(data)


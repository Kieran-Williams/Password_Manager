import password_generator
from Database import db_calls

def create_new_password(user_id):
    app_name = input('What is the name of the app:')
    app_url = input('What is the app URL, one is not required:')
    password = password_generator.generate()
    return(db_calls.create_new_password(user_id, password, app_name, app_url))

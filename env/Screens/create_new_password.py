import password_generator
from Database import db_calls
import hashing

def create_new_password(user_id, user_password):
    app_name = input('What is the name of the app:')
    app_url = input('What is the app URL, one is not required:')
    plain_text_password = password_generator.generate()
    encrypted_password = hashing.encrypt_password(user_password, plain_text_password, user_id)
    return(db_calls.create_new_password(user_id, encrypted_password, plain_text_password, app_name, app_url))

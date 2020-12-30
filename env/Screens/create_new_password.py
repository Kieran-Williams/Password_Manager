import password_generator
from Database import db_calls
import hashing

def create_new_password(user_id, user_password):
    app_name = input('What is the name of the app:')
    while True:
        if app_name == '':
            app_name = input('You need to enter an app name:')
        else:
            if db_calls.check_if_appname_exists(app_name) == 1:
               app_name = input('That app name already exists please enter a new app name:')
            elif db_calls.check_if_appname_exists(app_name) == 0:
                break
            else:
                print('Error. Exiting Application')
                exit()
    app_url = input('What is the app URL, one is not required:')
    plain_text_password = password_generator.generate()
    encrypted_password = hashing.encrypt_password(user_password, plain_text_password, user_id)
    return(db_calls.create_new_password(user_id, encrypted_password, plain_text_password, app_name, app_url))

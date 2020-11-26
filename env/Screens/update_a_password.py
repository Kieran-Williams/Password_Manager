from text_formatting import remove_spaces
from Database.db_calls import get_password_app_name, get_password_app_url, update_password_app_name, update_password_app_url
from password_generator import generate

def update_password(user_id):
    app = input('1.App Name \n2.App URL \nHow do you want to update the password:')
    while True:
        app = remove_spaces(app)
        if app.casefold() in ('1', 'appname'):
            app_name = input('What is the name of the app:')
            while True:
                if app_name == '':
                    app_name = input("You didn't enter a app name please try again:")
                else:
                    break
            response = get_password_app_name(app_name, user_id)
            if response == 0:
                try_again = input("An app with that name doesn't exist. \n1.Try Again \n2.Create a password \nWhat do you want to do:")
                try_again = remove_spaces(try_again)
                if try_again.casefold() in ('1', 'tryagain'):
                    a = 1
                elif try_again.casefold() in ('2', 'createapassword'):
                    return(0)
                else:
                    try_again = input("I didn't understand that please select one of the options:")
            else:
                password = generate()
                response = update_password_app_name(user_id, password, app_name)
                if response == 0:
                    return ('Could not update password')
                elif response == 1:
                    return ('Success', app_name, password)
                else:
                    return('Error')

        elif app.casefold() in ('2', 'appurl'):
            app_url = input('What is the URl of the app:')
            while True:
                if app_url == '':
                    app_url = input("You didn't enter a app url please try again:")
                    break
                else:
                    break
            response = get_password_app_url(app_url, user_id)
            if response == 0:
                try_again = input("An app with that url doesn't exist. \n1.Try Again \n2.Create a password \nWhat do you want to do:")
                try_again = remove_spaces(try_again)
                if try_again.casefold() in ('1', 'tryagain'):
                    a = 1
                elif try_again.casefold() in ('2', 'createapassword'):
                    return(0)
                else:
                    try_again = input("I didn't understand that please select one of the options:")
            else:
                password = generate()
                response = update_password_app_url(user_id, password, app_url)
                if response == 0:
                    return ('Could not update password')
                elif response == 1:
                    return ('Success', app_url, password)
                else:
                    return('Error')
        else:
            app = input("Sorry I didn't reconginse that please select one of the optoins:")
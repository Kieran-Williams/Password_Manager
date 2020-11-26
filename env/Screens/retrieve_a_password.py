from text_formatting import remove_spaces
from Database.db_calls import get_password_app_name, get_password_app_url

def retrieve_password(user_id):
    app = input('1.App Name \n2.App URL \nHow do you want to retrieve the password:')
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
                return(response)
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
                return(response)
        else:
            app = input("Sorry I didn't reconginse that please select one of the optoins:")
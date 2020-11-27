from Database import create_db, db_calls
import inital_user_check
from text_formatting import remove_spaces
from Screens import *
from pathlib import Path

db = Path(str(Path().absolute()) + '/Database/password_manager.db')
if db.exists():
    pass
else:
    response = create_db.create_db()
    if response == 0:
        print('Can not install app, please restart')
        exit()
    elif response == 1:
        pass
    else:
        print('Error')
        exit()

x = db_calls.check_if_users_empty()

if x == 0:
    response = (inital_user_check.no_user_exists())
    username = response[1]
    password = response[2]
    print(response[0], '\n''Username is: ' + username, '\n''Password is: ' + password)
else:
    login_or_creatuser = input('1.Login \n2.Create New User \nWhat do you want to do:') 
    while True:
        login_or_creatuser = remove_spaces(login_or_creatuser)
        if login_or_creatuser.casefold() in ('1', 'login'):
            username = input('What is your username:')
            password = input('What is your password:')
            response = inital_user_check.login(username, password)
            if response[0] == 0:
                username = response[1]
                password = response[2]
                break
            elif response == 1:
                print('Error')
                break
        elif login_or_creatuser.casefold() in ('2', 'createnewuser'):
            response = inital_user_check.create_user()
            username = response[1]
            password = response[2]
            print(response[0], '\n''Username is: ' + username, '\n''Password is: ' + password)
            break
        else:
            login_or_creatuser = input("Sorry I didn't reconginse that please select one of the optoins:")

user_id = db_calls.get_user_id(username)
choice = welcome_screen.welcome(username)
while True:
    if choice == '1':
        #Retrieve a password
        response = retrieve_a_password.retrieve_password(user_id)
        if response == 0:
            choice = '2'
        else:
            print(response)
            choice = welcome_screen.welcome(username)
    elif choice == '2':
        #Create a new password
        print(create_new_password.create_new_password(user_id))
        choice = welcome_screen.welcome(username)
    elif choice == '3':
        #Update a password
        response = update_a_password.update_password(user_id)
        if response == 0:
            choice = '2'
        else:
            print(response)
            choice = welcome_screen.welcome(username)
    elif choice == '4':
        #Delete a password
        response = delete_a_password.delete_password(user_id)
        if response == 0:
            choice = welcome_screen.welcome(username)
        else:
            print(response)
            choice = welcome_screen.welcome(username)
    elif choice == '5':
        #View all passwords
        response = view_all_passwords.all_passwords(user_id)
        if response == 0:
            choice = welcome_screen.welcome(username)
        else:
            for i in response:
                print('App Name:', i[0], ' App URL:', i[1], ' Password:', i[2], ' Updated Date:', i[3], '\n')
            choice = welcome_screen.welcome(username)
    elif choice == '6':
        #Exit Password Manager
        print('Exiting Password Manager...')
        exit()
    else:
        print('Error')
from Database.db_calls import check_if_username_exists, create_new_user, db_login
from text_formatting import remove_spaces


def no_user_exists():
    print('You need to set up an account to use the Password Manager')
    i = input('Would you like to set up an account, Yes or No?')
    i = remove_spaces(i)
    while True:
        if i.casefold() == 'yes':
            return(create_user())
        elif i.casefold() == 'no':
            print('Okay, exiting Password Manager')
            exit()
        else:
            i = input("Sorry I didn't recongise what you entered, please enter Yes or No.")
              
            
def create_user():
    print('lets create a new user...')
    username = input('What do you want your username to be?')
    while True:
        if username == '':
            username = input("You didn't enter a username please try again:")
        else:
            if check_if_username_exists(username) == 1:
                username = input('Username ' + username + ' already exists please try another one:')
            elif check_if_username_exists(username) == 0:
                break
    password = input('What do you want your account password to be:')
    while True:
        if password == '':
            password = input("You didn't enter a password please try again:")
        else:
            break
    response = create_new_user(username, password)
    return(response, username, password)


def login(username, password):
    login_attempt = db_login(username, password)
    while True:
        if login_attempt == 0:
            return (0, username, password)
            break
        elif login_attempt == 1:
            print("That username doesn't exist")
            username = input('What is your username:')
            password = input('What is your password:')
            login_attempt = db_login(username, password)
        elif login_attempt == 2:
            print("That password is incorrect")
            password = input('What is your password:')
            login_attempt = db_login(username, password)
        else:
            return 1
            break

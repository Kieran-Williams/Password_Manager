from Database.db_calls import check_if_username_exists, create_new_user, db_login, hash_login
from text_formatting import remove_spaces
import hashing


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
    hash_password = hashing.get_hashed_password(password)
    response = create_new_user(username, hash_password)
    return(response, username, password)


def login(username, plain_text_password):
    hashed_password = hash_login(username)
    while True:
        if hashed_password == 0:
            print("That username doesn't exist")
            username = input('What is your username:')
            plain_text_password = input('What is your password:')
            hashed_password = hash_login(username)
        else:
            login_attempt = hashing.check_password(plain_text_password, hashed_password)
            if login_attempt == True:
                return (0, username, plain_text_password)
                break
            else:
                print("That password is incorrect")
                plain_text_password = input('What is your password:')
                login_attempt = hashing.check_password(plain_text_password, hashed_password)

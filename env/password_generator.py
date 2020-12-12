import random, string, hashing

def generate():
    requirements = input('1.Letter & Number characters \n2.Letter, Number & Special characters \nWhat type of password do you need:')
    length = input('How many characters does the password need to be:')
    if requirements == '1':
        password_characters = string.ascii_letters + string.digits
        plain_text_password = ''.join(random.choice(password_characters) for i in range(int(length)))
        return(plain_text_password)
    elif requirements == '2':
        password_characters = string.ascii_letters + string.digits + string.punctuation
        plain_text_password = ''.join(random.choice(password_characters) for i in range(int(length)))
        return(plain_text_password)
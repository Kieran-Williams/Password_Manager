import random, string

def generate():
    length = input('Tell me how long does your password needs to be:')
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(int(length)))
    return(password)
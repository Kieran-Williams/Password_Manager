import bcrypt
import random
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Database import db_calls


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(12))


def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)


def generate_random_user_id():
    return (random.random()*100000000000000000)


def encrypt_password(user_password, generated_password, user_id):
    key = generate_key(user_password, user_id)
    generated_password = bytes(generated_password, 'utf-8')
    f = Fernet(key)
    enctypted_password = f.encrypt(generated_password)
    return enctypted_password
    
    
def decrypt_password(user_password, encrypted_password, user_id): 
    key = generate_key(user_password, user_id)
    f = Fernet(key)
    holding = f.decrypt(encrypted_password)
    plain_text_password = holding.decode('utf-8')
    return(plain_text_password)


def generate_key(password, user_id):
    password = bytes(password, 'utf-8')
    user_salt = db_calls.get_user_salt(user_id)
    salt = bytes(user_salt[0], 'utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def generate_salt():
    salt = bcrypt.gensalt()
    return salt

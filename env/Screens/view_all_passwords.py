from Database.db_calls import *
from hashing import decrypt_password

def all_passwords(user_id, user_password):
    response = get_all_passwords(user_id)
    if response == 0:
        print('error')
    else:
        holding_list = []
        for i in response:
            a = []
            a.append(i[3])
            if i[4] == '':
                a.append('N/A')
            else:
                a.append(i[4])
            a.append((decrypt_password(user_password, i[2], user_id)))
            a.append(i[5])
            holding_list.append(a)
        return(holding_list)
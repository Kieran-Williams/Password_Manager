def welcome (username):
    print('------------Welcome ' + username + '------------')
    print('1. Retreave a password')
    print('2. Create a new password')
    print('3. Update a password')
    print('4. Delete a password')
    print('5. View all passwords')
    print('6. Exit')
    choice = input('What do you want to do:')
    return choice
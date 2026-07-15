myPassword = {'Amy': 'Anteater', 'Bob': 'Bumblebee', 'Charlie': 'Caterpillar'}

username = 'start'
while username != '':
    print('enter your username or blank to exit:')
    username = input()
    if username in myPassword:
        print ('enter your password')
        password = input()
    
        if password == myPassword[username]:
            print('access granted')
        else:
            for i in range(2):
                print ('Incorrect password. Try again:')
                password = input()
                if password == myPassword[username]:
                    print('access granted')
                    break
                else:
                    print ('access denied')
    else:
        print('user does not exist')
    break
print('exiting program')

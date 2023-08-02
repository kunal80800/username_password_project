--username password--

for i in range(3):
    u=input('enter ypur username:')
    if u=='abc':
        print('welcome')
        for j in range(3):
            p=input('enter your password: ')
            if p=='12345':
                print('successfully login')
                break
            else:
                print('invalid password')
        break
    else:
        print('invalid')
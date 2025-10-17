#write a program to check whether a given username contains less than  or equal to 10 characters or not?
user_name = input('Enter your user name: ')
if(len(user_name) <= 10):
    print('Your username contaions less than or equal to 10 characters!')
else:
    print('Your user name contains characters more than 10!')

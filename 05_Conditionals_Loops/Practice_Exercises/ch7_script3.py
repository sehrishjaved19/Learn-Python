#write a program to identify whetre a give number is prime or not
n=int(input('Enter an integer: '))

if n<=1:
    print('Number is not prime!')
else:
    for i in range(2,n):
        if n%i == 0:
            print('Number is not prime!')
            break
    else:
        print('Number is prime!')

# In while loop, the condition is checked first. If evaluateds to true, the body of the loop is executed otherwise not!

#if the loop is enetered, the process of[condition check & execution] is continued until the condition becomes False.

i = 1
while(i<6):
    print(i)
    i += 1
#If the condition never become false, the loop keeps getting executed




#write a program to print the content of a list using while loop
l=[1,'hira','qadar',False,'sehrish']

i=0
while(i<len(l)):
    print(l[i])
    i += 1

#print even number
i=2
while(i<=10):
    print(i)
    i += 2

#print odd number
i=1
while(i<=9):
    print(i)
    i += 2

#count down from 5 to 1
z=5
while(z>=1):
    print(z)
    z = z-1

#print message 5 time
count=0
while(count<5):
    print("welcome to the loop!")
    count += 1

#sum numbers untill user enters 0
total=0
num = int(input('Enter a number(0 to stop): '))
while(num != 0):
    total += num
    num = int(input('Enter another number (0 to stop): '))

print('Total sum is: ', total)

#keep asking for password untill correct
password= ""
while password != "python123":
    password=input("Enter password: ")

print("Access granted!")

#infinite loop with break condition
while True:
    name=input('Enter your name( type \'exit\') to quit:  ')
    if name == 'exit':
        break
    print('Hello, ',name)

#print the multiplication table of a number entered by the user
n=int(input('Enter an integer: '))
i=1
while(i<=10):
    print(n,'*',i,'=' ,n*i)
    i += 1

#print the sum of numbers from 1 to 100
i=0
sum=0
while(i<=100):
    sum+=i
    i+=1

print(sum)

#ask the user to guess a secret number until they get it right
secret_num=4
a=int(input('choose one enter from 0 to 9: '))
while(a!=4):
    print('You guessed wrong!')
    a = int(input('Choose another number from 0 to 9: '))

print('You guessed it right!')

#keep asking the user to enter a username until it is atleast 5 characters long

user_name=(input('Enter your user name: '))
while(len(user_name)<5):
    print("❌ Username is too short! Please try again!")
    user_name=(input('Enter your user name again: '))
print('Entered name is valid according to the requirement!')



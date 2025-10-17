#A condition in Python is an expression that evaluates to either True or False, and is used to control the flow of a program — mainly through if statements and loops
a=int(input("Enter your age: "))

if(a>18):
    print('You are above the age of concent!')
    print('Good for you👍!')
elif(a<=0):
    print('You are entering an invalid age!')
else:
    print('you are below the age of concent!')

print('End of program.')

#if elif else ladder
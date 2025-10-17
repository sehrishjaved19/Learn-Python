# Write a program to calculate the factorial of a given number using for loop

#  5!=5*4*3*2*1

n=int(input('Enter an integer: '))
product=1
for i in range (1, n+1):
    product= product*i

print(f'The factorial of {n} is {product}')

'''Write a program to print the following pattern
        *
       ***
      *****
for n=3'''

n = int(input('Enter an integer: '))
for i in range(1,n+1):
    print(' '*(n-i), end="")#end="" will does not move the course to the next line for in the next iteration  while the next iteration will be performed in the same line.
    print('*'*(2*i-1))




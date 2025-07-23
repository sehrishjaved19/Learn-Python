#a function is a group of statements performing a specific task when being called.
#THIS FUNCTION CAN BE CALLED ANY NUMBER OF TIMES, ANYWHERE IN THE PROGRAM

# this is a function Definition(This part containing the exact set of instructions which are executed during the function call.)
def avg():
    name = input('Enter your name: ')
    sub1=int (input('Enter marks of biology: '))
    sub2=int (input('Enter marks of physics: '))
    sub3=int (input('Enter marks of chemistry: '))
    print(f' Dear {name}!, Average Marks of your subjects are { (sub1+sub2+sub3)/3}')


#whenever we want to call a function, we put the name of the function followed by the paranthese as follows:
avg()#this is function call
avg()

#Functions are of two types
#    1.Built-in function(e.g: print(), len(), etc)
#    2.User defined function(e.g: thr avove definition function)

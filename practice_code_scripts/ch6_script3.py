#program to print eith msg is spam or not!
p2 = 'Make a lot of money'
p1 = 'buy now'
p3 = 'subscribe this'
p4 = 'click this'

message=input('Enter Your Comment: ')

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print('This comment is a spam!')
else:
    print('This comment is not a spam!')

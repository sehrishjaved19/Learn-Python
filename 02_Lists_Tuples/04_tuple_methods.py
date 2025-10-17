a=('hello',False,35, False,65.78,False,'newage')
print(a)

no=a.count(False)
print(no)#use to display how many time a particukar value is present in the tuple.as False is 3 times present in the tuple, it will display 3 as output

i=a.index(False)
print(i)#it will returns the first index of a particular value

repeat=(1,2,3)
r=repeat*5#this will print the value of repeat 5 time
print(r)

tuple1=(1,2,3)
tuple2=(4,5,6)
s=tuple1+tuple2
print(s)#this will join these two tuples into one tuple

q=(35,50,60,90,'hello')
print(60 in q)#this will give boolean falue either 60 is present in q or not

q=(35,50,60,90,'hello')
print(len(q))#give length of tuple


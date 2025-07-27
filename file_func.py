f = open('file.txt')
lines = f.readlines()# readlines () will read the attached file and converts its lines into the itams of list , and print that list in output
print(lines, type(lines))
f.close()

f= open('file.txt')
line1 = f.readline()#wwill print first line  when readline is first called , if again called then it will read 2nd line if again then 3rd line and so on
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
f.close()

#to print the complete txt file, we can use while loop,
f= open('file.txt')
line= f.readline()
while(line != ''):
    print(line)
    line= f.readline()

f.close()




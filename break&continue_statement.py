#the BREAK statement: is used  to come out of the loop when encountered. It instructs program to exit the loop now.
for i in range(0,80):
    if i ==3:
        break#exit the loop right now
    print(i)


#Continue statement
for i in range(100):
    if(i==34):
        continue#skip this itreation will remove 34 from iteration
    print(i)
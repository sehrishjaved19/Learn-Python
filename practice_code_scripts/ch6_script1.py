num1 = int(input("Enter an integer1: "))
num2 = int(input("Enter an integer2: "))
num3 = int(input("Enter an integer3: "))
num4 = int(input("Enter an integer4: "))
if(num1>num2 and num1>num3 and num1>num4):
    print("Interer1 is Greater!")
elif(num2>num1 and num2>3 and num2>num4):
    print("Integer2 is greater!")
elif( num3>num1 and num3>num2 and num3>num4):
    print("Integer3 is greater!")
else:
    print("Integer4 is greater!")

#another way
num_a= int(input("Enter an integer_a: "))
num_b= int(input("Enter an integer_b: "))
num_c= int(input("Enter an integer_c: "))
num_d= int(input("Enter an integer_d: "))

greatest=max(num_a,num_b,num_c,num_d)
print("The Greatest number is ",greatest)


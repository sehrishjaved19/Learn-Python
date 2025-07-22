#Write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33%in each subject to pass. Assume 3 subjects and take marks as an input from the user.
subject_1=int(input("Enter marks of Math: "))
subject_2=int(input("Enter marks of Biology: "))
subject_3=int(input("Enter marks of Physics: "))

total_percentage = (100*(subject_1 + subject_2 + subject_3))/300
if(total_percentage>=40 and subject_1>=33 and subject_2>=33 and subject_3>=33):
    print("You are pass!")
else:("You failed!")
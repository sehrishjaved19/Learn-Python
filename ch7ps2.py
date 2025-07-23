#Write a program to greet all the persons names stored in a list and wich start with S

l=["Usman", "Sehrish", "Seher", "Aiman"]
for name in l:
    if(name.startswith('S')):
        print(f'Hello, {name}!')
#Write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'.

with open('poem.txt') as f:
    content = f.read()
    if('twinkle' in content):
        print('The word Twinkle is present in the content!')
    else:
        print('The word Twinkle is not present in the content!')

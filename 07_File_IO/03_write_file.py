# Writing to a file (overwrites previous content)
st = 'A thing of beauty is a joy for ever!'
f=open('myfile.txt', 'w')

f.write(st)
f.close()
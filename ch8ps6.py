#write a python function to remove a given word from a list ad strip it at the same
def remove(l,word):
    n=[]  
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ['Sehrish','Aimanry','Fatima','ry']
print(remove(l,'ry'))

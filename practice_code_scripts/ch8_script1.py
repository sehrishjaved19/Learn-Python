#write a program using functions to find greatest of these numbers.

def greatest(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return a
    else:
        return c
a=1
b=2
c=3

print(greatest(a, b, c))

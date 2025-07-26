#write a puthon program tp print the multiplication table of given number
def table(n):
    for i in range(1, 11):
        print(f'{n}x{i} = {n*i}')

table(8)
s1={1,3,6,78}
s2={ 1,78,45,76,12}
print(s1.union(s2))
print(s1|s2)#another way of union

print(s1.intersection(s2))
print(s1&s2)#another way of intersection

print(s1-s2)#is for difference

print(s1^s2)#symmetric difference(combine the elemnts of set1 and set2 and ignore the elements that are common in them) 

a={'aiman':'learner',
   'zara':'student',
   'farah':'2no.'}
print(a.items())#provide the values of dict pairs, in the form of tuple

print(a.keys())#will print only keys from dict
print(a.values())#will print only values from dict
#notice output
a.update({'aiman':45,'khadija':'teacher'})
print(a)
print(a['aiman'])
print(a.get('farah'))
print(a.get('hello'))#will print none
# print(a['hello'])     #will print error msg

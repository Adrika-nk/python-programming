#reversing the tuple
'''
tuple=[23,64,83,54,19]
rev=tuple[::-1]
print(rev)
'''

#access value 20 which is 5th item
'''
tuple=[23,64,83,54,19,20]
print(tuple.index(20))
'''

#create tuple with singke item 50
'''
tuple=50,
print(tuple)
print(type(tuple))
'''

#unpack the tuple into 4 variables
'''
tuple=42,26,46,84
a,b,c,d=tuple
print(a,b,c,d)
'''

#swap two tuples
'''
a=63,47,72,'adrika'
b=36,57,26,'anil'
a,b=b,a
print(a,b)
'''

#copy an element from one tuple to new
'''
tuple=42,26,46,84
newtup=(tuple[2])
print(newtup)
'''

#modify the tuple
'''
tup=1,2,3,4,'adr'
l=list(tup)
print(l)
print(type(l))
l[3]=1000
print(l)
tup=tuple(l)
print(tup)
'''

#sort a tuple
'''
a=2,4,7,4,1,8,5,9
sortedtuple=tuple(sorted(a))
print(sortedtuple)
'''

#counting number of time 50 in a tuple

tup=(50,25,47,50)
print(tup.count(50))

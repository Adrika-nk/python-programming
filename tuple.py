#tuple
'''tuple1=(0,1,2,3)
tuple2='python','program'
tuple3=(tuple1,tuple2)

print(1 in tuple1)
'''

#list
'''list1=[1]
print(type(list1))
'''


'''tup1=("python")*3
print(tup1)

tup1=("python,")*3
print(tup1)
'''


#reassign
'''tuple1=(0,1,2,3)
tuple[0]=4
print(tuple1)

TypeError: 'type' object does not support item assignment
'''

#delete
'''tuple1=(0,1,2,3)
del tuple1[0]
print(tuple1)

TypeError: 'tuple' object doesn't support item deletion
'''

#append
'''list=[1,2,3,4]
tuple1=(0,1,2,3)
del tuple1[0]
'''

'''tuple1=(0,1,2,3)
y=list(tuple1)
y.remove(1)
tuple1=tuple(y)
print(tuple1)
'''

'''tuple1=1,2,3
a,b,c,d=tuple1
print(a,b,c,d)
'''

#count
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=tup.count(4)
print(x)
'''

#sum
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
sum=sum(tup)
print(sum)
'''

#len
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=len(tup)
print(x)
'''

#max
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=max(tup)
print(x)
'''

#min
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=min(tup)
print(x)
'''

#index
'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=(tup.index(7))
print(x)
'''

'''tup=(1,2,3,4,5,2,3,5,4,7,6,4)
x=(tup.index(10))
print(x)
'''

#loop through tuple and index number
'''tup1=("apple","banana","cherry")
for x in range(len(tup1)):
    print(x)
 '''     
#using while loop

#zipping
firstname=("Simon","Sarah","Mehdi")
lastname=("Sinek","Smith","Lopes")
ages=(20,22,25)
zipped=zip(firstname,lastname,ages)
print(zipped)
print(list(zipped))

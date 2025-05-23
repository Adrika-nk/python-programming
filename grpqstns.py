#combine two list with same index numbers
'''
li1=['M','na','i','Juli']
li2=['y','me','s','us']
zipped=zip(li1,li2)
print(zipped)
print(list(zipped))

'''

#finding the square of numbers
'''
num=[1,2,3,4,5,6,7]
square=[i**2 for i in num]
print(square)

'''

#removing empty strings
'''
li1=['apple','','banana','','orange']
new=[x for x in li1 if x!='']
print(new)

'''

#removing white spaces

sen='hi hello world'
new=sen.replace(" ","")
print(new)



#sum all items in a list
'''
num=[1,2,4,5,2,4,6,7]
sum=sum(num)
print(sum)

'''

#largest from list
'''
num=[1,2,4,5,2,4,6,7]
print(max(num))
print(min(num))

'''

#counting number of elements
'''
list=[1,2,4,5,2,4,6,7]
print(list.count(4))

'''

#removing even numbers
num=[1,2,4,5,2,4,6,7]
oddnum=[x for x in num if x%2!=0]
print(oddnum)

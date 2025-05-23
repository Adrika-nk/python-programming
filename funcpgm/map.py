#map
'''def calculatesquare(n):
    return n*n
numbers=(1,2,3,4)
result=map(calculatesquare,numbers)
print(list(result))
'''

#how to use lambda function with map()
'''numbers=(1,2,3,4)
result=map(lambda n:n*n,numbers)
print(list(result))
'''
'''li=["adrika","sneha","dilshad"]
result=map (str.upper,li)
print(list(result))
'''

#passing multiple iterables to map() using lambda
'''num1=[1,2,3]
num2=[4,5,6]
result=map(lambda n1,n2:n1+n2,num1,num2)
print(list(result))

[5, 7, 9]
'''

#questions
'''def letters(a):
    
    result=map(lambda li1:li1[0],li1)
    print(list(result))

li1=["adrika","sneha","ayana","anagha"]
letters(li1)
'''

'''def celsius(a):

    result=map(lambda li1:li1 * 9/5 + 32,a)
    print(list(result))


li1=[32,40,35]
celsius(li1)
'''

'''def fact(n):
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto

li1=[3,4,5,6]
result=map(fact,li1)
print(list(result))
'''
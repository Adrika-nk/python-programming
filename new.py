"""a='this is python full stack this development,these are some questions to practice'
for i in a:
    b=a.count('this')
    c=a.count('these')
print('this',"=",b)
print('these',"=",c)
"""

#capitalize first and last letter of a string
"""a='my name is adrika'
sp=a.split()
print(sp)
result=''
for i in sp:
    if len(i)==1:
        z=i.upper()
        result=result+' '+a
    else:
        result=result+' '+i[0].upper()+i[1:-1]+i[-1].upper()
print(result)
    
"""

#mirror of a string
x=input("Enter a sentence")
a=x[::-1]
print(a)

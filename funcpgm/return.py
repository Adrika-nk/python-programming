'''def num_add(a,b):
    return a+b
a=int(input("Enter the number"))
b=int(input("Enter the number"))
s=num_add(a,b)
print(s)
print("Hello")
'''

'''def stsplit(s):
    a=s.split()
    return a
st='hello world'
print(stsplit(st))
'''
def num_add(a,b):
    d={}
    d['addition']=a+b
    d['subtraction']=a-b
    d['multiplication']=a*b
    d['division']=a/b
    return d

a=int(input("Enter first number"))
b=int(input("Enter second number"))
s=num_add(a,b)
print(s)


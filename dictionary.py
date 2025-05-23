#dictionary
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Name":"Adrika.N,K"}
print(dict1)
"""

#length
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
print(dict1["Place"])
"""

#dict constuctor
"""dict1=dict(name="Adrika",place="Kozhikode")
print(dict1)
"""

#type
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
print(type(dict1))
"""

#get
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
x=dict1.get("Place")
print(x)
"""

#dictkeys
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
x=dict1.keys()
print(x)
"""

#values

#items
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
x=dict1.items()
print(x)
"""

#membership operator
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
if "Place" in dict1:
    print("Yes")
"""

#to check values using membership
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack","Hobbies":["singing","reading"]}
if "Adrika" in dict1.values():
    print("Yes")
"""

#update value
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack"}
dict1.update({"Place":"idukki"})
print(dict1)
"""

"""a=int(input("Enter first number"))
b=int(input("Enter second number"))
dict1={}
dict1["Addition"]=a+b
dict1["Subtraction"]=a-b
dict1["Multiplication"]=a*b
dict1["Division"]=a/b
print(dict1)
"""

#pop
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack"}
dict1.pop("Place")
print(dict1)
"""

#pop item
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack"}
dict1.popitem()
print(dict1)
"""

#del
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack"}
del dict1["Name"]
print(dict1)
"""

"""d={}
a=int(input("Enter the number"))
for i in range(5,a+1):
    d[i]=i*2
print(d)

{5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22, 12: 24, 13: 26, 14: 28, 15: 30}
"""

#clear
"""dict1={"Name":"Adrika","Age":20,"Place":"Kozhikode","Course":"Python fullstack"}
dict1.clear()
print(dict1)
"""

#nested dictionary
"""sdict={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sdict["class"]["student"]["marks"]["history"])
"""

"""keys=['Ten','Twenty','Thirty']
values=[10,20,30]
dict1={}
for i in range(len(keys)):
    dict1[keys[i]]=values[i]
print(dict1)
"""

"""str1='python is an interpreted and dynamic programming language'
d={}
sp=str1.split()
for i in sp:
    if i[0] not in d:
        d[i[0]]=[]
        d[i[0]].append(i)
    else:
        d[i[0]].append(i)
print(d)
"""


"""num=input("Enter value")
n=len(num)
d=''
numval={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
pos={1:'ones',2:'tens',3:'hundreds',4:'thousands',5:'ten thousands',6:'lakhs'}
for i in num:
    x=int(i)
    d+=' '+numval[x]+' '+pos[n]
    n-=1
print(d)
"""

#contact book
print("1.Add a contact")
print("2.Display all contacts")
print("3.Search a contact")
print("4.Modify a contact")
print("5.Exit")
d={}
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter the name:")
        number=input("Enter the number")
        d[name]=number
        print("Contact added successfully")
    elif choice==2:
        print("Name\tPhone Number")
        for i in d:
            print(name+"    "+d[i])
    elif choice==3:
        search=input("Search the name:")
        if search in d:
            print(search+"    "+d[search])
        else:
            print("No contact found")
    elif choice==4:
        modify=input("Enter the name to modify")
        if modify in d:
            update=input("Enter new number")
            d[modify]=update
            print("Phone number modified")
            print(modify+"  "+d[modify])
        else:
            print("No such contact")
    elif choice==5:
        break
    
        

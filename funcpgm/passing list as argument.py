'''def my_function(food):
    print(fruits)
fruits=["apple","banana","kiwi"]
my_function(fruits)
'''

'''def even_odd(num):
    a=[]
    b=[]
    for i in num:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    print(a,b)

list1=[1,2,3,4,6,5,7,9]
even_odd(list1)
'''


'''def licreate(a):
    li=[]
    for i in range(a):
        b=input("Enter the element:")
        li.append(b)
    print(li)
x=int(input("how many elements you want to enter?"))
licreate(x)
'''


def reassign(li1):
    ind=int(input("Enter the index position you want to change"))
    value=int(input("Enter the value you want to reassign"))
    li1[ind]=value
    print(li1)

def insert(li1):
    ind=int(input("Enter the index position you want to insert"))
    value=int(input("Enter the value you want to insert"))
    li1.insert(ind,value)
    print(li1)

def delete(li1):
    ind=int(input("Enter the index position you want to delete"))
    del li1[ind]
    print(li1)

def sum(li1):
    su=0
    for i in li1:
        su=su+i
    print(su)

li=[1,2,3,4,5,6]
while True:
    choice=int(input("Enter the choice"))
    if choice==1:
        reassign(li)
    elif choice==2:
        insert(li)
    elif choice==3:
        delete(li)
    elif choice==4:
        sum(li)
    else:
        print("Enter valid choice!!")
#palindrome
'''x=input("Enter a string")
b=x.lower()
c=b.replace(' ','')
rev=b[::-1]
if b==rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
'''

#add new value to end
list1=[1,2,3,4,5,4,6,10,8]
choice=int(input("Enter your choice"))
new=[]
if choice==1:
    x=int(input("Enter the value to be added"))
    list1.append(x)
elif choice==2:
    x=int(input("Enter value to be inserted"))
    a=int(input("Enter the index position insert value"))
    list1.insert(a,x)
elif choice==3:
    for i in list1:
        if i%2==0:
            new.append(i)
    print(new)
elif choice==4:
    n=int(input("Enter the element to be deleted"))
    list1.remove(n)
    print(list1)
elif choice==5:
    list1.clear()
print(list1)




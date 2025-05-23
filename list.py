#string
'''student=['adrika',20,2005]
print(student)
'''

#position
'''student=['adrika',20,2005]
print(student[2])
'''

#replacing
'''student=['adrika',20,2005]
student[2]=1997
print(student)
'''

#type of string
'''student=['adrika',20,2005]
student[2]=1997
print(type(student))
print(student)
'''

#delete value
'''student=['adrika',20,2005]
student[2]=1997
del student[2]
print(student)
'''

#clear
'''student=['adrika',20,2005]
student.clear()
print(student)
'''

#length
'''student=['adrika',20,2005]
print(len(student))
'''

#concatenation
'''fam=['anil',60]
print([student]+[fam])
'''


#repetition print(student*3)

#membership in
'''if 'adrika' in student:
    print("yes")
else:
    print("no")
'''


#membership not in
'''if 'adrika' not in student:
    print("yes")
else:
    print("no")
'''
#for
'''for i in student:
    print(i)
'''

#while
'''student=['adrika',20,2005]
i=0
n=len(student)
while (i<n):
    print(student[i])
    i+=1
'''


#negative indexing
'''student=['adrika',20,2005]
print(student[-2])
'''

'''sub=int(input("Number of subjects:"))
sum=0
for i in range(sub):
    marks=int(input("Enter the mark:"))
    sum=sum+marks
print(sum)
avg=sum/sub
print(avg)

Number of subjects:5
Enter the mark:100
Enter the mark:95
Enter the mark:90
Enter the mark:80
Enter the mark:75
440
88.0
'''


#slicing
'''list=[10,20,30,40,50,60,70,80,90]'''
'''print(list[0:5])'''
'''print(list[0:5:2])'''
'''print(list[::-1])'''


#append
'''list1=[10,20,30,40,50,60,70,80,90]
list1.append(100);
print(list1)

'''

'''list1=[10,20,30,40,50,60,80,80,70,80,90]
print(list1.count(80))
'''


'''list1=[10,20,30,40,50,60,70,80,90]
print(min(list1))
print(max(list1))
'''

#min and max
'''list=['Adrika','ayana']
print(max(list))
print(min(list))
'''


#insert in element position
'''fruits=['apple','banana','orange']
fruits.insert(2,"watermelon")
print(fruits)
'''

#remove and pop
'''fruits=['apple','banana','orange','apple']
fruits.remove('apple')
print(fruits)

'''
'''fruits.pop(2)
print(fruits)
'''

'''fruits.remove("apple")
print(fruits)
'''

#sort
'''list=[2,4,3,8,6,0,1]
list.sort()
print(list)
'''

'''list=[2,4,3,8,6,0,1]
list.sort(reverse=True)
print(list)
'''

'''list=[2,4,3,8,6,0,1]
li1=sorted(list)
print(li1)
'''
#questions
#reverse of lis using for loop
'''list=[10,20,30,40]
for i in range(len(list)-1,-1,-1):
    print(list[i])
'''



#print even numbers in a list
'''list=[1,2,3,5,4,8,9,15,12,18,20,30]
for i in list:
    if i%2==0:
        print(i)
'''




#multiple of 5 and 3
'''list=[1,2,3,5,4,8,9,15,12,18,20,30]
for i in list:
    if i%3==0 and i%5==0:
        print(i)
'''



#create empty list and enter elements as user input
'''elist=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    values=int(input("Enter the element"))
    elist.append(values);
print(elist)
'''


#create list and 2 seperate list for odd and even numbers
'''li=[1,3,2,5,4,6,7,8,9]
lieven=[]
liodd=[]
for i in li:
    if i%2==0:
        lieven.append(i);
    if i%2!=0:
        liodd.append(i);
print(lieven,liodd)
'''



'''li=[]
num=int(input("Enter the values to be appended"))
for i in range(num):
    values=int(input("Enter the value:"))
    li.append(values);
print(li)
midval=int(input("enter the element that is needed to be added in the midpoint:"))
mid=num//2
li.insert(mid,midval)
print(li)
'''

list1=["M","na","i","Juli"]
list2=["y","me","s","us"]
listfin=[]
for i in range(i):
    listfin.append(list1,list2);
print(listfin)

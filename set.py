#set(unchangeable,unordered,unindexed)
"""name={"Adrika","Ayana","Dilshad","Sneha","Anakha","Dilshad","Saheer",1,True,False,0}
print(type(name))
"""

#set constructor
"""name={}
a=set()
print(type(a))
"""

#length
"""name={"Adrika","Ayana","Dilshad","Sneha","Anakha","Dilshad","Saheer"}
print(len(name))
"""

#printing elements one by one using loop
"""name={"Adrika","Ayana","Dilshad","Sneha","Anakha","Dilshad","Saheer"}
for i in name:
    print(i)
"""

#in operator
"""name={"Adrika","Ayana","Dilshad","Sneha","Anakha","Dilshad","Saheer"}
for i in name:
    if 'adrika' in name:
        print(i)
"""

#add
"""set={"apple","banana","cherry"}
set.add("orange")
print(set)
"""

#add sets
"""set1={"apple","mango","banana"}
set2={"pineapple","cherry","avocado"}
list1=["kiwi","grapes"]
set1.update(list1)
print(set1)
"""

#remove
"""set1={"apple","mango","banana"}
set1.remove("grapes")
print(set1)

KeyError: 'grapes'
"""


#discard
"""set1={"apple","mango","banana"}
set1.discard("grapes")
print(set1)
"""

#pop
"""set1={"apple","mango","banana"}
x=set1.pop()
print(x)
print(set1)
"""

#clear and delete
"""fruits={"apple","banana","orange"}
x=fruits.clear()
print(x)
"""

#union
"""set1={"a","b","c","d"}
set2={1,2,3,4}
set3=set1.union(set2)
print(set3)
"""

#update
"""set1={"a","b","c","d"}
set2={1,2,3,4}
set1.update(set2)
print(set1)
"""

#intersection update
"""x={"apple","mango","banana"}
y={"apple","cherry","avocado"}
x.intersection(y)
print(set1)
"""

#symmetric diiferenvce update
"""x={"apple","mango","banana"}
y={"apple","cherry","avocado"}
b=x.symmetric_difference(y)
print(b)
"""

#palindrome
"""x=input("Enter a string")
rev=x[::-1]
if x==rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
"""

#uppercase half length of a string
stringg="hello guys"
a=len(stringg)/2
print((a).upper())

#multi line strings
'''a=wskjwmdkielokod
jdwimskmijiwm
print(a)
'''

#index
"""a='''adrika
shhwhdhdhdhj'''
print(a[2])
"""

#loop
"""a='''adrika'''
for i in a:
    print(i)
"""

#length
"""a='''adrika@$#1 254'''
print(len(a))
"""

#check string
"""a='''adrika is a good girl'''
print("good" in a)
"""

#slicing
"""a="Hello world"
print(a[2:7])
"""

#uppercase
"""a="Hello world"
print(a.upper())
"""

#lowercase
"""a="Hello World"
print(a.lower())
"""

#strip
"""a="   Hello World   "
print(a.strip())
"""

#replace
"""a="Hai Hello World"
print(a.replace("H","i"))
"""

#split
"""a='''adrika is a good girl'''
sp=a.split()
print(sp)

['adrika', 'is', 'a', 'good', 'girl']
"""


#split character
"""a='''adr@ika is a go@od girl'''
sp=a.split('@')
print(sp)

['adr', 'ika is a go', 'od girl']
"""

#concatenation
"""a="Adrika"
b="Anil"
c=a+b
print(c)
"""

#formatting
"""name='adrika'
age=20
place='clt'
form='I am {},I am {} years old,from {}'
print(form.format(name,age,place))
print(f'i am {name},i am {age} years old,from{place}')
"""

#escape characters(illegal)
"""a="i am \"adrika\"."
print(a)
"""

#(illegal)
"""txt='It\'s alright'
print(txt)
"""
#\n
"""txt="Hello\nWorld"
print(txt)
"""

#\t
"""txt="Hello\tWorld"
print(txt)
"""

#\b
"""txt="Hello\bWorld"
print(txt)
"""

#capitalize(built in methods)
"""a="hello.welCome to my world."
x=a.capitalize()
print(x)
"""

#casefold
"""a="HELLO.welCome to my World."
x=a.casefold()
print(x)
"""

#center
"""a="Adrika"
x=a.center(20,'@')
print(x)
"""

#count
"""a="aaadrika"
x=a.count('a')
print(x)
"""

#endswith()
"""a="Hello,welcome to my world."
x=a.endswith(".")
print(x)
"""

#find()
"""a="Hello,welcome to my world."
x=a.find('j')
print(x)
"""

#index
"""a="Hello,welcome to my world."
x=a.index('e',5,13)
print(x)
"""

#isalnum
"""a='Abc123'
x=a.isalnum()
print(x)
"""

#isalpha
"""a='Abc'
x=a.isalpha()
print(x)
"""

#isdigit()
"""a='123'
x=a.isdigit()
print(x)
"""

#islower
"""a='abv'
x=a.islower()
print(x)
"""

#isupper
"""a='ABC'
x=a.isupper()
print(x)
"""

#title()
"""a="Hello,welCOME to my world.this is adrika"
x=a.title()
print(x)
"""

#swapcase
"""a="Hello,welCOME to my world.this is adrika"
x=a.swapcase()
print(x)
"""

#maketrans()
"""a="Sunday is a holiday"
mytrans=a.maketrans("S","P")
print(a.translate(mytrans))
"""

#join()
"""a=['i','am','learning','python']
b=' '.join(a)
print(b)
"""

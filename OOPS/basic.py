#create an object named p1,and print the value of x
'''class myname:
    x=5
    def greet():
    print("hello world")
    p1=myname()
print(p1.x)
greet()
'''

#self->current instance of a class and used to access variables that belongs to class
#self keyword is cahngeable but not recommendable

#python constructor
#it is a special function
#also called init
#automatically calls when an object is created


'''class myClass:
    def __init__(self):
        print("this is myClass")

    def hello(self):
        print("hello")
obj=myClass()
obj.hello()
'''

'''class myClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello(self):
        print("My name is "+self.name)
        print("My age is ",self.age)
p1=myClass("Adrika",20)
p2=myClass("Ayana",23)
p1.hello()
p2.hello()
'''

#INHERITANCE is the capablity of one class to derive or inherit the properties from another classes
#newly formed class is derived class/child
#base class is parent class

'''class Animal():
    def speak(Animal):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
d=Dog()
d.bark()
d.speak()
'''

'''class Arithmetic():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        print(self.num1-self.num2)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        print(self.num1/self.num2)
obj=Arithmetic(10,20)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
'''       

d=[{"name":"Adrika","score":90},
   {"name":"Ayana","score":80},
   {"name":"Sneha","score":65},
   {"name":"Anakha","score":60},
   {"name":"Saheer","score":95},
   {"name":"Dilshad","score":80},]

def score(d):
    return True if d("score")>70 else False
high_score=list(filter(lambda a:(a["name"] if a["score"]>70 else False),d))
new=list(high_score)
print(list(map(lambda b:b["name"],new)))
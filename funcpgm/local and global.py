total=10
def sum(a,b):
    total=a+b
    print("Inside the function local :",total)
    return total;
sum(10,20);
print(total)

#NameError: name 'total' is not defined
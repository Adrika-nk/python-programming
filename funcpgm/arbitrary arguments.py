def find_sum(*numbers):
    result=0
    for i in numbers:
        result=result+i
    
    return result
x=find_sum(1,2,3,89)
print(x)

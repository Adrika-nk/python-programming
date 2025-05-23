'''numbers=[x for x in range(10,1,-1)]
print(numbers)
'''

'''numbers=[1,2,3,4]
square=[]
for i in range(numbers):
    sq=(i*2 for i in numbers)
print(square)
'''


even_numbers=[num for num in range(1,10)if num%2==0]
for i in range(1,10):
    print(even_numbers)

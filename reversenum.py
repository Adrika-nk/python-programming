num=8426
sum=0
while num!=0:
    dig=num%10
    sum=sum+dig
    num//=10
print("The sum of digits is:",sum)

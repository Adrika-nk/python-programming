num=2552
#pal=2552
rev=0
a=0
while num!=0:
    dig=num%10
    rev=rev*10+dig
    num//=10
print("The reverse is:",rev)
print("num=:",num)
if num==rev:
    print("Palindrome")
else:
      print("Not Palindrome")

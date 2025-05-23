'''def greatest(li):
    li.sort()
    print(li)
    a=li[-2]
    print("The second largest is:",a)
    
li=[2,3,6,5,8,9]
greatest(li)
'''

'''def year(yr):
    if(y%4==0):
        print("It is a leap year")
    elif(y%100!=0) or (y%400==0):
        print("It is not a leap year")


y=int(input("Enter a year:"))
year(y)
'''

'''def vowels(s):
    st="aeiouAEIOU"
    d={}
    li1=s.split()
    print(li1)
    for i in li1:
        count=0
        for a in i:
            if a in st:
                count+=1
            d[i]=count
    print(d)
    
       

s="Adrika is a good girl"
vowels(s)
'''

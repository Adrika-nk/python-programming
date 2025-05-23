basicsalary=int(input("Enter the basic salary"))
if basicsalary<10000:
    da=basicsalary*25/100
    hra=basicsalary*30/100
    pf=basicsalary*8/100

elif basicsalary>=10000 and basicsalary<20000:
    da=basicsalary*20/100
    hra=basicsalary*25/100
    pf=basicsalary*6/100
    
elif basicsalary>=20000 and basicsalary<30000:
    da=basicsalary*15/100
    hra=basicsalary*20/100
    pf=basicsalary*4/100

else:
    da=basicsalary*10/100
    hra=basicsalary*15/100
    pf=basicsalary*2/100

netsalary=basicsalary+da+hra-pf
print("The net salary is",netsalary)

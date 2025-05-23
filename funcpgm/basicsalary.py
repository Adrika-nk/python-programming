#calculate the net salary of an employee

def basicsalary(b):
    da=b*5/100
    ta=b*3/100
    pf=b*2/100
    netsalary=b+da+ta-pf
    print("The net salary is",netsalary)


    
basic=int(input("Enter the basic salary"))
basicsalary(basic)

#net salary=basic salary+da+travelling allowance-pf

"""da=5% of basic salary
ta=3% of basic salary
pf=2% of basic salary"""

'''basicsalary=int(input("Enter the basic salary"))
da=basicsalary*5/100
ta=basicsalary*3/100
pf=basicsalary*2/100

netsalary=basicsalary+da+ta-pf
print("the net salary is",netsalary)


#basicsalaray below 10000, hra 4%
da 7%
pf 3%

bs bw 10000 and 50000
hra 2
da 5
pf 3

bs>50000
hra 3%
da 2%
pf 3%
'''

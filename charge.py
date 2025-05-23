unit=int(input("Enter the unit value"))
if unit>0 and unit<=100:
    charge=unit*.50

elif unit>=101 and unit<=200:
    charge=50+unit-100*1

elif unit>=201 and unit<=300:
    charge=150+unit-200*1.5

elif unit>300:
    charge=300+unit-300*2
print("the charge is:",charge)

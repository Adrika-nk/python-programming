a=float(input("Enter value for a:"))
b=float(input("Enter value for b:"))
c=float(input("Enter value for c:"))
discriminant=b**2-4*a*c
if discriminant>0:
    print("The roots is real")
else:
    print("The roots are imaginary")

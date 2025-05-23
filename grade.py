


#5 subjects average marks
a=float(input("Mark of Maths:"))
b=float(input("Mark of Science:"))
c=float(input("Mark of Economics:"))
d=float(input("Mark of Physics:"))

avg=(a+b+c+d)/4
if avg>=91 and avg<=100:
    print("Grade A+")
elif avg>=81 and avg<=90:
    print("Grade A")
elif avg>=71 and avg<=80:
    print("Grade B+")
elif avg>=61 and avg<=70:
    print("Grade C")
elif avg>=51 and avg<=60:
    print("Grade D")
else:
    print("You are failed")

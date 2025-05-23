def student(**stud):
    d={}
    for i in stud:
        d[i]=stud[i]
    print(d)
student(name="Adrika",age=20,course="Python",place="Kozhikode")
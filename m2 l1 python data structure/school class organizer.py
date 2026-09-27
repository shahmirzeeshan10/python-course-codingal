students=["shahmir","mustafa","ahmed","ibrahim"]
print("students in the class",students)
print("total students in the class",len(students))
print("first",students[0])
print("last", students[-1])
print("first 3:", students[:3])
students.append("saim")
students.remove("ibrahim")
students.sort()
print("updated:", students)

teacher={"name":"ms uzma","subject":"coding","experience":1}
print("Teacher:",teacher)
print("subject:",teacher["subject"])
teacher["experience"]=90000
print("updated teacher:", teacher)
rollnumbers=[1,2,3,4,5]
names=["shahmir","alizeh","sana","zeeshan","oreo"]
family=dict(zip(rollnumbers, names))
print(family[5])
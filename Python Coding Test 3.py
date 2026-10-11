students = {"PERCY" : 56, "ANNABETH" : 100, "JASON" : 98, "PIPER" : 82, "LEO" : 44, "FRANK" : 80, "HAZEL" : 96}

total = 0
for i in students.values():
    total += i

average = (total / len(students))
print(f"\nThe average mark of the class is: {average}")

top = max(students.values())
print("\nThe Highest Scorer is : ", end = " ")

for i, j in students.items():
    if j == top:
        print(i)

bottom = min(students.values())
print(f"The Lowest Scorer is : ", end = " ")

for i, j in students.items():
    if j == bottom:
        print(i)

name = input("\nEnter the name you are looking for:").strip().upper()

if name in students:
    print(f"\nThe student {name} is found:\nName : {name}\nMarks : {students[name]}")
else:
    print(f"\nThere is no student named as {name} in the system.\nKindly Check for Spelling Errors or Try Again!")
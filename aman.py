students_CGPA = {
    "A" : 5,
    "B" : 6,
    "C" : 7,
    "D" : 8,
    "E" : 9
}
v = students_CGPA.get("A")
for value in students_CGPA.values():
    if v < value:
        v = value
print("Highest cgpa is : " , v)

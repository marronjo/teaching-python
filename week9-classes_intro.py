#used to represent the square of a tic tac toe board
class square:                  
    def __init__(self, value):
        self.value = value

square1 = square("x")
print(square1.value)

class student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

first_student = student("Mark", 25, "Harvard")
print(first_student.name)
print(first_student.age)
print(first_student.school)

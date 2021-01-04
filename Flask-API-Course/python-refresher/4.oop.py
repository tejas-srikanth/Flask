class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades)/len(self.grades)

student1 = Student('Rolf', (95, 100, 92, 100, 100, 96))
print(student1.average())
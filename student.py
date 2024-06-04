from Person import Person

class Student(Person):
    def __init__(self,StudentId, GraduationDay, Specilization, NumberOfHours):
        self.StudemtId = StudentId
        self.specilization = Specilization
        self.NumberOfHours = NumberOfHours
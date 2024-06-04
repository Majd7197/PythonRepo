from Person import Person
#subclasses () put in () the name of the super CLASS!!!
class Guest(Person):
    def __init__(self,purpose):
        self.purpose = purpose
        
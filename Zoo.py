class Animal:
    def __init__(self,name,age,health_level ,happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    def display_info(self):
        print(f"The Animal name is {self.name},and the health level is {self.health_level} and happiness level is {self.happiness_level} ")
        return self
    def feed(self):
        self.health_level += 10
        self.happiness_level +=10  
        return self
class Lion(Animal):
    def __init__(self,type,name,age,health_level = 50 ,happiness_level = 50):
        self.type = type
        super().__init__(name,age,health_level ,happiness_level)
class Tiger(Animal):
    def __init__(self,size,name,age,health_level = 50 ,happiness_level = 50):
        self.size = size
        super().__init__(name,age,health_level ,happiness_level)
class Bear(Animal):
    def __init__(self,sound,name,age,health_level = 50 ,happiness_level = 50):
        self.sound = sound
        super().__init__(name,age,health_level ,happiness_level)
        
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(type = "african",name = name, age = 5) )
    def add_tiger(self, name):
        self.animals.append( Tiger(size = "large" , name=name, age = 5) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

zoo1.animals[0].feed()
print("\nAfter feeding Nala:")
zoo1.animals[0].display_info()


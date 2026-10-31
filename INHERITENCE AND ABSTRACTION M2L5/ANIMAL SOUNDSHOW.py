from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat
    def display(self):
        print(f"name:{self.name} , habitat:{self.habitat}")
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self, name, habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed
    def speak(self):
        print(f"{self.name}  {self.breed} say:woof! woof!")

class lion(Animal): 
    def __init__(self,name,habitat,pride):
        super().__init__(name,habitat)
        self.pride=pride
    def speak(self):
        print(f"{self.name} {self.pride} says roar!roar!")
d=Dog("Bruno","Antartica","shitzu")
lion=lion("Simba","savannah","pride rock")
print("animal soundshow")
for i in [d,lion]:
    i.display()
    i.speak()
    print()

    
class Animal:
    def speak(self):
        print("Animal speaks")

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Dog(Animal, Vehicle): 
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.move()
dog.bark()


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Employee(Person):
    def __init__(self, name, id, salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post

    def display(self):
        print(f"Employee details are: \nName: {self.name}, \nID: {self.id}, \nSalary: {self.salary}, \nPost: {self.post}")


p = Employee("Riya", 989, 50000, "Tester")
p.display()

'''
Побудувати іерархію класів для співробітників
'''

class Cat:
    def __init__(self) -> None:
        self.legs = ["right", "left", "back right", "back left"]

class SiameseCat(Cat):
    def __init__(self) -> None:
        super().__init__()

class Person:
    def __init__(self, name = "Person") -> None:
        if len(name) == 0:
            # raise ValueError
            name = "Person"
        self.name = name

    def say_hello(self):
        print("Hello!")

    def say_name(self):
        print(self.name)


class Employee(Person):
    def __init__(self, salary) -> None:
        super().__init__(name)

        # self.name = name

    def say_super_hello(self):
        super().say_hello()

employee = Employee("Igor", 1000)
employee.say_name()

Person("Igor")
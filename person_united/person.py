# from person.salary import 
# from .salary import Salary
from salary import Salary


class Person:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = Salary(salary)

try:
    person_one = Person("Igor", 4000)
    print(dir(person_one))
    person_one.salary.salary -= 5000
    print(person_one.salary)
except ValueError:
    print("Value should not be less than 0")
# print(person_one.salary.multiply_salary_by_two())
# person_one.salary.salary -= 5000
# print(person_one.salary)

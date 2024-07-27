
class Salary:
    def __init__(self, salary):
        self.salary = salary

    def multiply_salary_by_two(self):
        return self.salary * 2
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Salary):
            return self.salary == other.salary
        # elif isinstance(other, int):
        #     return self.salary == other
        return False

salary_one = Salary(1000)
print(dir(salary_one))
print(salary_one.salary)

# salary_two = Salary(2000)

# print(dir(salary_one))
# print(salary_two)
# print(salary_one == salary_two)

# print(salary_one == 1000)

# print(isinstance("Hello", str))

# print(salary_one.multiply_salary_by_two())

# print(dir("Hello!"))
# print("Hello" + " world")
# print(dir(salary_one))

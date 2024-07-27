

class Salary:
    def __init__(self, salary):
        self.salary = salary

    def multiply_salary_by_two(self):
        return self.salary * 2
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Salary):
            return self.salary == other.salary
        return False
    
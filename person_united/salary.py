
''' Доповнити клас Salary, щоб була можливість посортувати обʼєкти цього класу'''
class Salary:
    def __init__(self, salary):
        if salary < 0:
            raise ValueError
        self.salary = salary

    def multiply_salary_by_two(self):
        return self.salary * 2
    
    # ==
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Salary):
            return self.salary == other.salary
        return False
    
    # <
    def __lt__(self, other) -> bool:
        if isinstance(other, Salary):
            return self.salary < other.salary
        return False
    
    def __sub__(self, other):
        return Salary(self.salary - other.salary)
    
    def __str__(self):
        return f'Salary amount is {self.salary}'
    
    def __repr__(self) -> str:
        return f'Salary({self.salary})'



if __name__ == '__main__':
    # numbers_list = [5, 4, 3, 2, 1] # [1, 2, 3, 4, 5]
    # numbers_list.sort()
    # print(numbers_list)

    # numbers_list_two = [5, 4, 3, 2, 1]
    # print(sorted(numbers_list_two))
    # print(numbers_list_two)

    salary_one = Salary(5000)
    print(salary_one)

    salary_two = Salary(4000)
    [salary_one, salary_two]

    salary_list = [Salary(5000), Salary(4000), Salary(3000), Salary(2000), Salary(1000)]
    # print(salary_list)
    # print(sorted(salary_list))
    # print(sorted(salary_list))

    # salary_list.
    # str_list = ["Hello", "world", "one", "two"]
    # print(str_list.index("world"))
    # print(salary_list.index(Salary(4000)))

    # def check(salary)

    '''
    Знайти усі заробітні плати, в яких значення буде більше або дорівнює 3000
    '''
    print(list(filter(lambda salary_object: salary_object == Salary(3000), salary_list)))

    print(Salary(5000) - Salary(3000)) # Salary(2000)


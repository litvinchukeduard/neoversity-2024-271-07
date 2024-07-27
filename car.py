
class Car:
    number_of_wheels = 4

    def __init__(self, number_of_doors):
        var = "Hello"
        self.number_of_doors = number_of_doors

car_zero = Car(1)
print(car_zero.number_of_wheels)

# print(Car.number_of_wheels)
Car.number_of_wheels += 1

# car_one = Car(4)
# print(car_one.number_of_wheels)

# car_two = Car(4)
# # car_two.number_of_doors -= 1
# print(car_two.number_of_wheels)

# print(car_one.number_of_doors)

print(car_zero.number_of_wheels)

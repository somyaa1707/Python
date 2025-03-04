#Merge Two Lists into a Dictionary (using a Lambda Function)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
merge_lists = lambda keys, values: dict(zip(keys, values))
result = merge_lists(keys, values)
print(result)  

#Create a Product Class with Instance and Class Variables, and a Method to Calculate Discounted Price
class Product:
    discount_rate = 0.1  
    def __init__(self, name, price):
        self.name = name  
        self.price = price  
    def calculate_discounted_price(self):
        return self.price * (1 - Product.discount_rate)
product = Product("Laptop", 1000)
print(product.calculate_discounted_price()) 

#Create a Base Class Shape and Derived Classes Circle and Rectangle (Inheritance)
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  
print(rectangle.area())  

#Multiple Inheritance: Create Person and Employee Base Classes, and a Manager Class that Inherits from Both
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}"
class Employee:
    def __init__(self, job_title):
        self.job_title = job_title
    def get_job_title(self):
        return f"I am a {self.job_title}"
class Manager(Person, Employee):
    def __init__(self, name, job_title, department):
        Person.__init__(self, name)
        Employee.__init__(self, job_title)
        self.department = department
    def get_department(self):
        return f"I manage the {self.department} department."
manager = Manager("Alice", "Manager", "Sales")
print(manager.greet())  
print(manager.get_job_title())  
print(manager.get_department())  

# Implement Polymorphism with Different Animal Classes (Dynamic Method Calling)
class Dog:
    def make_sound(self):
        return "Woof!"
class Cat:
    def make_sound(self):
        return "Meow!"
class Cow:
    def make_sound(self):
        return "Moo!"
def play_sound(animal):
    print(animal.make_sound())
dog = Dog()
cat = Cat()
cow = Cow()
play_sound(dog)  
play_sound(cat)  
play_sound(cow)  

#Design a Car Rental System with Classes Vehicle, Car, and Bike Using OOP
class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
    def rental_cost(self, days):
        return self.rental_rate * days
class Car(Vehicle):
    def __init__(self, brand, model, rental_rate, num_doors):
        super().__init__(brand, model, rental_rate)
        self.num_doors = num_doors
    def car_details(self):
        return f"Car: {self.brand} {self.model}, {self.num_doors} doors"
class Bike(Vehicle):
    def __init__(self, brand, model, rental_rate, type_of_bike):
        super().__init__(brand, model, rental_rate)
        self.type_of_bike = type_of_bike
    def bike_details(self):
        return f"Bike: {self.brand} {self.model}, Type: {self.type_of_bike}"
car = Car("Toyota", "Camry", 50, 4)
bike = Bike("Yamaha", "MT-07", 20, "Sport")
print(car.car_details())  
print(bike.bike_details())  
print(f"Car rental cost for 3 days: ${car.rental_cost(3)}")  
print(f"Bike rental cost for 2 days: ${bike.rental_cost(2)}")  


# Level 1: Basic Polymorphism Beginner 
# Q1. Animal Sound (Method Overriding) Create a parent class Animal with a method sound(). 
# Create child classes Dog, Cat, and Cow that override the sound() method. 
# Expected output: Dog barks Cat meows Cow moos 
class animal:
    def sound(self):
        print("Animal Sound")
class Dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("Cat meows")
class cow(animal):
    def sound(self):
        print("Cow moos")
a=Dog()
b=cat()
c=cow()

a.sound()
b.sound()
c.sound()

# Q2. Payment System Create a parent class Payment with a method pay(). 
# Create child classes UPI, CreditCard, and Cash. Each class should implement its own pay() method. 
# Expected output: Payment through UPI Payment through Credit Card Payment through Cash 
class Payment():
    def pay(self):
        print("Payment Process")
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit")
class Cash(Payment):
    def pay(self):
        print("Card Payment through Cash")


a=UPI()
b=CreditCard()
c=Cash()

a.pay()
b.pay()
c.pay()

# Q3. Employee Salary Create a parent class Employee with a method calculate_salary(). 
# Create child classes FullTimeEmployee and PartTimeEmployee. 
# • Full-time salary = monthly salary • Part-time salary = working hours × hourly rate Display the salary for each employee. 
class Employee:
    def calculate_salary(self):
        print("Calculated Salary")
class FullTimeEmployee(Employee):
    def calculate_salary(self,salary):
        self.salary=salary
        print("Monthly Salary is:",self.salary)
class PartTimeEmployee(Employee):
    def calculate_salary(self,hours,amount):
        self.hours=hours
        self.amount=amount
        print("Total Amount:",self.hours * self.amount)

a=FullTimeEmployee()
b=PartTimeEmployee()

a.calculate_salary(30000)
b.calculate_salary(6,100)

# Q4. Shape Area Create a parent class Shape with an area() method. 
# Create child classes Circle, Rectangle, and Square. 
# Calculate and display the area of each shape using method overriding. 
class Shape:
    def area(self):
        print("Calculating Area")
class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        print("Area of Circle:",3.14*self.radius*self.radius)
class Rectangle(Shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("Area of Rectangle:",self.length * self.breadth)
class Square(Shape):
    def area(self,side):
        self.side=side
        print("Area of Square:",self.side*self.side)

circle = Circle()
rectangle = Rectangle()
square = Square()

circle.area(4)
rectangle.area(2,3)
square.area(6)

# Q5. Vehicle Information Create a parent class Vehicle with a method start(). 
# Create child classes Car, Bike, and Bus, each with a different implementation of start(). 
# Use a loop to call the method for all objects. 
class Vehicle:
    def start(self):
        print("start....")
class Car(Vehicle):
    def start(self):
        print("Caring started")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
class Bus(Vehicle):
    def start(self):
        print("Bus started")

#mor--list
list=[Vehicle(),Car(),Bike(),Bus()]
for i in list:
    i.start()

# Level 2: Intermediate Polymorphism Intermediate 
# Q6. Method Overloading Using Default Arguments Create a class Calculator with a method add() that accepts two or three numbers and returns their sum. 
# Expected output: 15 30 60 
class Calculator:
    def add(self,a,b,c=0):
        print("Sum of two Numbers:",a+b)
    def add(self,a,b,c):
        print("Sum of three Numbers:",a+b+c)
a=Calculator()
a.add(15,30,60)
# a.add(10,20)--> error bcz second method overload 1st method

# Q7. Duck Typing – Notification System Create three unrelated classes: 
# EmailNotification, SMSNotification, and WhatsAppNotification. Each class should have a send() method. 
# Create a function notify_user() that accepts any object and calls its send() method. 
class notification:
    def send(self):
        print("New Notification")
class Email(notification):
    def send(self):
        print("Email Message...")
class Whatsapp(notification):
    def send(self):
        print("Whatsapp Message...")
class SMS(notification):
    def send(self):
        print("Message...")

#mor--duck type
def send_notification(abc):
    abc.send()
N=notification()
a=Email()
b=Whatsapp()
c=SMS()
send_notification(N)
send_notification(a)
send_notification(b)
send_notification(c)

# Q8. Banking System Create a parent class Bank with a method interest_rate(). 
# Create child classes SBI, HDFC, and ICICI, each returning a different interest rate. 
# Display the interest rate using a common function. 
class Bank:
    def interest_rate(self):
        print("Interest Rate")
class SBI(Bank):
    def interest_rate(self):
        print("SBI Interest Rate: 7%")
class HDFC(Bank):
    def interest_rate(self):
        print("HDFC Interest Rate: 7.5%")
class ICICI(Bank):
    def interest_rate(self):
        print("ICICI Interest Rate: 7.25%")

def display_rate(bank):
    bank.interest_rate()

sbi = SBI()
hdfc = HDFC()
icici = ICICI()

display_rate(sbi)
display_rate(hdfc)
display_rate(icici)

# Q9. Polymorphism with Built-in Functions Create a list, tuple, string, and dictionary.
#  Use the same built-in functions len() and type() on all four objects. 
# Explain how the same function works with different object types. 

my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30)
my_string = "Python"
my_dict = {"name": "Raju", "age": 20}

print("List:")
print(len(my_list))
print(type(my_list))

print("\nTuple:")
print(len(my_tuple))
print(type(my_tuple))

print("\nString:")
print(len(my_string))
print(type(my_string))

print("\nDictionary:")
print(len(my_dict))
print(type(my_dict))

# Q10. Food Ordering System Create a parent class Food with a method prepare(). 
# Create child classes Pizza, Burger, and Biryani. Each class should provide its own preparation process. 
# Call prepare() using a common function that accepts different food objects. 
class Food:
    def prepare(self):
        print("Preparing food")
class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza: Add toppings and bake")
class Burger(Food):
    def prepare(self):
        print("Preparing Burger: Add patty and vegetables")
class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani: Cook rice with spices and chicken")
def prepare_food(food):
    food.prepare()

f=Food()
pi = Pizza()
bu = Burger()
bi = Biryani()

prepare_food(f)
prepare_food(pi)
prepare_food(bu)
prepare_food(bi)


# Level 3: Advanced Problem-Solving
# Advanced
# Q11. Operator Overloading – Addition
# Create a class Book with attributes pages. Overload the + operator using __add__() to add the 
# pages of two books.
# Expected output:
# Book 1 pages: 150
# Book 2 pages: 200
# Total pages: 350
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(150)
book2 = Book(200)

print("Book 1 pages:", book1.pages)
print("Book 2 pages:", book2.pages)
print("Total pages:", book1 + book2)
# Q12. Operator Overloading – Comparison
# Create a class Product with an attribute price. Overload the > operator using __gt__() to 
# compare the prices of two products.
# Display which product has the higher price.
class Product:
    def __init__(self, price):
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

product1 = Product(500)
product2 = Product(800)

if product1 > product2:
    print("Product 1 has higher price")
else:
    print("Product 2 has higher price")

# Q13. Duck Typing – Media Player
# Create three classes: Audio, Video, and Podcast. Each class should have a play() method.
# Create a function play_media() that accepts any object and calls its play() method without 
# checking its class.
class Audio:
    def play(self):
        print("Playing audio")
class Video:
    def play(self):
        print("Playing video")
class Podcast:
    def play(self):
        print("Playing podcast")

def play_media(media):
    media.play()

play_media(Audio())
play_media(Video())
play_media(Podcast())

# Q14. Polymorphism with Class Methods
# Create a parent class Employee with a class method company_info(). Create child classes 
# Developer and DataAnalyst that override the class method.
# Call the method using both child classes and explain the output.
class Employee:
    def company_info():
        print("Employee works in the company")


class Developer(Employee):
    def company_info():
        print("Developer works in the company")


class DataAnalyst(Employee):
    def company_info():
        print("Data Analyst works in the company")


Developer.company_info()
DataAnalyst.company_info()
# Q15. Shopping Cart
# Create classes Electronics, Clothing, and Grocery. Each class should have a method 
# calculate_discount() with a different discount calculation.
# Create a common function to calculate and display the final price for different products.
class Electronics:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 10 / 100


class Clothing:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 20 / 100


class Grocery:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 5 / 100


def calculate_final_price(product):
    discount = product.calculate_discount()
    final_price = product.price - discount
    print("Final price:", final_price)


calculate_final_price(Electronics(1000))
calculate_final_price(Clothing(1000))
calculate_final_price(Grocery(1000))

# Interview Practice
# Q16. Ride Booking Application
# Create a parent class Ride with a method calculate_fare(). Create child classes BikeRide, 
# CarRide, and AutoRide.
# Each ride should calculate its fare based on distance and its own rate per kilometer. Display the 
# fare using a common function.
class Ride:
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        pass


class BikeRide(Ride):
    def calculate_fare(self):
        return self.distance * 10


class CarRide(Ride):
    def calculate_fare(self):
        return self.distance * 20


class AutoRide(Ride):
    def calculate_fare(self):
        return self.distance * 15


def display_fare(ride):
    fare = ride.calculate_fare()
    print("Fare:", fare)


display_fare(BikeRide(10))
display_fare(CarRide(10))
display_fare(AutoRide(10))

# Q17. Hospital Management System
# Create a parent class Doctor with a method treat_patient(). Create child classes Cardiologist, 
# Dentist, and Neurologist.
# Each doctor should provide a different treatment description. Use polymorphism to call the 
# methods.
class Doctor:
    def treat_patient(self):
        pass


class Cardiologist(Doctor):
    def treat_patient(self):
        print("Treating heart problems")


class Dentist(Doctor):
    def treat_patient(self):
        print("Treating dental problems")


class Neurologist(Doctor):
    def treat_patient(self):
        print("Treating nervous system problems")


def treat(doctor):
    doctor.treat_patient()


treat(Cardiologist())
treat(Dentist())
treat(Neurologist())
# Q18. File Processing System
# Create classes CSVFile, JSONFile, and TextFile. Each class should have a read_file() method.
# Create a common function process_file() that accepts different file objects and calls the 
# appropriate method.
class Doctor:
        def treat_patient(self):
            pass
class Cardiologist(Doctor):
    def treat_patient(self):
        print("Treating heart problems")

class Dentist(Doctor):
    def treat_patient(self):
        print("Treating dental problems")

class Neurologist(Doctor):
    def treat_patient(self):
        print("Treating nervous system problems")

def treat(doctor):
    doctor.treat_patient()

treat(Cardiologist())
treat(Dentist())
treat(Neurologist())
# Q19. Custom Data Types
# Create a class Distance with attributes km and meters. Overload the + operator to add two 
# distance objects and return the total distance in normalized kilometers and meters.
# Example:
# Distance 1: 2 km 500 meters
# Distance 2: 3 km 800 meters
# Total: 6 km 300 meters
class Distance:
    def __init__(self,km,meters):
        self.km=km
        self.meters=meters
    def __add__(self,other):
        total_km = self.km + other.km
        total_meters = self.meters + other.meters

        if total_meters >= 1000:
            total_km += total_meters // 1000
            total_meters = total_meters % 1000

        return Distance(total_km, total_meters)
distance1 = Distance(2, 500)
distance2 = Distance(3, 800)

total = distance1 + distance2

print("Total:", total.km, "km", total.meters, "meters")
# Q20. Complete Polymorphism Challenge
# Create a class Employee and child classes Manager, Developer, and Tester.
# Each employee should have:
# • A work() method with a different implementation.
# • A calculate_bonus() method with a different implementation.
# • A display_details() method to display employee information.Store all employee objects in a list and use a loop to call the methods without checking the 
# object type.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        pass

    def calculate_bonus(self):
        pass

    def display_details(self):
        pass


class Manager(Employee):
    def work(self):
        print("Manager manages the team")

    def calculate_bonus(self):
        return self.salary * 20 / 100

    def display_details(self):
        print("Name:", self.name)
        print("Role: Manager")


class Developer(Employee):
    def work(self):
        print("Developer writes code")

    def calculate_bonus(self):
        return self.salary * 15 / 100

    def display_details(self):
        print("Name:", self.name)
        print("Role: Developer")


class Tester(Employee):
    def work(self):
        print("Tester tests the application")

    def calculate_bonus(self):
        return self.salary * 10 / 100

    def display_details(self):
        print("Name:", self.name)
        print("Role: Tester")


employees = [
    Manager("Ravi", 50000),
    Developer("Anu", 40000),
    Tester("Kiran", 30000)
]

for employee in employees:
    employee.display_details()
    employee.work()
    print("Bonus:", employee.calculate_bonus())

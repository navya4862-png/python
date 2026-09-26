# single Inheritance 1. 
# Create a Person class with name and age. 
# Create a Student class that inherits from Person and adds course. 
# Display all details.  

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = Student("Navya", 22, "Python")

student1.display()

# 2. Create an Employee class with name, salary, and department. 
# Create a Manager class that inherits from Employee and adds team_size.  
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Team Size:", self.team_size)

manager1 = Manager("Navya", 50000, "IT", 10)

manager1.display()

# 3. Create a Vehicle class with brand and model. 
# Create a Car class that inherits from Vehicle and adds fuel_type.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)

car1 = Car("Toyota", "Fortuner", "Diesel")

car1.display()

# 4. Create a BankAccount class with account_number and balance. 
# Create a SavingsAccount class that inherits from it and adds interest_rate.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")

account1 = SavingsAccount(123456, 50000, 6.5)

account1.display()  

# 5. Create a Product class with product_name and price. 
# Create an ElectronicProduct class that inherits from it and adds warranty_years.  
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_name, price, warranty_years):
        super().__init__(product_name, price)
        self.warranty_years = warranty_years

    def display(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Warranty:", self.warranty_years, "years")

product1 = ElectronicProduct("Laptop", 50000, 2)

product1.display()

# 6. Create an Animal class with name and age. 
# Create a Dog class that inherits from it and adds breed. 
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Breed:", self.breed)

dog1 = Dog("Tommy", 3, "Labrador")

dog1.display()

# Constructor + super() 7. Create a Person class with a constructor accepting name and age. 
# Create a Student class with course and marks. Use super().  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)

student1 = Student("Navya", 22, "Python", 85)

student1.display()

# 8. Create an Employee class with name and salary. 
# Create a Developer class with language and experience. Initialize all values using super().  
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, language, experience):
        super().__init__(name, salary)
        self.language = language
        self.experience = experience

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Experience:", self.experience, "years")

developer1 = Developer("Navya", 40000, "Python", 1)

developer1.display()

# 9. Create a Vehicle class with brand and model. 
# Create a Car class with fuel_type and price. Use super() to initialize parent attributes. 
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)


car1 = Car("Toyota", "Fortuner", "Diesel", 4000000)

car1.display()

# 10. Create a BankAccount class with holder_name and balance. 
# Create a SavingsAccount class with interest_rate. Calculate the final balance.  
class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_final_balance(self):
        interest = self.balance * self.interest_rate / 100
        final_balance = self.balance + interest

        print("Holder Name:", self.holder_name)
        print("Initial Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", interest)
        print("Final Balance:", final_balance)

account1 = SavingsAccount("Navya", 50000, 6)

account1.calculate_final_balance()

# 11. Create a Company class with company_name. 
# Create an Employee class with employee_name and salary. Use super().  
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

class Employee(Company):
    def __init__(self, company_name, employee_name, salary):
        super().__init__(company_name)
        self.employee_name = employee_name
        self.salary = salary

    def display(self):
        print("Company Name:", self.company_name)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)

employee1 = Employee("TCS", "Navya", 40000)

employee1.display()

# 12.Create the following:

# Person -> Employee -> Manager
# Store appropriate information in each class and display all details.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Employee:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    def show(self):
        print("Emp_id:",self.id)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,age,id,salary,department):
        super().__init__(name,age,id,salary)
        self.department=department
    def details(self):
        print("emp_dep:",self.department)

e1=Manager("Navya",22,101,30000,"IT")
e1.display()
e1.show()
e1.details()

# 13
class vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
class car(vehical):
    def __init__(self,brand,model,fuel_type,price):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
        self.price=price
    def display_car(self):
        print("Fuel_type:",self.fuel_type)
        print("Price:",self.price)
class ElectricCar(car):
    def __init__(self,brand,model,fuel_type,price,battery_capacity,range):
        super().__init__(brand,model,fuel_type,price)
        self.battery_capacity=battery_capacity
        self.range=range
    def display_ElectricCar(self):
        print("Battery Capacity:",self.battery_capacity ,"KWH\h")
        print("Range:",self.range,"Km")

car1=ElectricCar("Tata","Nexon","Electric",1500000,40,32)
car1.display()
car1.display_car()
car1.display_ElectricCar()

# 14
class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class GraduateStudent(students):
    def __init__(self,name,age,course, college):
        super().__init__(name,age)
        self.course=course
        self.college=college
    def display_GraduateStudent(self):
        print("Course:",self.course)
        print("College:",self.college)
class ResearchStudent(GraduateStudent):
    def __init__(self,name,age,course,college,research_topic,guide_name):
        super().__init__(name,age,course,college)
        self.research_topic=research_topic
        self.guide_name=guide_name
    def display_ResearchStudent(self):
        print("Research Topic:",self.research_topic)
        print("Guide Name:",self.guide_name)

s1=ResearchStudent("Navya",22,"B.Tech","ABC Clg","AI","Dr.Rao")
s1.display()
s1.display_GraduateStudent()
s1.display_ResearchStudent()

# 15
class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name of Animal:",self.name)
        print("Age of animal:",self.age)

class Mammal(Animal):
    def __init__(self,name,age,fur_color):
        super().__init__(name,age)
        self.fur_color=fur_color
    def display_Mammal(self):
        print("Fur Color id:",self.fur_color)

class Dog(Mammal):
    def __init__(self,name,age,fur_color,breed):
        super().__init__(name,age,fur_color)
        self.breed=breed
    def display_Dog(self):
        print("Breed:",self.breed)

d1 = Dog("Bruno", 3, "Brown", "Labrador")

d1.display()
d1.display_Mammal()
d1.display_Dog()

# Multiple Inheritance 
# 16. Create Father and Mother classes with different properties. 
# Create a Child class that inherits from both.  
class Father:
    def __init__(self, father_name, father_job):
        self.father_name = father_name
        self.father_job = father_job

    def display_father(self):
        print("Father Name:", self.father_name)
        print("Father Job:", self.father_job)


class Mother:
    def __init__(self, mother_name, mother_job):
        self.mother_name = mother_name
        self.mother_job = mother_job

    def display_mother(self):
        print("Mother Name:", self.mother_name)
        print("Mother Job:", self.mother_job)


class Child(Father, Mother):
    def __init__(self, father_name, father_job, mother_name, mother_job,
                 child_name, age):

        Father.__init__(self, father_name, father_job)
        Mother.__init__(self, mother_name, mother_job)

        self.child_name = child_name
        self.age = age

    def display_child(self):
        print("Child Name:", self.child_name)
        print("Child Age:", self.age)


c1 = Child("Ramesh", "Engineer", "Sita", "Teacher", "Kaju", 22)

c1.display_father()
c1.display_mother()
c1.display_child()
       
# 17. Create Printer and Scanner classes. 
# Create a Machine class that inherits from both.  

class Printer:
    def __init__(self, printer_type, print_speed):
        self.printer_type = printer_type
        self.print_speed = print_speed

    def print_document(self):
        print("Printer Type:", self.printer_type)
        print("Print Speed:", self.print_speed, "pages/min")


class Scanner:
    def __init__(self, scanner_type, scan_resolution):
        self.scanner_type = scanner_type
        self.scan_resolution = scan_resolution

    def scan_document(self):
        print("Scanner Type:", self.scanner_type)
        print("Scan Resolution:", self.scan_resolution, "DPI")


class Machine(Printer, Scanner):
    def __init__(self, printer_type, print_speed, scanner_type,
                 scan_resolution, machine_name):

        super().__init__(printer_type, print_speed)
        Scanner.__init__(self, scanner_type, scan_resolution)

        self.machine_name = machine_name

    def display_machine(self):
        print("Machine Name:", self.machine_name)


m1 = Machine("Laser", 30, "Flatbed", 1200, "HP All-in-One")

m1.print_document()
m1.scan_document()
m1.display_machine()
# 18. Create Teacher and Researcher classes. 
# Create a Professor class that inherits from both.  
class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display_teacher(self):
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)


class Researcher:
    def __init__(self, research_area, research_paper):
        self.research_area = research_area
        self.research_paper = research_paper

    def display_researcher(self):
        print("Research Area:", self.research_area)
        print("Research Paper:", self.research_paper)


class Professor(Teacher, Researcher):
    def __init__(self, teacher_name, subject, research_area,
                 research_paper, experience):

        Teacher.__init__(self, teacher_name, subject)
        Researcher.__init__(self, research_area, research_paper)

        self.experience = experience

    def display_professor(self):
        print("Experience:", self.experience)


p1 = Professor("Dr. Ravi", "Python", "AI", "Machine Learning", 10)

p1.display_teacher()
p1.display_researcher()
p1.display_professor()

# 19. Create Developer and Designer classes. 
# Creatclass Developer:
class Developer:
    def __init__(self, developer_name, language):
        self.developer_name = developer_name
        self.language = language

    def display_developer(self):
        print("Developer Name:", self.developer_name)
        print("Language:", self.language)


class Designer:
    def __init__(self, design_tool, design_type):
        self.design_tool = design_tool
        self.design_type = design_type

    def display_designer(self):
        print("Design Tool:", self.design_tool)
        print("Design Type:", self.design_type)


class UIDeveloper(Developer, Designer):
    def __init__(self, developer_name, language, design_tool,
                 design_type, project_name):

        Developer.__init__(self, developer_name, language)
        Designer.__init__(self, design_tool, design_type)

        self.project_name = project_name

    def display_ui_developer(self):
        print("Project Name:", self.project_name)


u1 = UIDeveloper("Navya", "Python", "Figma", "UI Design", "Food App")

u1.display_developer()
u1.display_designer()
u1.display_ui_developer()

# Hierarchical Inheritance 
# 20. Create an Employee parent class and two child classes Developer and Tester. 
# Add different properties to each child.  
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        print("Developer:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)


class Tester(Employee):
    def __init__(self, name, salary, testing_tool):
        super().__init__(name, salary)
        self.testing_tool = testing_tool

    def display(self):
        print("Tester:", self.name)
        print("Salary:", self.salary)
        print("Testing Tool:", self.testing_tool)


d1 = Developer("Navya", 40000, "Python")
t1 = Tester("Ravi", 35000, "SQL")

d1.display()
t1.display()

## 21. Create an Animal parent class and child classes Dog, Cat, and Cow. 
## Add different attributes and methods to each child.  
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(self.name, "is barking")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(self.name, "is meowing")


class Cow(Animal):
    def __init__(self, name, age, milk):
        super().__init__(name, age)
        self.milk = milk

    def give_milk(self):
        print(self.name, "gives", self.milk, "litres of milk")


d1 = Dog("Bruno", 3, "Labrador")
c1 = Cat("Kitty", 2, "White")
cw1 = Cow("Ganga", 5, 10)

d1.bark()
c1.meow()
cw1.give_milk()

## 22. Create a Vehicle parent class and child classes Car, Bike, and Bus. Display their specific information. 
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def display(self):
        print(self.brand, "is a Car")


class Bike(Vehicle):
    def display(self):
        print(self.brand, "is a Bike")


class Bus(Vehicle):
    def display(self):
        print(self.brand, "is a Bus")


c1 = Car("Tata")
b1 = Bike("Honda")
bus1 = Bus("Metru Bus")

c1.display()
b1.display()
bus1.display() 

# 23. Create this structure:  
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)
        self.language = language


class Tester(Employee):
    def __init__(self, name, salary, tool):
        Employee.__init__(self, name, salary)
        self.tool = tool


class TeamLead(Developer, Tester):
    def __init__(self, name, salary, language, tool, team_size):
        Developer.__init__(self, name, salary, language)
        Tester.__init__(self, name, salary, tool)
        self.team_size = team_size

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Testing Tool:", self.tool)
        print("Team Size:", self.team_size)


t1 = TeamLead("Navya", 50000, "Python", "API Tester", 5)

t1.display()

#24
class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_device(self):
        print("Brand:", self.brand)


class Phone(Device):
    def __init__(self, brand, phone_number):
        Device.__init__(self, brand)
        self.phone_number = phone_number

    def call(self):
        print("Phone Number:", self.phone_number)
        print("Calling...")


class Camera(Device):
    def __init__(self, brand, camera_type):
        Device.__init__(self, brand)
        self.camera_type = camera_type

    def take_photo(self):
        print("Camera Type:", self.camera_type)
        print("Photo taken")


class Smartphone(Phone, Camera):
    def __init__(self, brand, phone_number, camera_type, model):
        Phone.__init__(self, brand, phone_number)
        Camera.__init__(self, brand, camera_type)
        self.model = model

    def display_smartphone(self):
        print("Model:", self.model)


s1 = Smartphone("Samsung", "9876543210", "Digital", "Galaxy S24")

s1.display_device()
s1.call()
s1.take_photo()
s1.display_smartphone()
#25
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        Person.__init__(self, name, age)
        self.course = course


class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary


class Intern(Student, Employee):
    def __init__(self, name, age, course, salary, duration):
        Student.__init__(self, name, age, course)
        Employee.__init__(self, name, age, salary)
        self.duration = duration

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Salary:", self.salary)
        print("Duration:", self.duration)


i1 = Intern("Navya", 22, "Python", 15000, "3 Months")

i1.display()

# 26
class Library:
    def __init__(self,library_name):
        self.library_name=library_name
class Book(Library):
    def __init__(self,library_name,book_name,author,price):
        super().__init__(library_name)
        self.book_name=book_name
        self.author=author
        self.price=price
class EBook(Book):
    def __init__(self,library_name,book_name,author,price,file_size):
        super().__init__(library_name,book_name,author,price)
        self.file_size=file_size
    def display(self):
        print("Library:", self.library_name)
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print("File Size:", self.file_size)
e1 = EBook("City Library", "Python Basics", "John", 500, "10 MB")

e1.display()


#27
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Customer(User):
    def __init__(self, name, email, customer_id):
        User.__init__(self, name, email)
        self.customer_id = customer_id


class Seller(User):
    def __init__(self, name, email, seller_id):
        User.__init__(self, name, email)
        self.seller_id = seller_id


class Marketplace(Customer, Seller):
    def __init__(self, name, email, customer_id, seller_id, product):
        Customer.__init__(self, name, email, customer_id)
        Seller.__init__(self, name, email, seller_id)
        self.product = product

    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Customer ID:", self.customer_id)
        print("Seller ID:", self.seller_id)
        print("Product:", self.product)


m1 = Marketplace(
    "Navya",
    "navya@gmail.com",
    101,
    201,
    "Laptop"
)

m1.display()

# 28. College Management System
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        Person.__init__(self,name, age)
        self.course = course


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self,name, age)
        self.subject = subject


class Assistant(Student, Teacher):
    def __init__(self, name, age, course, subject, role):
        Student.__init__(self, name, age, course)
        Teacher.__init__(self, name, age, subject)
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Subject:", self.subject)
        print("Role:", self.role)


a1 = Assistant("Navya", 22, "Python", "Database", "Teaching Assistant")

a1.display()

29
class Account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


class Savings(Account):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)


class Current(Account):
    def __init__(self, account_holder, account_number, balance, overdraft_limit):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Overdraft Limit:", self.overdraft_limit)


s1 = Savings("Navya", 101, 10000, 5)
s1.deposit(2000)
s1.withdraw(3000)
s1.display()

# 30
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)
        self.language = language


class Tester(Employee):
    def __init__(self, name, salary, testing_tool):
        Employee.__init__(self, name, salary)
        self.testing_tool = testing_tool


class TeamLead(Developer, Tester):
    def __init__(self, name, salary, language, testing_tool, team_size):
        Developer.__init__(self, name, salary, language)
        Tester.__init__(self, name, salary, testing_tool)
        self.team_size = team_size

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Testing Tool:", self.testing_tool)
        print("Team Size:", self.team_size)


t1 = TeamLead("Navya", 50000, "Python", "Selenium", 5)
t1.display()

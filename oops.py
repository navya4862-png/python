# 1.Student Details

class student():
  
  def __init__(self,name,age,course):
    self.name=name
    self.age=age
    self.course=course
    
  def display(self):
    print("Name:",self.name)
    print("Age:",self.age,"Course:",self.course)

s1=student("Navya",22,"ECE")
s2=student("Maggi",23,"CSE")
s3=student("Sandy",24,"AI")
s4=student("Varsha",25,"ML")

s1.display()
s2.display()
s3.display()
s4.display()

# 2 .Employee Salary

class Employee():

  def __init__(self,name,salary):
        self.name=name
        self.salary=salary

  def display_salary(self):
    print("Name:",self.name,"Salary:",self.salary)

#object
e1=Employee("Ravi",35000)
e2=Employee("Shiva",5000)

#fun call
Employee.display_salary(e1)
Employee.display_salary(e2) 

#  3.bank account

class bank():
  def __init__(self,account_holder,balance):
    self.account_holder=account_holder
    self.balance=balance

  def deposite(self,amount):
    self.balance+=amount

  def withdraw(self,amount):
    if amount>self.balance:
      print("Insuffienct Balance")
    else:
      self.balance-=amount
  def display(self):
    print("Name:",self.account_holder)
    print("Balance:",self.balance)

c1=bank("Raju",45000)
c2=bank("Vinnu",20000)

c1.deposite(3000)
c2.withdraw(500)

c1.display()
c2.display()

#  4.mobile
class mobile():
  
  def __init__(self,brand,model,price):
    self.brand=brand
    self.model=model
    self.price=price
    
  def display_mobile(self):
    print("Brand:",self.brand)
    print("Model:",self.model,"Price:",self.price)

m1 = mobile("Apple", "iPhone 15", 60000)
m2 = mobile("Samsung", "S24", 70000)

m1.display_mobile()
m2.display_mobile()

# 5.Rectange-Area and Perimeter

class Rectangle():
  def __init__(self,a,b):
    self.a=a
    self.b=b

  def area(self):
    print("Area of Rectangle:",self.a * self.b)

  def perimeter(self):
    print("Perimeter of Rectangle:", 2*(self.a + self.b))

a = int(input("Enter a value:"))
b=int(input("Enter a value:"))

r1=Rectangle(a,b)

r1.area()
r1.perimeter()

# 6. Student Marks
class Student():
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

  def display_marks(self):
    print("Name:",self.name)
    print("Marks:",self.marks)

  def check_result(self):
    
    if self.marks>=40:
      print("Pass")
    else:
      print("Fail")

s1=Student("Navya",45)
s2=Student("Sandy",90)
s3=Student("Mickey",78)
s4=Student("Kaju",80)
s5=Student("Vinnu",15)

s1.display_marks()
s1.check_result()
s2.display_marks()
s2.check_result()
s3.display_marks()
s3.check_result()
s4.display_marks()
s4.check_result()
s5.display_marks()
s5.check_result()


# 7 Employee Bonus

class Employee():
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

  def calculate_bonus(self):
    
    if self.salary>=50000:
      self.bonus=self.salary*0.1
      
    else:
        self.bonus=self.salary * 0.05
      
    self.total=self.bonus+self.salary
      
  def display(self):

    print("Employee Name:",self.name)
    print("Salary:",self.salary)
    print("Bonus:",self.bonus)
    print("Total Salary:",self.total)

e1=Employee("Nav",70000)

e1.calculate_bonus()
e1.display()

#8.Product Discount
class Product():
  def __init__(self,product_name,price):
     self.product_name=product_name
     self.price=price

  def calculate_discount(self):
    if self.price>=5000:
      self.discount=self.price*0.2
    elif self.price >=2000:
      self.discount=self.price*0.1
    else:
      self.discount=self.price*0.05
    self.total_price=self.price-self.discount

  def display(self):
    print("Product Name:",self.product_name)
    print("Price:",self.price)
    print("Discount:",self.discount)
    print("Final Price:",self.total_price)

p1=Product("Rice",10000)

p1.calculate_discount()
p1.display()

# 10. car information

class Car():
  def __init__(self,brand,price,fuel_type):
    self.brand=brand
    self.price=price
    self.fuel_type=fuel_type

  def display(self):
    print("Brand:",self.brand)
    print("Price:",self.price)
    print("Fuel Type:",self.fuel_type)

  def check_price(self):
    if self.price>1000000:
      print(self.brand,"is Premium Car")
    else:
      print(self.brand,"is Normal Car")

c1 = Car("BMW", 1500000, "Petrol")

c1.display()
c1.check_price()
    
c2 = Car("Toyota", 800000, "Diesel")

c2.display()
c2.check_price()

# 11.Electricity Bill

class ElectricityBill():
  
  def __init__(self,customer_name,units):
    self.customer_name=customer_name
    self.units=units

  def calculate_bill(self):
    if self.units<=100:
      self.price=self.units*2
    elif self.units>=101 and self.units<=200:
      self.price=self.units*3
    elif self.units >=201 and self.units<=300:
      self.price=self.units*5
    else:
      self.price=self.units*7

  def display_bill(self):
    print("Customer Name:",self.customer_name)
    print("Units:",self.units)
    print("Total Bill:",self.price)

c1=ElectricityBill("Raju",150)
c1.calculate_bill()
c1.display_bill()

c2 = ElectricityBill("Sita", 250)
c2.calculate_bill()
c2.display_bill()

# 12.Library Book

class Book():
  def __init__(self,title,author,price,available):
    self.title=title
    self.author=author
    self.price=price
    self.available=available

  def display_book(self):
    print("Title:", self.title)
    print("Author:", self.author)
    print("Price:", self.price)
    print("Available:", self.available)

  def borrow_book(self):
    if self.available:
       print("Book borrowed successfully")
       self.available=False
    else:
      print("Book is already borrowed")

  def return_book(self):
    if self.available==False:
      print("book returned successfully")
      self.available=True
    else:
      print("Book is already available")
      
      
b1 = Book("Python Basics", "John", 500, True)
b1.display_book()
b1.borrow_book()
b1.return_book()

b2 = Book("Data Analytics", "David", 800, False)
b2.display_book()
b2.borrow_book()
b2.return_book()

# 13.Shopping Cart
class Product():
  def __init__(self,name,price,quantity):
   self.name=name
   self.price=price
   self.quantity=quantity

  def calculate_total(self):
    self.total=self.price*self.quantity
  def display_product(self):
    print("Name:",self.name)
    print("Price:",self.price)
    print("Quantity:",self.quantity)
    print("Total Amount:",self.total)

p1=Product("Rice",50,5)
p1.calculate_total()
p1.display_product()

p2 = Product("Laptop", 50000, 2)
p2.calculate_total()
p2.display_product()

p3 = Product("Pen", 20, 10)
p3.calculate_total()
p3.display_product()

# 14.Employee Performane
class Employee():
  def __init__(self,name,salary,rating):
    self.name=name
    self.salary=salary
    self.rating=rating

  def display(self):
    print("Name:",self.name)
    print("Salary:",self.salary)
    print("Rating:",self.rating)

  def calculate_increment(self):
    if self.rating>=4.5:
      self.increment=self.salary*0.2
    elif self.rating>=3.5:
      self.increment=self.salary*0.1
    else:
      self.increment=self.salary*0.05

    print("Increment:",self.increment)

e1=Employee("Raju",35000,4.5)
e1.display()
e1.calculate_increment()

e2 = Employee("Sita", 50000, 3.8)
e2.display()
e2.calculate_increment()

#15.Bank Account Validation
class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance = self.balance - amount
            
        else:
            print("Withdrawal not allowed")

    def check_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


b1 = BankAccount("Ramu", 5000)

b1.deposit(2000)
b1.withdraw(5500)
b1.check_balance()

b2 = BankAccount("Sita", 3000)

b2.deposit(1000)
b2.withdraw(7500)
b2.check_balance()

#16.Online Food Order
class FoodOrder():
    def __init__(self, customer_name, food_name, price, quantity):
        self.customer_name = customer_name
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        self.total=self.price*self.quantity

    def apply_discount(self):
        if self.total>=2000:
          self.discount=self.total*0.2
        elif self.total>=1000:
          self.discount=self.total*0.1
        else:
          self.discount=0

        self.final_amount=self.total-self.discount

    def display_order(self):
        print("Customer Name:",self.customer_name)
        print("Food:",self.food_name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Discount:",self.discount)
        print("Final Amount:",self.final_amount)
      


f1 = FoodOrder("Ravi", "Biryani", 600, 4)

f1.calculate_total()
f1.apply_discount()
f1.display_order()

f2 = FoodOrder("Sita", "Pizza", 1200, 2)

f2.calculate_total()
f2.apply_discount()
f2.display_order()

#17.Hospital Patient
class Patient():
    def __init__(self, name, age, disease, bill):
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = bill

    def display_patient(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Bill:", self.bill)

    def add_bill(self, amount):
        self.bill = self.bill + amount

    def check_bill(self):
        print("Current Bill:", self.bill)


p1 = Patient("Raju", 45, "Fever", 5000)
p2 = Patient("Sita", 30, "Cold", 3000)

p1.add_bill(2000)
p2.add_bill(1500)

p1.display_patient()
p1.check_bill()

p2.display_patient()
p2.check_bill()

#18.Employee Attendance
class Employee():
    def __init__(self, name, total_days, present_days):
        self.name = name
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        self.attendance=(self.present_days/self.total_days)*100

    def check_attendance(self):
        if self.attendance>=75:
          print("Attendance:",self.attendance)
          print("Eligible")
        else:
          print("Attendance:",self.attendance)
          print("Not Eligible")
          


e1 = Employee("Raju", 100, 80)

e1.attendance_percentage()
e1.check_attendance()

#19.Movie Ticket Booking
class MovieTicket():
    def __init__(self, movie_name, ticket_price, number_of_tickets):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets

    def calculate_total(self):
        self.total = self.ticket_price * self.number_of_tickets

    def apply_discount(self):
        if self.number_of_tickets >= 5:
            self.discount = self.total * 0.10
        else:
            self.discount = 0

        self.final_price = self.total - self.discount

    def display_ticket(self):
        print("Movie Name:", self.movie_name)
        print("Ticket Price:", self.ticket_price)
        print("Number of Tickets:", self.number_of_tickets)
        print("Total:", self.total)
        print("Discount:", self.discount)
        print("Final Price:", self.final_price)


m1 = MovieTicket("Avatar", 300, 6)

m1.calculate_total()
m1.apply_discount()
m1.display_ticket()

#20.Student Report Card
class Student():
    def __init__(self, name, roll_no, python, sql, powerbi):
        self.name = name
        self.roll_no = roll_no
        self.python = python
        self.sql = sql
        self.powerbi = powerbi

    def calculate_total(self):
        self.total = self.python + self.sql + self.powerbi

    def calculate_average(self):
        self.average = self.total / 3

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 75:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 40:
            self.grade = "D"
        else:
            self.grade = "Fail"

    def display_report(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Python:", self.python)
        print("SQL:", self.sql)
        print("PowerBI:", self.powerbi)
        print("Total:", self.total)
        print("Average:", self.average)
        print("Grade:", self.grade)


s1 = Student("Kaju", 101, 85, 90, 80)

s1.calculate_total()
s1.calculate_average()
s1.calculate_grade()
s1.display_report()

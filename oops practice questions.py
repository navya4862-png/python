# 1. Create a Student class with attributes name, age, and marks. Create an object and display all the details. 

class Student():
  name="Navya"
  age=22
  marks=190
  
s1=Student()

print("Name:",s1.name,"Age:",s1.age,"Marks:",s1.marks)

#   2. Create a Car class with attributes brand and model. Create two objects with different values and display their details. 

class Car():
  
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    
c1=Car("XYZ",156)
c2=Car("ZXY",651)

print("Brand:",c1.brand,"Model:",c1.model)
print("Brand:",c2.brand,"Model:",c2.model)

#   3. Create a Calculator class with methods add(), subtract(), multiply(), and divide(). Take two numbers from the user and perform all operations. 
class calculator():
  
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
    
  def add(self):
    print("Addition:",self.num1+self.num2)
  def sub(self):
    print("Subtraction:",self.num1-self.num2)
  def mul(self):
    print("Multiplication:",self.num1*self.num2)
  def div(self):
    print("Division:",self.num1/self.num2)
    
a=int(input("Enter a Number1:"))
b=int(input("Enter a Number2:"))

obj=calculator(a,b)

obj.add()
obj.sub()
obj.mul()
obj.div()
  
#   4. Create a Rectangle class with attributes length and breadth. Create methods area() and perimeter(). 

class Rectangle():
  
  def __init__(self,a,b):
    self.a=a
    self.b=b
    
  def area(self):
    print("Area:",self.a*self.b)
    
  def perimeter(self):
    print("Perimeter:",2 * (self.a + self.b))
    
len=int(input("Enter a number:"))
bre=int(input("Enter a number:"))

obj=Rectangle(len,bre)

obj.area()
obj.perimeter()

# 5. Create an Employee class with attributes name, salary, and department. Create a method display_details() to print the employee information. 

class Employee():
  
  def __init__(self,name,salary,department):
    self.name=name
    self.salary=salary
    self.department=department
    
  def display_details(self):
    print("Name:",self.name)
    print("salary:",self.salary,"Department:",self.department)
    
e1=Employee("Raju",38000,"IT")
e2=Employee("Ravi",45000,"HR")
e3=Employee("Shiva",35000,"Sales")

Employee.display_details(e1)
Employee.display_details(e2)
Employee.display_details(e3)

# 6. Create a BankAccount class with an initial balance. Create methods deposit() and withdraw(). Display the updated balance after each operation. 

class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Updated Balance:", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Updated Balance:", self.balance)


balance = int(input("Enter initial balance: "))
obj = BankAccount(balance)

print("1. Deposit")
print("2. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter deposit amount: "))
    obj.deposit(amount)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))
    obj.withdraw(amount)

else:
    print("Invalid choice")


# 7. Create a Student class with a method calculate_grade() that returns: ○ 90–100 → A ○ 75–89 → B ○ 60–74 → C ○ 40–59 → D ○ Below 40 → F 

class Student():
  
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
  def calculate_grade(self):
      if 90 <= self.marks <= 100:
        print(self.name, "A")
      elif  75 <= self.marks <= 89:
        print(self.name, "B")
      elif 60 <= self.marks <= 74:
        print(self.name, "C")
      elif 40 <= self.marks <= 59:
        print(self.name, "D")
      else:
        print(self.name, "F")
        
s1=Student("Kavya",90)
s2=Student("Deepak",35)
s3=Student("Ravi",63)

Student.calculate_grade(s1)
Student.calculate_grade(s2)
Student.calculate_grade(s3)

# 8. Create a Person class with a method introduce() that prints the person's name, age, and city. Create three different objects and call the method for each.
class person():
  def __init__(self,name,age,city):
    self.name=name
    self.age=age
    self.city=city
  def introduce(self):
    print("Hello, my name is", self.name, "I am", self.age, "years old and I live in", self.city)

p1=person("Shiva", 31,"Hyderabad")
p2=person("Kaju",40,"Chennai")
p3=person("Megu",22,"Delhi")

person.introduce(p1)
person.introduce(p2)
person.introduce(p3)


# 9. Create a Product class with attributes name, price, and quantity. Create a method total_cost() that calculates price × quantity and displays the result. 

class Product():
  
  def __init__(self,name,price,quantity):
    self.name=name
    self.price=price
    self.quantity=quantity
    
  def total_cost(self):
    total_cost=self.price * self.quantity
    print("Name:",self.name,"Price:",self.price)
    print("Total Cost:",total_cost)

p1=Product("Sugar",50,15)
p2=Product("wheat",100,50)
p3=Product("Cookies",50,150)

Product.total_cost(p1)
Product.total_cost(p2)
Product.total_cost(p3)

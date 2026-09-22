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

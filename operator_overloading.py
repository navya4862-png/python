# Q1. Create a class Book with a pages attribute. 
# Overload + to add the pages of two books. 
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
page1=Book(120)
page2=Book(200)
print(page1+page2)

# Q2. Create a class Employee with a salary attribute. 
# Overload > to compare two employees' salaries. Easy
class Employee:
    def __init__(self,sal):
        self.sal=sal
    def __gt__(self,other):
        return self.sal>other.sal
e1=Employee(20000)
e2=Employee(30000)
print(e1>e2)
if e1>e2:
    print("E1 is greater")
else:
    print("E2 is greater")

# Q3. Create a class Temperature and overload - 
# to find the difference between two temperatures. 
class Temperature:
    def __init__(self,temp):
        self.temp=temp
    def __sub__(self,other):
        return self.temp-other.temp
t1=Temperature(300)
t2=Temperature(100)
print(t1-t2)
# Q4. Create a class Rectangle with length and width.
# Overload * to calculate the area of two rectangle objects by multiplying their areas. 
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __mul__(self,other):
        return (self.length * self.width) * (other.length*other.width)
l=Rectangle(20,30)
w=Rectangle(40,10)
mult=l * w
print(mult)
# Q5. Create a class Time with hours and minutes. 
# Overload + to add two time objects and normalize minutes when the total exceeds 60.
class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def __add__(self,other):
        total_minutes=self.minutes+other.minutes
        extra_hours=total_minutes // 60
        final_minutes=total_minutes % 60


        return f"{self.hours+other.hours+extra_hours} hr {final_minutes} min"
t1=Time(2,40)
t2=Time(1,30)
print(t1+t2)

# Q6. Create a class ShoppingCart with a list of item prices. 
# Overload + to combine the contents of two shopping carts.
class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def __add__(self, other):
        return self.prices + other.prices


cart1 = ShoppingCart([100, 200])
cart2 = ShoppingCart([50, 300])

print(cart1 + cart2)

# Q7. Create a class Distance and overload +, -, and == to add, subtract, and compare distances.
class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __add__(self, other):
        return self.distance + other.distance

    def __sub__(self, other):
        return self.distance - other.distance

    def __eq__(self, other):
        return self.distance == other.distance


d1 = Distance(50)
d2 = Distance(30)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
print("Equal:", d1 == d2)
# Q8. Create a class Vector with x and y coordinates. Overload +, -, and * to 
# add, subtract, and calculate the dot product of two vectors.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Dot Product:", v1 * v2)

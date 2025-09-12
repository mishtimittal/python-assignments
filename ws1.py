#question 1

print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")

#question 2

x=input("enter first name:")
y=input("enter last name: ")
print("reversed order=",y,x)

# question 3

r=float(input("enter radius:"))
area=(22/7)*r*r
print("area of circle=",area)

# question 4

color_list=["Red","Green","White" ,"Black"]
print("first colour:",color_list[0])
print("last colour:",color_list[3])

# question 5

n=int(input("enter value n="))
value=(n*1)+(n*11)+(n*111)
print(value)

# question 6

values = input("Enter comma-separated numbers: ")
list_values = values.split(",")
tuple_values = tuple(list_values)
print("List:", list_values)
print("Tuple:", tuple_values)

# question 7

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# question 8

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping: a =", a, " b =", b)

# question 9

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# question 10

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# question 11


import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", dist)

# question 12

a = int(input("Enter angle1: "))
b = int(input("Enter angle2: "))
c = int(input("Enter angle3: "))

if a + b + c == 180:
    print("It is a Triangle")
else:
    print("Not a Triangle")

# question 13

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
A = p * (1 + r/100)**t
CI = A - p
print("Compound Interest:", CI)

# question 14

n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# question 15

N = int(input("Enter a number: "))
sum_sq = sum(i*i for i in range(1, N+1))
print("Sum of squares:", sum_sq)

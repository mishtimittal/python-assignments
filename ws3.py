# 1
def diff_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    return abs(n - 17)

# 2
def test_range(n):
    return (100 <= n <= 1000) or (n == 2000)

# 3
def reverse_string(s):
    return s[::-1]

# 4
def count_case(s):
    d = {"UPPER": 0, "LOWER": 0}
    for c in s:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
    return d

# 5
def unique_list(lst):
    return list(set(lst))

# 6
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 7
def robot():
    def move():
        return "Robot is moving!"
    return move()

# 8
def student(name, age, course):
    print("Argument names:", student._code_.co_varnames)

# 9
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)

# 10
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"

# 11
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x, y) == (2, 0)

# 12
class Student:
    def _init_(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    
    def display(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}"

# 13
student1 = Student("101", "Alice", "CSE")
student2 = Student("102", "Bob", "ECE")
print(student1.display())
print(student2.display())

# 14
import math
class Circle:
    def _init_(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# 15
class MyString:
    def _init_(self):
        self.s = ""
    
    def get_String(self, s):
        self.s = s
    
    def print_String(self):
        print(self.s.upper())

# 16
class Robot:
    def _init_(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level
    
    def perform_task(self):
        print(f"{self.name} is performing {self.task}")
        self.battery_level -= 10
    
    def recharge(self):
        self.battery_level = 100
    
    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")
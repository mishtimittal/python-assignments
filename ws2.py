# Q1
L = [11, 12, 13, 14]

# (i) Add 50 and 60
L.extend([50, 60])
print("Q1(i):", L)

# (ii) Remove 11 and 13
L.remove(11)
L.remove(13)
print("Q1(ii):", L)

# (iii) Sort ascending
L.sort()
print("Q1(iii):", L)

# (iv) Sort descending
L.sort(reverse=True)
print("Q1(iv):", L)

# (v) Search for 13
print("Q1(v):", 13 in L)

# (vi) Count elements
print("Q1(vi):", len(L))

# (vii) Sum all elements
print("Q1(vii):", sum(L))

# (viii) Sum odd numbers
print("Q1(viii):", sum([x for x in L if x % 2 != 0]))

# (ix) Sum even numbers
print("Q1(ix):", sum([x for x in L if x % 2 == 0]))

# (x) Sum prime numbers
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print("Q1(x):", sum([x for x in L if is_prime(x)]))

# (xi) Clear L
L.clear()
print("Q1(xi):", L)

# (xii) Delete L
del L
# print(L)  # will give error


# Q2: Sum items in list (without sum())
lst = [1, 2, 3, 4]
s = 0
for i in lst:
    s += i
print("Q2:", s)


# Q3: Multiply items in list
lst = [1, 2, 3, 4]
mul = 1
for i in lst:
    mul *= i
print("Q3:", mul)


# Q4: 3*4*6 3D array of '*'
arr = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
print("Q4:", arr)


# Q5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i)
D[8] = 8.8
print("Q5(i):", D)

# (ii)
D.pop(2)
print("Q5(ii):", D)

# (iii)
print("Q5(iii):", 6 in D)

# (iv)
print("Q5(iv):", len(D))

# (v)
print("Q5(v):", sum(D.values()))

# (vi)
D[3] = 7.1
print("Q5(vi):", D)

# (vii)
D.clear()
print("Q5(vii):", D)


# Q6
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i)
S1.update([55, 66])
print("Q6(i):", S1)

# (ii)
S1.discard(10)
S1.discard(30)
print("Q6(ii):", S1)

# (iii)
print("Q6(iii):", 40 in S1)

# (iv)
print("Q6(iv):", S1.union(S2))

# (v)
print("Q6(v):", S1.intersection(S2))

# (vi)
print("Q6(vi):", S1 - S2)


# Q7(i): 100 random strings
import random, string
for _ in range(5):   # printing 5 instead of 100 (to see output)
    length = random.randint(6, 8)
    s = ''.join(random.choices(string.ascii_letters, k=length))
    print("Q7(i):", s)

# Q7(ii): Prime numbers between 600 and 800
primes = [x for x in range(600, 801) if is_prime(x)]
print("Q7(ii):", primes)

# Q7(iii): Numbers divisible by 7 and 9
nums = [x for x in range(100, 1001) if x%7==0 and x%9==0]
print("Q7(iii):", nums)


# Q8: Exam schedule
exam_st_date = (11, 12, 2025)
print("Q8: The examination will start from: %i / %i / %i"%exam_st_date)


# Q9
lst = [10,15,22,30,33,40]
for i in lst:
    if i%5==0:
        print("Q9:", i)


# Q10: Even or Odd using boolean
num = 7
is_even = (num%2==0)
print("Q10:", "Even" if is_even else "Odd")


# Q11: Count "Emma"
text = "Emma is good. Emma likes python. Emma codes."
print("Q11:", text.count("Emma"))


# Q12: New list odd from first, even from second
list1 = [1,2,3,4,5]
list2 = [10,11,12,13,14]
newlist = [x for x in list1 if x%2!=0] + [y for y in list2 if y%2==0]
print("Q12:", newlist)


# Q13: Robot positions
positions = [(2,3), (4,5), (6,7), (7,8)]
print("Q13:", [p for p in positions if p[0]%2==0])


# Q14: Sensor readings
sensor_data = {1:2.3, 2:4.5, 3:1.8, 4:3.6}
print("Q14:", [k for k,v in sensor_data.items() if v>3.0])


# Q15: Commands not executed
commands_received = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed = {"MOVE","TURN_LEFT","STOP"}
print("Q15:", commands_received - commands_executed)
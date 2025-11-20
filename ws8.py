import math


# Q1 – Point Class (Distance, Midpoint, Line Equation, Reflection)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def line_equation(A, B):
    if A.x == B.x:
        return None, None, f"x = {A.x}"

    m = (B.y - A.y) / (B.x - A.x)
    c = A.y - m * A.x
    return m, c, f"y = {m}x + {c}"


def reflect_point_over_line(A, B, C):
    a = B.y - A.y
    b = A.x - B.x
    c = B.x*A.y - A.x*B.y

    d = (a*C.x + b*C.y + c) / (a*a + b*b)

    rx = C.x - 2*a*d
    ry = C.y - 2*b*d

    return Point(rx, ry)


# Q2 – Vector Operations


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_with(self, other):
        dot = self.dot(other)
        mag = self.magnitude() * other.magnitude()
        return math.degrees(math.acos(dot / mag))

    def projection_on(self, other):
        scalar = self.dot(other) / (other.magnitude() ** 2)
        return Vector(scalar * other.x, scalar * other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"



# Q3 – Segment and Closest Point

def segment_length(S, E):
    return math.hypot(E.x - S.x, E.y - S.y)


def closest_point_on_segment(S, E, P):
    SE = ((E.x - S.x), (E.y - S.y))
    SP = ((P.x - S.x), (P.y - S.y))

    seg_len_sq = SE[0]**2 + SE[1]**2
    if seg_len_sq == 0:
        return S

    # projection factor t
    t = (SP[0]*SE[0] + SP[1]*SE[1]) / seg_len_sq
    t = max(0, min(1, t))  # clamp to segment

    closest_x = S.x + t * SE[0]
    closest_y = S.y + t * SE[1]
    return Point(closest_x, closest_y)


def distance_point_to_segment(S, E, P):
    closest = closest_point_on_segment(S, E, P)
    return closest, math.hypot(P.x - closest.x, P.y - closest.y)



# Q4 – Line Intersection


def line_intersection(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1

    if det == 0:
        return None  # parallel or same

    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    return Point(x, y)



print("\n================= Q1 OUTPUT =================")

A = Point(1, 3)
B = Point(5, 6)
C = Point(2, 1)

print("Distance AB:", A.distance(B))
print("Midpoint AB:", A.midpoint(B))

m, c, eq = line_equation(A, B)
print("Line Equation:", eq)

ref = reflect_point_over_line(A, B, C)
print("Reflection of C over AB:", ref)


print("\n================= Q2 OUTPUT =================")

A_vec = Vector(2, 3)
B_vec = Vector(-1, 4)
C_vec = Vector(3, -2)

R = A_vec.add(B_vec).add(C_vec)
print("Resultant Vector R:", R)

print("Magnitude A:", A_vec.magnitude())
print("Magnitude B:", B_vec.magnitude())
print("Magnitude C:", C_vec.magnitude())

print("A·B =", A_vec.dot(B_vec))
print("A·C =", A_vec.dot(C_vec))
print("B·C =", B_vec.dot(C_vec))

print("Angle(A,B) =", A_vec.angle_with(B_vec))
print("Angle(A,C) =", A_vec.angle_with(C_vec))
print("Angle(B,C) =", B_vec.angle_with(C_vec))

print("Projection of A on B:", A_vec.projection_on(B_vec))


print("\n================= Q3 OUTPUT =================")

S = Point(0, 0)
E = Point(6, 4)
P = Point(3, 10)

print("Length of segment SE:", segment_length(S, E))

closest, dist = distance_point_to_segment(S, E, P)
print("Closest point to P:", closest)
print("Distance from P to segment:", dist)


print("\n================= Q4 OUTPUT =================")

# Example:
# L1 : a1x + b1y = c1
# L2 : a2x + b2y = c2

a1, b1, c1 = 2, -1, 3
a2, b2, c2 = 1, 2, 10

pt = line_intersection(a1, b1, c1, a2, b2, c2)

if pt is None:
    print("Lines are parallel or coincident.")
else:
    print("Intersection point:", pt)

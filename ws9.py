import tkinter as tk





root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

tk.Label(root, text="Robot Control Panel", bg="yellow", font=("Arial", 16)).pack(pady=10)

root.mainloop()







root = tk.Tk()
root.title("Q2 - Black Point")
c = tk.Canvas(root, width=300, height=200, bg="white")
c.pack()

x, y = 100, 100
r = 2 
c.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")

root.mainloop()






pts = [(20,50), (100,120), (180,90), (250,150)]

root = tk.Tk()
root.title("Q3 - Robot Path")
c = tk.Canvas(root, width=300, height=200, bg="white")
c.pack()

flat = [coord for p in pts for coord in p]
c.create_line(*flat, fill="blue", width=3, joinstyle="round")

for x,y in pts:
    c.create_oval(x-3, y-3, x+3, y+3, fill="blue", outline="")

root.mainloop()








root = tk.Tk()
root.title("Q4 - Moving Point")
W, H = 500, 150
c = tk.Canvas(root, width=W, height=H, bg="white")
c.pack()

x, y = 10, H//2
r = 4
point = c.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="")

dx = 4

def animate():
    c.move(point, dx, 0)
    pos = c.coords(point)  
    if pos[2] < W:
        root.after(30, animate) 
    else:
        
        c.coords(point, -r, y-r, -r* -1, y+r)  
        
animate()
root.mainloop()








root = tk.Tk()
root.title("Q5 - Simple Robot")
c = tk.Canvas(root, width=300, height=180, bg="white")
c.pack()

body = c.create_rectangle(80,40,220,120, fill="#a0c4ff", outline="black", width=2)
left_wheel = c.create_oval(90,110,130,150, fill="black")
right_wheel = c.create_oval(170,110,210,150, fill="black")

c.create_oval(110,60,125,75, fill="white", outline="")
c.create_oval(175,60,190,75, fill="white", outline="")

root.mainloop()








root = tk.Tk()
root.title("Q6 - Robot Controller")
W, H = 400, 300
c = tk.Canvas(root, width=W, height=H, bg="lightgray")
c.pack()

rx, ry, r = 200, 150, 12
robot = c.create_oval(rx-r, ry-r, rx+r, ry+r, fill="orange", outline="")

def move(dx, dy):
    c.move(robot, dx, dy)
    
    x1,y1,x2,y2 = c.coords(robot)
    if x1 < 0: c.move(robot, -x1, 0)
    if y1 < 0: c.move(robot, 0, -y1)
    if x2 > W: c.move(robot, W-x2, 0)
    if y2 > H: c.move(robot, 0, H-y2)

frame = tk.Frame(root)
frame.pack(pady=8)

btn_up = tk.Button(frame, text="Up", width=8, command=lambda: move(0, -10))
btn_left = tk.Button(frame, text="Left", width=8, command=lambda: move(-10, 0))
btn_right = tk.Button(frame, text="Right", width=8, command=lambda: move(10, 0))
btn_down = tk.Button(frame, text="Down", width=8, command=lambda: move(0, 10))

btn_up.grid(row=0, column=1, padx=4, pady=2)
btn_left.grid(row=1, column=0, padx=4, pady=2)
btn_right.grid(row=1, column=2, padx=4, pady=2)
btn_down.grid(row=2, column=1, padx=4, pady=2)

root.mainloop()










root = tk.Tk()
root.title("Q7 - Bouncing Ball")
W, H = 500, 300
c = tk.Canvas(root, width=W, height=H, bg="white")
c.pack()

x, y = 200, 150
r = 15
ball = c.create_oval(x-r, y-r, x+r, y+r, fill="green", outline="")

dx, dy = 4, 3  

def update():
    global dx, dy
    c.move(ball, dx, dy)
    x1,y1,x2,y2 = c.coords(ball)

    if x1 <= 0 or x2 >= W:
        dx = -dx
 
    if y1 <= 0 or y2 >= H:
        dy = -dy
    root.after(20, update)

update()
root.mainloop()







import math

root = tk.Tk()
root.title("Q8 - Robot to Target")
W, H = 520, 300
c = tk.Canvas(root, width=W, height=H, bg="white")
c.pack()

start = (50,200)
target = (450,200)
r = 10
robot = c.create_oval(start[0]-r, start[1]-r, start[0]+r, start[1]+r, fill="purple", outline="")

dx = target[0] - start[0]
dy = target[1] - start[1]
dist = math.hypot(dx, dy)
if dist == 0:
    step = (0,0)
else:
    speed = 3.0 
    step = (dx/dist*speed, dy/dist*speed)

def move():
    x1,y1,x2,y2 = c.coords(robot)
    cx = (x1+x2)/2
    cy = (y1+y2)/2
  
    rem = math.hypot(target[0]-cx, target[1]-cy)
    if rem <= speed:
       
        c.coords(robot, target[0]-r, target[1]-r, target[0]+r, target[1]+r)
    else:
        c.move(robot, step[0], step[1])
        root.after(20, move)

move()
root.mainloop()

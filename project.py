import numpy as np
import pandas as pd

# -----------------------
# Project 1: Sensor Data
# -----------------------

# Load sensor data
sensor_df = pd.read_csv("sensor_data.csv")

# Convert numeric columns to numpy arrays
temp = sensor_df["temperature"].to_numpy()
dist = sensor_df["distance"].to_numpy()
batt = sensor_df["battery"].to_numpy()
humi = sensor_df["humidity"].to_numpy()

# Calculate average, min, and max for each sensor
avg_temp, min_temp, max_temp = np.mean(temp), np.min(temp), np.max(temp)
avg_dist, min_dist, max_dist = np.mean(dist), np.min(dist), np.max(dist)
avg_batt, min_batt, max_batt = np.mean(batt), np.min(batt), np.max(batt)
avg_humi, min_humi, max_humi = np.mean(humi), np.min(humi), np.max(humi)

# Find the time when temperature was highest
max_temp_index = np.argmax(temp)
time_of_max_temp = sensor_df.loc[max_temp_index, "timestamp"]

# Count how many times battery dropped below 30%
battery_below_30 = np.sum(batt < 30)

# Save results to a text file
with open("sensor_results.txt", "w") as f:
    f.write("=== Sensor Data Results ===\n\n")
    f.write(f"Temperature -> Avg: {avg_temp:.2f}, Min: {min_temp:.2f}, Max: {max_temp:.2f}\n")
    f.write(f"Distance -> Avg: {avg_dist:.2f}, Min: {min_dist:.2f}, Max: {max_dist:.2f}\n")
    f.write(f"Battery -> Avg: {avg_batt:.2f}, Min: {min_batt:.2f}, Max: {max_batt:.2f}\n")
    f.write(f"Humidity -> Avg: {avg_humi:.2f}, Min: {min_humi:.2f}, Max: {max_humi:.2f}\n")
    f.write(f"\nTime of highest temperature: {time_of_max_temp}\n")
    f.write(f"Battery below 30% count: {battery_below_30}\n")


# -----------------------
# Project 2: Robot Path
# -----------------------

# Load robot path data
robot_df = pd.read_csv("robot_path (1).csv")
x = robot_df["x"].to_numpy()
y = robot_df["y"].to_numpy()

# Calculate total distance traveled
total_distance = 0
for i in range(1, len(x)):
    dx = x[i] - x[i-1]
    dy = y[i] - y[i-1]
    total_distance += np.sqrt(dx**2 + dy**2)

# Find the farthest point from the origin (0,0)
distances = np.sqrt(x**2 + y**2)
farthest_index = np.argmax(distances)
farthest_point = (x[farthest_index], y[farthest_index])

# Check for revisited positions (efficient way)
positions = list(zip(x, y))
seen = set()
revisited = []
for pos in positions:
    if pos in seen and pos not in revisited:
        revisited.append(pos)
    seen.add(pos)

# Save results to a text file
with open("robot_results.txt", "w") as f:
    f.write("=== Robot Path Results ===\n\n")
    f.write(f"Total distance traveled: {total_distance:.2f}\n")
    f.write(f"Farthest point from origin: {farthest_point}\n")
    if revisited:
        f.write(f"Revisited positions: {revisited}\n")
    else:
        f.write("No revisited positions detected.\n")

print("Results saved in 'sensor_results.txt' and 'robot_results.txt'")

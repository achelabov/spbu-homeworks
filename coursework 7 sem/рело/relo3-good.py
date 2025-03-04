import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the vertices of the equilateral triangle and translate to origin
v1 = np.array([0.0, 0.0])
v2 = np.array([1.0, 0.0])
v3 = np.array([0.5, np.sqrt(3)/2])
centroid = np.array([(v1[0]+v2[0]+v3[0])/3, (v1[1]+v2[1]+v3[1])/3])
v1_centered = v1 - centroid
v2_centered = v2 - centroid
v3_centered = v3 - centroid

# Generate points for each arc of the Reuleaux triangle
num_points = 100
radius = 1.0  # Side length of the triangle

# Function to generate arc points
def generate_arc(center, start_point, end_point, num_points):
    vector_start = start_point - center
    vector_end = end_point - center
    theta_start = np.arctan2(vector_start[1], vector_start[0])
    theta_end = np.arctan2(vector_end[1], vector_end[0])
    if theta_end < theta_start:
        theta_end += 2 * np.pi
    theta = np.linspace(theta_start, theta_end, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y

# Generate the three arcs
x_arc1, y_arc1 = generate_arc(v3_centered, v1_centered, v2_centered, num_points)
x_arc2, y_arc2 = generate_arc(v1_centered, v2_centered, v3_centered, num_points)
x_arc3, y_arc3 = generate_arc(v2_centered, v3_centered, v1_centered, num_points)

# Combine all points
x = np.concatenate([x_arc1, x_arc2, x_arc3])
y = np.concatenate([y_arc1, y_arc2, y_arc3])

# Set up the animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    theta = frame * 2 * np.pi / 100  # Full rotation over 100 frames
    rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta),  np.cos(theta)]])
    rotated_points = np.dot(rot_matrix, np.vstack([x, y]))
    line.set_data(rotated_points[0], rotated_points[1])
    return line,

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=20)

plt.show()
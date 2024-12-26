import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
crank_length = 1.0  # Length of the crank
connecting_rod_length = 1.5  # Length of the connecting rod
slider_position = 0.0  # Initial position of the slider
num_frames = 100  # Number of frames for the animation

# Function to calculate the position of the slider
def calculate_slider_position(theta):
    # x position of the crank end
    x_crank = crank_length * np.cos(theta)
    # y position of the crank end
    y_crank = crank_length * np.sin(theta)
    
    # Using Pythagorean theorem to find the slider position
    slider_position = np.sqrt(connecting_rod_length**2 - x_crank**2)
    
    return x_crank, y_crank, slider_position

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# Initialize lines for crank, connecting rod, and slider
crank_line, = ax.plot([], [], 'ro-', label='Crank')
rod_line, = ax.plot([], [], 'bo-', label='Connecting Rod')
slider_line, = ax.plot([], [], 'go-', label='Slider')

# Add legend
ax.legend()

# Animation update function
def update(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid()
    
    # Calculate the angle of the crank
    theta = 2 * np.pi * frame / num_frames
    
    # Get positions
    x_crank, y_crank, slider_pos = calculate_slider_position(theta)
    
    # Update crank position
    crank_line.set_data([0, x_crank], [0, y_crank])
    
    # Update connecting rod position
    rod_line.set_data([x_crank, x_crank], [y_crank, slider_pos])
    
    # Update slider position
    slider_line.set_data([x_crank], [slider_pos])
    
    return crank_line, rod_line, slider_line

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the plot
plt.show()


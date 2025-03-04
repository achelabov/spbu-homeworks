import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the vertices of the equilateral triangle
A = np.array([0.0, 0.0])
B = np.array([1.0, 0.0])
C = np.array([0.5, np.sqrt(3)/2])

# Function to plot the Reuleaux triangle
def plot_reuleaux(ax):
    # Circle 1 centered at A
    theta1 = np.linspace(0, 2*np.pi, 100)
    x1 = A[0] + np.cos(theta1)
    y1 = A[1] + np.sin(theta1)
    ax.plot(x1, y1, 'b--', alpha=0.5)

    # Circle 2 centered at B
    theta2 = np.linspace(0, 2*np.pi, 100)
    x2 = B[0] + np.cos(theta2)
    y2 = B[1] + np.sin(theta2)
    ax.plot(x2, y2, 'b--', alpha=0.5)

    # Circle 3 centered at C
    theta3 = np.linspace(0, 2*np.pi, 100)
    x3 = C[0] + np.cos(theta3)
    y3 = C[1] + np.sin(theta3)
    ax.plot(x3, y3, 'b--', alpha=0.5)

    # Plot the Reuleaux triangle arcs
    # Arc from A to B on circle C
    theta_arc1 = np.linspace(np.pi/2, -np.pi/2, 100)
    x_arc1 = C[0] + np.cos(theta_arc1)
    y_arc1 = C[1] + np.sin(theta_arc1)
    ax.plot(x_arc1, y_arc1, 'r')

    # Arc from B to C on circle A
    theta_arc2 = np.linspace(-np.pi/6, np.pi - np.pi/6, 100)
    x_arc2 = A[0] + np.cos(theta_arc2)
    y_arc2 = A[1] + np.sin(theta_arc2)
    ax.plot(x_arc2, y_arc2, 'r')

    # Arc from C to A on circle B
    theta_arc3 = np.linspace(np.pi + np.pi/6, 2*np.pi - np.pi/6, 100)
    x_arc3 = B[0] + np.cos(theta_arc3)
    y_arc3 = B[1] + np.sin(theta_arc3)
    ax.plot(x_arc3, y_arc3, 'r')

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.axis([-0.5, 1.5, -0.5, 1.5])

# Plot the Reuleaux triangle
plot_reuleaux(ax)

# Define initial parallel tangent lines
width = 1.0  # Constant width of the Reuleaux triangle
line1, = ax.plot([], [], 'g-', lw=2)
line2, = ax.plot([], [], 'g-', lw=2)

# Animation function
def animate(theta):
    # Rotate the Reuleaux triangle
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    A_rot = np.dot(rotation_matrix, A)
    B_rot = np.dot(rotation_matrix, B)
    C_rot = np.dot(rotation_matrix, C)

    # Calculate the positions of the tangent lines
    # For simplicity, assume lines are horizontal
    y_top = width / 2
    y_bottom = -width / 2
    x_min, x_max = ax.get_xlim()
    line1.set_data([x_min, x_max], [y_top, y_top])
    line2.set_data([x_min, x_max], [y_bottom, y_bottom])

    return line1, line2

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 100),
                              interval=50, blit=True)

# Display the constant width value
ax.text(-0.4, 1.2, f'Constant Width: {width}', fontsize=12)

plt.show()
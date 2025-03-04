import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def rotate(x, y, cx, cy, angle):
    """
    Rotate points (x, y) around the center (cx, cy) by a given angle.
    
    :param x: array-like, x coordinates of points
    :param y: array-like, y coordinates of points
    :param cx: float, x coordinate of the center of rotation
    :param cy: float, y coordinate of the center of rotation
    :param angle: float, angle of rotation in radians
    :return: tuple of rotated x and y coordinates
    """
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    x_rotated = cx + (x - cx) * cos_theta - (y - cy) * sin_theta
    y_rotated = cy + (x - cx) * sin_theta + (y - cy) * cos_theta
    
    return x_rotated, y_rotated

def reuleaux_poly(n, N, W):
    """
    Generate a Reuleaux (constant-width) polygon.
    
    :param n: int, number of vertices (must be odd)
    :param N: int, number of points to draw along each edge of the boundary
    :param W: float, edge width
    :return: tuple of arrays (x_out, y_out, x_t, y_t)
    """
    if n < 3:
        raise ValueError('we must have n >= 3')
    if n % 2 == 0:
        raise ValueError('n must be odd')
    if N < 3:
        raise ValueError('N >= 3')
    if W <= 0:
        raise ValueError('W > 0')
    
    alpha = 2 * np.pi / n
    c = 1 + np.cos(alpha / 2)
    s = np.sin(alpha / 2)
    unit_width = np.sqrt(c**2 + s**2)
    R = W / unit_width
    
    theta = np.arange(0, 2 * np.pi, alpha)
    x_t = R * np.cos(theta)
    y_t = R * np.sin(theta)
    
    beta = 2 * np.arctan2(np.sin(alpha / 2), 1 + np.cos(alpha / 2))
    phi = np.linspace(np.pi - beta / 2, np.pi + beta / 2, N)
    x = R + W * np.cos(phi)
    y = W * np.sin(phi)
    
    x_out = x
    y_out = y
    for i in range(1, n):
        x, y = rotate(x, y, 0, 0, alpha)
        x_out = np.concatenate((x_out, x))
        y_out = np.concatenate((y_out, y))
    
    x_out = np.concatenate((x_out, [x_out[0]]))
    y_out = np.concatenate((y_out, [y_out[0]]))
    
    return x_out, y_out, x_t, y_t

def rolling_polygon(x, y, x1, y1, delta_a, prefix, figure_n):
    """
    Roll a polygon along a flat surface and track points on the polygon.
    
    :param x: array-like, x coordinates of the polygon
    :param y: array-like, y coordinates of the polygon
    :param x1: array-like, x coordinates of points to track
    :param y1: array-like, y coordinates of points to track
    :param delta_a: float, maximum step size for rotation
    :param prefix: str, prefix for animation files
    :param figure_n: int, figure number for plotting
    :return: tuple of tracked points (X, Y)
    """
    mn_y = np.min(y)
    y = y - mn_y
    y1 = y1 - mn_y
    
    dx = np.diff(x)
    dy = np.diff(y)
    edge_lengths = np.sqrt(dx**2 + dy**2)
    edge_angles = np.arctan2(dy, dx)
    I = np.where(y == np.min(y))[0][-1]
    
    fig = plt.figure(figure_n)
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'b', linewidth=2)
    ax.plot(x1, y1, 'g.', linewidth=2)
    
    P = poly_perimeter(x, y)
    ax.set_xlim(min(x) - 0.5, max(x) + 0.5 + P)
    ax.plot([min(x) - 0.5, max(x) + 0.5 + P], [0, 0], '-', linewidth=2)
    ax.set_ylim(-0.1, max(y) + 0.1)
    ax.axis('equal')
    ax.axis('off')
    
    filename = f'{prefix}_000.png'
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    
    X = [x1]
    Y = [y1]
    m = 1
    
    for i in range(len(x) - 1):
        if edge_angles[I] < 0:
            phi = 2 * np.pi + edge_angles[I]
        else:
            phi = edge_angles[I]
        
        if abs(edge_lengths[I]) < 1e-10:
            continue
        elif phi > delta_a:
            steps = int(np.ceil(phi / delta_a))
            phi2 = phi / steps
            for j in range(steps):
                x, y = rotate(x, y, x[I], y[I], -phi2)
                x1, y1 = rotate(x1, y1, x[I], y[I], -phi2)
                X.append(x1)
                Y.append(y1)
                
                fig = plt.figure(figure_n)
                ax = fig.add_subplot(111)
                ax.plot(x, y, 'r')
                ax.plot([X[-2][0], X[-1][0]], [Y[-2][0], Y[-1][0]], 'g')
                filename = f'{prefix}_{m:03d}.png'
                plt.savefig(filename, bbox_inches='tight')
                plt.close(fig)
                m += 1
        else:
            x, y = rotate(x, y, x[I], y[I], -phi)
            x1, y1 = rotate(x1, y1, x[I], y[I], -phi)
            X.append(x1)
            Y.append(y1)
            
            fig = plt.figure(figure_n)
            ax = fig.add_subplot(111)
            ax.plot(x, y, 'r')
            ax.plot([X[-2][0], X[-1][0]], [Y[-2][0], Y[-1][0]], 'g')
            filename = f'{prefix}_{m:03d}.png'
            plt.savefig(filename, bbox_inches='tight')
            plt.close(fig)
            m += 1
        
        edge_angles = np.roll(edge_angles, -1)
    
    images = []
    for filename in sorted(os.listdir('.')):
        if filename.startswith(prefix) and filename.endswith('.png'):
            images.append(imageio.imread(filename))
    
    imageio.mimsave(f'{prefix}.gif', images, duration=0.1)
    
    # Clean up PNG files
    for filename in sorted(os.listdir('.')):
        if filename.startswith(prefix) and filename.endswith('.png'):
            os.remove(filename)
    
    return np.array(X), np.array(Y)

def poly_perimeter(xv, yv):
    """
    Calculate the perimeter of a polygon.
    
    :param xv: array-like, x coordinates of polygon vertices
    :param yv: array-like, y coordinates of polygon vertices
    :return: float, perimeter of the polygon
    """
    dx = np.diff(xv)
    dy = np.diff(yv)
    edge_length = np.sqrt(dx**2 + dy**2)
    return np.sum(edge_length)

# Example usage:
n = 5  # Number of vertices (must be odd)
N = 20  # Number of points to draw along each edge
W = 1   # Edge width
delta_a = np.pi / 10  # Maximum step size for rotation
prefix = 'reuleaux_animation'  # Prefix for animation files
figure_n = 1  # Figure number for plotting

x_out, y_out, x_t, y_t = reuleaux_poly(n, N, W)
rolling_polygon(x_out, y_out, x_t, y_t, delta_a, prefix, figure_n)
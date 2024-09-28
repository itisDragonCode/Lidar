import numpy as np
import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def process_lidar_data(lidar_data):
    data = lidar_data
    points=[]
    for angle_str, distance in data.items():
        angle = float(angle_str)
        angle = degrees_to_radians(angle)
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        points.append([x, y])
    return points


def create_grid_map(points):
    # Find minimum and maximum x and y coordinates
    min_x = min(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    
    
    # Shift all points to ensure positive coordinates
    #translated_points = [(x - min_x, y - min_y) for (x, y) in points]
    
    # Determine new grid dimensions after translation
    grid_width = int(max_x - min_x) + 1
    grid_height = int(max_y - min_y) + 1
    
    # Create grid
    grid = np.ones((grid_height, grid_width))
    
    for (x, y) in points:
        grid_x = int(x)
        grid_y = int(y)
        grid[grid_y, grid_x] = 0  # Mark the cell as occupied
    
    return grid.tolist()

def create_grid(points, path=None):
    # Find minimum and maximum x and y coordinates
    min_x = int(min(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_x = int(max(point[0] for point in points))
    max_y = int(max(point[1] for point in points))
    
    # Determine new grid dimensions after translation
    grid_width = max_x - min_x + 1
    grid_height = max_y - min_y + 1

    lidar_cor = (0 - min_y, 0 - min_x)
    
    # Create grid
    grid = np.ones((grid_height, grid_width))
    
    for (x, y) in points:
        # grid_x = int(x)
        # grid_y = int(y)
        grid_x = int(x - min_x)
        grid_y = int(y - min_y)
        grid[grid_y, grid_x] = 0  # Mark the cell as occupied
   
    
    # grid[lidar_cor[0], lidar_cor[1]] = 0.75
    
    return grid.tolist(), lidar_cor

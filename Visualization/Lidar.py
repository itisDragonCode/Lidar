import time
from listen_to_lidar import listen_to_lidar
import functions as f
import numpy as np
import matplotlib.pyplot as plt

lidar_data, stop = listen_to_lidar()
#print(lidar_data['distances']) # prints the dictionary with all the accumulated distance data
time.sleep(1)
#print(lidar_data['distances']) # prints the updated distance data

stop()

cartesian_dots =  np.array(f.process_lidar_data(lidar_data['distances']))

grid= f.create_grid_map(cartesian_dots)

plt.imshow(grid , cmap='magma', origin='lower')
plt.gca().invert_yaxis()
plt.colorbar(label='Occupancy')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grid Map with Different Colors for 0 and 1')
plt.show()

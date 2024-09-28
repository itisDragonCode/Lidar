import time
from listen_to_lidar import listen_to_lidar
import functions as f
import numpy as np
import matplotlib.pyplot as plt
from grid import Grid
from astar import a_star

lidar_data, stop = listen_to_lidar()
#print(lidar_data['distances']) # prints the dictionary with all the accumulated distance data
time.sleep(1)
#print(lidar_data['distances']) # prints the updated distance data

stop()

cartesian_dots =  np.array(f.process_lidar_data(lidar_data['distances']))

#grid= f.create_grid_map(cartesian_dots)

grid, cor = f.create_grid(cartesian_dots)

rows = len(grid)
cols = len(grid[0])

obsticles = []

for i in range(0,rows):
    for j in range(0,cols):
        if grid[i][j] == 0:
            obsticles.append((i,j))

g = Grid(cols,rows, obstacles=obsticles)

src = (cor[0],cor[1])

g.grid[cor[0]][cor[1]] = 0.75

print(f'Coordinates of robot are ({cor[1]},{cor[0]})')

# Print the created grid
plt.imshow(g.grid, cmap='magma', origin='lower')
plt.gca().invert_yaxis()
plt.colorbar(label='Occupancy')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grid Map with Different Colors for 0 and 1')
plt.grid(True, which='both',  linestyle='', linewidth=0.5)
plt.show()

valid_dest = False

g.grid[cor[0]][cor[1]]= 1

while valid_dest==False:
    destX = int(input('Enter x value of destination: '))
    destY = int(input('Enter y value of destination: '))
    if(g.grid[destY][destX] == 0 or destX > cols or destX < 0 or destY > rows or destY < 0):
        print("Destination is blocked!")
    else:
        valid_dest = True

path = a_star(g, src, (destY,destX))

for node in path:
    if(g.grid[node[0]][node[1]]!=0):
        g.grid[node[0]][node[1]] = 0.5

g.grid[cor[0]][cor[1]]= 0.75

plt.imshow(g.grid, cmap='magma', origin='lower')
plt.gca().invert_yaxis()
plt.colorbar(label='Occupancy')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grid Map with Different Colors for 0 and 1')
plt.grid(True, which='both',  linestyle='', linewidth=0.5)
plt.show()

# plt.imshow(grid , cmap='magma', origin='lower')
# plt.gca().invert_yaxis()
# plt.colorbar(label='Occupancy')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Grid Map with Different Colors for 0 and 1')
# plt.show()
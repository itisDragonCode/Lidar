from itertools import product

class Grid(object):

    def __init__(self, i, j, obstacles = []):
        self.i = i
        self.j = j
        self.grid = [[1] * i for _ in range(j)]

        self.obstacles = obstacles

        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = 0

    def __str__(self):
        return "\n".join("".join(x) for x in self.char_map())

    def __repr__(self):
        return "{} by {} grid:\n".format(self.i, self.j) + self.__str__()

    def char_map(self):
        arr = [["_"] * self.j for _ in range(self.i)]

        for obstacle in self.obstacles:
            arr[obstacle[0]][obstacle[1]] = "X"

        return arr

    def get_adjacent(self, node):
        i = node[0]
        j = node[1]

        if i < 0 or i >= self.i or j < 0 or j >= self.j:
            raise Exception("Out of bounds")

        if self.grid[i][j] != 1:
            return []

        adjacent = []

        for del_pos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= i + del_pos[0] < self.j and 0 <= j + del_pos[1] < self.j:
                if self.grid[i + del_pos[0]][j + del_pos[1]] == 1:
                    adjacent.append((i + del_pos[0], j + del_pos[1]))

        return adjacent

    def get_nodes(self):
        return [(i, j) for i, j in product(range(self.i), range(self.j)) if (i, j) not in self.obstacles]

    def plot_path(self, path):
        arr = self.char_map()
        for node in path:
            arr[node[0]][node[1]] = "."

        return "\n".join("".join(x) for x in arr)

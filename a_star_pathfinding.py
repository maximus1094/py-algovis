# A Star Pathfinding Notes

# Movement cost: straight line - 10, diagonal - 14

# Node's G-Cost: node's 'distance' away from start node.
# Node's H-Cost: node's 'distance' away from end node. (can be precomputed)
    # Manhattan distance, 1 for each square
# Node's F-Cost: G + H

"""
NOTE: Everything in this pathfinding algorithm is adopted to the
system where it will be used. ie. to the main.py.

eg. Node.node_type must be one of the tile types in main.py.
"""

import time

# TILE TYPES
T_EMPTY = 0
T_BLOCKED = 1
T_SEARCH = 2
T_END = 3

# MOVEMENT TYPES
M_STRAIGHT = 10
M_DIAGONAL = 14

"""
Nodes are units on which A star search algorithm operates.

Performing the search simply on a 2D array is not possible, 
as additional information about each tile is needed.
Therefore, before starting the search, 2D arrays of integers are converted to
2D arrays on Nodes.
"""
class Node:
    def __init__(self, x_pos, y_pos, h_cost, node_type):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.h_cost = h_cost
        self.g_cost = None
        self.f_cost = None
        self.node_type = node_type
        self.parent_node = None

    def calc_f_cost(self):
        self.f_cost = self.h_cost + self.g_cost

"""
Position of object that we are searching for is used to calculate the H-COST.

If end position is not provided, this function can be used to calculate it,
as long as the tile is marked with the appropriate value.
"""
def get_endtile_pos(arr):
    arr_size = len(arr[0])

    for y in range(arr_size):
        for x in range(arr_size):
            if arr[y][x] == T_END:
                return (x,y)
    
    return None

"""
Takes a 2D array of ints and converts it to a 2D array of Nodes.
"""
def init_astar_array(tile_array, endtile_pos=None):
    if not endtile_pos:
        endtile_pos = get_endtile_pos(tile_array)

    end_x = endtile_pos[0]
    end_y = endtile_pos[1]

    arr_size = len(tile_array[0])

    astar_array = []
    for y in range(arr_size):
        astar_yline = []
        for x in range(arr_size):
            # Manhattan distance
            h_cost = abs(end_x - x) + abs(end_y - y)
            node_type = tile_array[y][x]

            new_node = Node(x_pos=x, y_pos=y, h_cost=h_cost, node_type=node_type)

            astar_yline.append(new_node)
            
        astar_array.append(astar_yline)

    return astar_array

def get_neighbour_positions(x_pos, y_pos, max_index):
    neighbour_positions = []

    for y in range(-1, 2):
        for x in range(-1, 2):
            new_x = x_pos + x
            new_y = y_pos + y

            if (new_x >= 0 and new_x <= max_index
                and new_y >= 0 and new_y <= max_index):
                
                move_cost = M_DIAGONAL
                if y == 0 or x == 0:
                    move_cost = M_STRAIGHT

                neighbour_positions.append((new_x, new_y, move_cost))
    
    # Remove current tile itself
    neighbour_positions.remove((x_pos, y_pos, M_STRAIGHT))

    return neighbour_positions

"""
This method finds the shortest path from start to end node.

Every computational step taken by this function will be reflected on the tile array,
hence displayed on the screen.
"""
def astar_algorithm(astar_array, tile_array, start_tile_pos):
    array_size = len(tile_array[0])

    open_list = []
    closed_list = []

    start_tile_x = start_tile_pos[0]
    start_tile_y = start_tile_pos[1]

    start_node = astar_array[start_tile_y][start_tile_x]
    start_node.g_cost = 0
    start_node.calc_f_cost()

    open_list.append(start_node)

    end_node_found = False

    while not end_node_found:
        # Sort open list by f_cost
        open_list.sort(key=lambda node: node.f_cost)

        current_node = open_list.pop(0)

        closed_list.append(current_node)

        if current_node.node_type == T_END:
            end_node_found = True

            return current_node

        # Examine neighbours of current node
        neighbours = get_neighbour_positions(current_node.x_pos, current_node.y_pos, array_size-1)
        for n_x, n_y, move_cost in neighbours:
            n_node = astar_array[n_y][n_x]

            if n_node.node_type == T_BLOCKED or n_node in closed_list:
                continue
            
            # Cost of path to neighbour
            new_n_g_cost = current_node.g_cost + move_cost

            if not n_node in open_list or new_n_g_cost < n_node.g_cost:
                n_node.g_cost = new_n_g_cost
                n_node.calc_f_cost()
                n_node.parent_node = current_node

                if not n_node in open_list:
                    tile_array[n_y][n_x] = T_SEARCH
                    open_list.append(n_node)

        time.sleep(0.005)

        if len(open_list) == 0:
            return None

"""
After finding the end node, this method is used to backtrack the shortest path
to the start node.
"""
def backtrack_path():
    pass

def a_star_search(tile_array, start_tile_pos, end_tile_pos):
    astar_array = init_astar_array(tile_array, end_tile_pos)

    end_node = astar_algorithm(astar_array, tile_array, start_tile_pos)

    return end_node
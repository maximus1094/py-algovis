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

# Tile types
T_EMPTY = 0
T_BLOCKED = 1
T_SEARCH = 2
T_END = 3

class Node:
    def __init__(self, h_cost, node_type):
        self.h_cost = h_cost
        self.g_cost = None
        self.f_cost = None
        self.node_type = node_type
        self.parent_node = None

def get_endtile_pos(arr):
    arr_size = len(arr[0])

    for y in range(arr_size):
        for x in range(arr_size):
            if arr[y][x] == T_END:
                return (x,y)
    
    return None

"""
Takes a 2d array of ints and converts it to a 2d array of Nodes
"""
def init_astar_array(array, endtile_pos=None):
    if not endtile_pos:
        endtile_pos = get_endtile_pos(array)

    end_x = endtile_pos[0]
    end_y = endtile_pos[1]

    arr_size = len(array[0])

    astar_array = []
    for y in range(arr_size):
        astar_yline = []
        for x in range(arr_size):
            h_cost = abs(end_x - x) + abs(end_y - y)
            node_type = array[y][x]

            new_node = Node(h_cost=h_cost, node_type=node_type)

            astar_yline.append(new_node)
            
        astar_array.append(astar_yline)

    return astar_array

"""
This method finds the shortest path from start to end node.

Every computational step taken by this function will be reflected on the field array,
hence displayed on the screen.
"""
def astar_algorithm(arr_astar, arr_field):
    pass

def print_astar(arr):
    for yline in arr:
        arrconv = [x.node_type for x in yline]

        print(arrconv)
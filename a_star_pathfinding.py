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
    def __init__(self, g_cost, h_cost, node_type):
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
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
def init_astar_array(array):
    end_x, end_y = get_endtile_pos(array)

    arr_size = len(array[0])

    astar_array = []
    for y in range(arr_size):
        astar_yline = []
        for x in range(arr_size):
            g_cost = 0
            h_cost = 0 # Need to know the location of end node to compute
            node_type = array[y][x]

            new_node = Node(g_cost=g_cost, h_cost=h_cost, node_type=node_type)

            astar_yline.append(new_node)
            
        astar_array.append(astar_yline)

    return astar_array

def print_astar(arr):
    for yline in arr:
        arrconv = [x.node_type for x in yline]

        print(arrconv)
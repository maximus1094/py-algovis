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

# MOVEMENT TYPES
M_STRAIGHT = 0
M_DIAGONAL = 1

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

            new_node = Node(x_pos=x, y_pos=y, h_cost=h_cost, node_type=node_type)

            astar_yline.append(new_node)
            
        astar_array.append(astar_yline)

    return astar_array

def get_neighbour_positions(x_pos, y_pos, field_size):
    neighbour_positions = []

    for y in range(-1, 2):
        for x in range(-1, 2):
            new_x = x_pos + x
            new_y = y_pos + y

            if (new_x >= 0 and new_x <= field_size-1
                and new_y >= 0 and new_y <= field_size-1):
                
                move_type = M_DIAGONAL
                if y == 0 or x == 0:
                    move_type = M_STRAIGHT

                neighbour_positions.append((new_x, new_y, move_type))
    
    neighbour_positions.remove((x_pos, y_pos, M_STRAIGHT))

    return neighbour_positions

"""
This method finds the shortest path from start to end node.

Every computational step taken by this function will be reflected on the field array,
hence displayed on the screen.
"""
def astar_algorithm(arr_astar, arr_field, start_tile_pos):
    arr_size = len(arr_field[0])

    open_list = []
    closed_list = []

    start_tile_x = start_tile_pos[0]
    start_tile_y = start_tile_pos[1]

    start_node = arr_astar[start_tile_y][start_tile_x]
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
        neighbours = get_neighbour_positions(current_node.x_pos, current_node.y_pos, arr_size)
        for n_x, n_y, move_type in neighbours:
            n_node = arr_astar[n_y][n_x]

            if n_node.node_type == T_BLOCKED or n_node in closed_list:
                continue
            
            # Cost of path to neighbour
            new_n_g_cost = current_node.g_cost
            if move_type == M_DIAGONAL:
                new_n_g_cost += 14
            else:
                new_n_g_cost += 10

            if not n_node in open_list or new_n_g_cost < n_node.g_cost:
                n_node.g_cost = new_n_g_cost
                n_node.calc_f_cost()
                n_node.parent_node = current_node

                if not n_node in open_list:
                    open_list.append(n_node)

        if len(open_list) == 0:
            return None

def print_astar(arr):
    for yline in arr:
        arrconv = [x.node_type for x in yline]

        print(arrconv)
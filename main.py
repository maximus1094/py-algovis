import pygame
import math

from a_star_pathfinding import *

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_dwidth = 600
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Tile types
T_EMPTY = 0
T_BLOCKED = 1
T_SEARCH = 2
T_END = 3

# Colors
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(0, 0, 0)

tile_colors = {
    T_EMPTY: pygame.Color(204, 201, 220), # Bright grey ccc9dc
    T_BLOCKED: pygame.Color(74, 25, 66), # Purple 4a1942
    T_SEARCH: pygame.Color(199, 239, 0), # Bright yellow c7ef00
    T_END: pygame.Color(68, 68, 68) # Dark grey 434440 
}

font = pygame.font.SysFont(None, 22)

# Objects (Move to a better place later)
# Field = 40 * 40 tiles
# Tile Codes
# 0 = regular unused tile
field = [[0] * 40 for _ in range(40)]

tile_width = 10
tile_height = 10

field_width = tile_width * 40
field_height = tile_height * 40

field_start_x = (m_dwidth - field_width) / 2
field_start_y = 125

# Functions
def draw_field():
    tile_padding_x = 1
    tile_padding_y = 1

    tile_offset_x = 0
    tile_offset_y = 0

    y_range = range(len(field))
    x_range = range(len(field[0]))
    for y in y_range:
        for x in x_range:
            tile_rect = [field_start_x + tile_offset_x, field_start_y + tile_offset_y, tile_width-tile_padding_x, tile_height-tile_padding_y]
            
            tile_color = tile_colors[field[y][x]]
            pygame.draw.rect(m_display, tile_color, tile_rect)

            tile_offset_x += tile_width

        tile_offset_x = 0
        tile_offset_y += tile_height

def print_field():
    for line in field:
        print(line)

def mouse_pos_to_field_index(mouse_x, mouse_y):
    tile_x_index = math.floor((mouse_x - field_start_x) / tile_width)
    tile_y_index = math.floor((mouse_y - field_start_y) / tile_height)

    return (tile_x_index, tile_y_index)

def change_tile(x, y, new_type):
    # Only empty tiles are allowed to be converted
    if field[y][x] == T_EMPTY:
        field[y][x] = new_type

def draw_text(text, position, color):
    text_on_screen = font.render(text, True, color)
    m_display.blit(text_on_screen, position)

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

start_tile_placed = False
end_tile_placed = False
end_tile_pos = None
placing_tile = False

astar_array = None

while not m_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_quit = True
            break

        # For the moment, using keys to start A STAR ALGO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                astar_array = init_astar_array(field, end_tile_pos)
                
                print('A STAR array generated.')
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if within field bounds            
            if (mouse_x >= field_start_x and mouse_x <= field_start_x + field_width
                and mouse_y >= field_start_y and mouse_y <= field_start_y + field_height):
                
                # Get clicked tile
                tile_x_index, tile_y_index = mouse_pos_to_field_index(mouse_x, mouse_y)

                # Setting up field before search begins
                tile_type = T_EMPTY
                if not start_tile_placed:
                    placing_tile = True
                    tile_type = T_SEARCH
                    start_tile_placed = True
                elif not end_tile_placed:
                    placing_tile = True
                    tile_type = T_END
                    end_tile_placed = True

                    end_tile_pos = (tile_x_index, tile_y_index)
                else:
                    # Just for testing
                    if astar_array:
                        node = astar_array[tile_y_index][tile_x_index]
                        print(f'Tile H cost: {node.h_cost}')

                change_tile(tile_x_index, tile_y_index, tile_type)
            else:
                # Check for button clicks etc.
                print('Clicked outside the field!')

        elif event.type == pygame.MOUSEBUTTONUP:
            placing_tile = False

        if pygame.mouse.get_pressed()[0] and not placing_tile:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if within field bounds            
            if (mouse_x >= field_start_x and mouse_x <= field_start_x + field_width
                and mouse_y >= field_start_y and mouse_y <= field_start_y + field_height):
            
                tile_x_index, tile_y_index = mouse_pos_to_field_index(mouse_x, mouse_y)
                
                if start_tile_placed and end_tile_placed:
                    change_tile(tile_x_index, tile_y_index, T_BLOCKED)

    # Clear display
    m_display.fill(c_white)

    # Draw on display
    draw_field()

    if not start_tile_placed:
        draw_text('Click to place starting point.', [field_start_x, field_start_y * (3/4)], c_black)
    elif not end_tile_placed:
        draw_text('Click to place end point.', [field_start_x, field_start_y * (3/4)], c_black)
    else:
        draw_text('Drag to place barriers.', [field_start_x, field_start_y * (3/4)], c_black)

    # Update display
    pygame.display.update()

    m_clock.tick(m_fps)

# Exit
pygame.quit()
quit()
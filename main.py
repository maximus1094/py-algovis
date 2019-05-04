import pygame
import math

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_dwidth = 600
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Tile types
T_NORMAL = 0
T_BLOCKED = 1
T_START = 2
T_END = 3

# Colours
c_white = pygame.Color(255, 255, 255)

c_black = pygame.Color(0, 0, 0)
c_red = pygame.Color(255, 0, 0)
c_green = pygame.Color(0, 255, 0)
c_blue = pygame.Color(0, 0, 255)


tile_colors = {
    T_NORMAL: c_black,
    T_BLOCKED: c_blue,
    T_START: c_green,
    T_END: c_red
}

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

def convert_tile(x, y, new_type):
    field[y][x] = new_type

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

start_tile_placed = False
end_tile_placed = False

while not m_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_quit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if within field bounds            
            if (mouse_x >= field_start_x and mouse_x <= field_start_x + field_width
                and mouse_y >= field_start_y and mouse_y <= field_start_y + field_height):
                
                # Get clicked tile
                tile_x_index = math.floor((mouse_x - field_start_x) / tile_width)
                tile_y_index = math.floor((mouse_y - field_start_y) / tile_height)

                # Setting up field before search begins
                tile_type = T_BLOCKED
                if not start_tile_placed:
                    tile_type = T_START
                    start_tile_placed = True
                elif not end_tile_placed:
                    tile_type = T_END
                    end_tile_placed = True

                convert_tile(tile_x_index, tile_y_index, tile_type)
            else:
                # Check for button clicks etc.
                print('Clicked outside the field!')

    # Clear display
    m_display.fill(c_white)

    # Draw on display
    draw_field()

    # Update display
    pygame.display.update()

    m_clock.tick(m_fps)

# Exit
pygame.quit()
quit()
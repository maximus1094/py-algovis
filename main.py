import pygame
import math

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_dwidth = 600
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Colours
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(0, 0, 0)

# Objects (Move to a better place later)
# Field = 40 * 40 tiles
# Tile Codes
# 0 = regular unused tile
field = [0] * 40
field = [field] * 40

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

    for yline in field:
        for x in yline:
            tile = [field_start_x + tile_offset_x, field_start_y + tile_offset_y, tile_width-tile_padding_x, tile_height-tile_padding_y]
            
            pygame.draw.rect(m_display, c_black, tile)

            tile_offset_x += tile_width

        tile_offset_x = 0
        tile_offset_y += tile_height

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

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

                print(f'Tile index: {tile_x_index, tile_y_index}')
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
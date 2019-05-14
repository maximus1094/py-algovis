import pygame
import math

from field import *
from a_star_pathfinding import *

# Pygame stuff
pygame.init()
pygame.display.set_caption('A-Star Pathfinding')

m_dwidth = 600
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Colors
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(0, 0, 0)

font = pygame.font.SysFont(None, 22)

# Field
field = Field(m_dwidth)

helper_text_pos = [field.field_start_x, field.field_start_y * (3/4)]

def draw_text(text, position, color):
    text_on_screen = font.render(text, True, color)
    m_display.blit(text_on_screen, position)

def draw_helper_text():
    if not field.start_tile_placed:
        draw_text('Click to place starting point.', helper_text_pos, c_black)
    elif not field.end_tile_placed:
        draw_text('Click to place end point.', helper_text_pos, c_black)
    else:
        draw_text('Drag to place barriers.', helper_text_pos, c_black)

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

placement_mode = True # If False, tiles cannot be placed
placing_tile = False

while not m_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_quit = True
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                placement_mode = False

                run_search(field.tile_array, field.start_tile_pos, field.end_tile_pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if within field bounds            
            if field.coord_in_field(mouse_x, mouse_y):
                tile_x_index, tile_y_index = field.get_tile_index(mouse_x, mouse_y)

                if placement_mode:
                    tile_type = T_EMPTY
                    if not field.start_tile_placed:
                        placing_tile = True
                        field.place_start_tile(tile_x_index, tile_y_index)
                        
                    elif not field.end_tile_placed:
                        placing_tile = True
                        field.place_end_tile(tile_x_index, tile_y_index)
                    
                else:
                    # Do something after the tiles have been placed.
                    pass

        elif event.type == pygame.MOUSEBUTTONUP:
            placing_tile = False

        if pygame.mouse.get_pressed()[0] and not placing_tile:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if within field bounds            
            if field.coord_in_field(mouse_x, mouse_y):
                tile_x_index, tile_y_index = field.get_tile_index(mouse_x, mouse_y)
                
                if field.start_tile_placed and field.end_tile_placed:
                    field.place_tile(tile_x_index, tile_y_index, T_BLOCKED)

    # Clear display
    m_display.fill(c_white)

    # Draw on display
    field.draw_field(m_display)

    draw_helper_text()

    # Update display
    pygame.display.update()

    m_clock.tick(m_fps)

# Exit
pygame.quit()
quit()
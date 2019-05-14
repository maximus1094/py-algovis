import pygame
import math

""" CONSTANTS """
# TILE TYPES
T_EMPTY = 0
T_BLOCKED = 1
T_SEARCH = 2
T_END = 3

TILE_COLORS = {
    T_EMPTY: pygame.Color(204, 201, 220), # Bright grey ccc9dc
    T_BLOCKED: pygame.Color(74, 25, 66), # Purple 4a1942
    T_SEARCH: pygame.Color(199, 239, 0), # Bright yellow c7ef00
    T_END: pygame.Color(68, 68, 68) # Dark grey 434440 
}

TILE_WIDTH = 10
TILE_HEIGHT = 10

NUM_TILES = 40

# FIELD = 40 * 40 TILES
FIELD_WIDTH = TILE_WIDTH * NUM_TILES
FIELD_HEIGHT = TILE_HEIGHT * NUM_TILES

class Field():

    def __init__(self, m_dwidth):
        self.field_start_x = (m_dwidth - FIELD_WIDTH) / 2
        self.field_start_y = 125
        self.tile_array = [[0] * NUM_TILES for _ in range(NUM_TILES)]
        self.start_tile_placed = False
        self.start_tile_pos = None
        self.end_tile_placed = False
        self.end_tile_pos = None

    def get_tile_index(self, x, y):
        tile_x_index = math.floor((x - self.field_start_x) / TILE_WIDTH)
        tile_y_index = math.floor((y - self.field_start_y) / TILE_HEIGHT)

        return (tile_x_index, tile_y_index)

    def coord_in_field(self, x, y):
        if (x >= self.field_start_x and x <= self.field_start_x + FIELD_WIDTH
            and y >= self.field_start_y and y <= self.field_start_y + FIELD_HEIGHT):

            return True
        return False  

    def place_tile(self, x_index, y_index, new_type):
        # Only empty tiles are allowed to be converted
        if self.tile_array[y_index][x_index] == T_EMPTY:
            self.tile_array[y_index][x_index] = new_type

    def place_start_tile(self, x_index, y_index):
        self.place_tile(x_index, y_index, T_SEARCH)
        self.start_tile_pos = (x_index, y_index)
        self.start_tile_placed = True
    
    def place_end_tile(self, x_index, y_index):
        self.place_tile(x_index, y_index, T_END)
        self.end_tile_pos = (x_index, y_index)
        self.end_tile_placed = True

    def draw_field(self, m_display):
        tile_padding_x = 1
        tile_padding_y = 1

        tile_offset_x = 0
        tile_offset_y = 0

        y_range = range(NUM_TILES)
        x_range = range(NUM_TILES)
        for y in y_range:
            for x in x_range:
                tile_rect = [self.field_start_x + tile_offset_x, self.field_start_y + tile_offset_y, TILE_WIDTH-tile_padding_x, TILE_HEIGHT-tile_padding_y]
                
                tile_color = TILE_COLORS[self.tile_array[y][x]]
                pygame.draw.rect(m_display, tile_color, tile_rect)

                tile_offset_x += TILE_WIDTH

            tile_offset_x = 0
            tile_offset_y += TILE_HEIGHT

    
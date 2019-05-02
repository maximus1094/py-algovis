import pygame

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_dwidth = 600
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Colours
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(0, 0, 0)

# Functions
def draw_field():
    # Field = 40 * 40 tiles
    # Tile Codes
    # 0 = regular unused tile
    field = [0] * 40
    field = [field] * 40

    tile_offset_x = 0
    tile_offset_y = 0
    tile_width = 10
    tile_height = 10

    space_x = 1
    space_y = 1

    field_width = tile_width * 40 + space_x * 39
    field_height = tile_height * 40 + space_y * 39

    field_start_x = (m_dwidth - field_width) / 2
    field_start_y = 125

    for yline in field:
        for x in yline:
            tile = [field_start_x + tile_offset_x, field_start_y + tile_offset_y, tile_width, tile_height]
            
            pygame.draw.rect(m_display, c_black, tile)

            tile_offset_x += tile_width + space_x

        tile_offset_x = 0
        tile_offset_y += tile_height + space_y

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

while not m_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_quit = True

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
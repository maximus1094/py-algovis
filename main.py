import pygame

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_dwidth = 800
m_dheight = 600
m_display = pygame.display.set_mode((m_dwidth, m_dheight))

# Colours
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(0, 0, 0)

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
    pygame.draw.rect(m_display, c_black, [m_dwidth/2, m_dheight/2, 30, 30])

    # Update display
    pygame.display.update()

    m_clock.tick(m_fps)

# Exit
pygame.quit()
quit()
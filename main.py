import pygame

# Start
pygame.init()
pygame.display.set_caption('Application Title')

m_display = pygame.display.set_mode((800, 600))

# Main loop
m_fps = 30
m_clock = pygame.time.Clock()
m_quit = False

while not m_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_quit = True
    
    m_clock.tick(m_fps)

# Exit
pygame.quit()
quit()
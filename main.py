import pygame

pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Pinky in Space")

icon = pygame.image.load('Images/space-pig_icon.png')
pygame.display.set_icon(icon)


# Game Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Change screen color = RGB
    screen.fill((0,0,0))
    pygame.display.update() # Update the display.
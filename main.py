import pygame

pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Pinky in Space")

icon = pygame.image.load('Images\space-pig_icon.png')
pygame.display.set_icon(icon)

# Add Player
playerIMG = pygame.image.load('Images\pig_spaceship_Player.png')
playerIMG = pygame.transform.scale(playerIMG, (125,75))

# Player coordinates
playerX = 340
playerY = 480

def player():
    # Screen.blit() draws the image of the player.
    screen.blit(playerIMG,(playerX,playerY))

# Game Loop
running = True
while running:
    
    # Change screen color = RGB
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call the player
    player()
    pygame.display.update() # Update the display.


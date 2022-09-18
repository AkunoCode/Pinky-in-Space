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
playerIMG = pygame.transform.scale(playerIMG, (125,75)) # Resize the image

# Player default coordinates related to screen size (x = 800, y = 600)
playerX = 340
playerY = 480
# Change in coordinate
playerX_change = 0


# Add Enemy
enemyIMG = pygame.image.load('Images\monster_Enemy.png')
enemyIMG = pygame.transform.scale(enemyIMG, (100,75)) # Resize the image

# Enemy default coordinates related to screen size (x = 800, y = 600)
enemyX = 350
enemyY = 50
# Change in coordinate
enemyX_change = 0

def player(x,y): # takes x and y as parameter to change position
    # Screen.blit() draws the image of the enemy.
    screen.blit(playerIMG,(x,y))

def enemy(x,y): # takes x and y as parameter to change position
    # Screen.blit() draws the image of the enemy.
    screen.blit(enemyIMG,(x,y))

# Game Loop
running = True
while running:
    
    # Change screen color = RGB
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # To check if keystroke is pressed and whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = - 0.2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.2
        # To check if keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.0

    # Move by change
    playerX += playerX_change

    # Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 675: # 675 because the player image is 125width (800 - 125 = 675)
        playerX = 675

    # Call the player
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() # Update the display.


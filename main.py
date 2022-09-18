from math import sqrt
import random
import pygame

pygame.init()

# Create the screen ----------------------------------------
screen = pygame.display.set_mode((800,600))

# Title and Icon -------------------------------------------
pygame.display.set_caption("Pinky in Space")
icon = pygame.image.load('Images\space-pig_icon.png')
pygame.display.set_icon(icon)

# Background ----------------------------------------------
background = pygame.image.load('Images\space_Background.jpg')
background = pygame.transform.scale(background, (800,600))

# Add Player -----------------------------------------------
playerIMG = pygame.image.load('Images\pig_spaceship_Player.png')
playerIMG = pygame.transform.scale(playerIMG, (125,75)) # Resize the image

# Player default coordinates related to screen size (x = 800, y = 600)
playerX = 340
playerY = 480

# Change in coordinate
playerX_change = 0

# Add Enemy -----------------------------------------------------------------------
enemyIMG = pygame.image.load('Images\monster_Enemy.png')
enemyIMG = pygame.transform.scale(enemyIMG, (75,60)) # Resize the image

# Enemy default coordinates related to screen size (x = 800, y = 600)
enemyX = random.randint(0,700)
enemyY = random.randint(50,150)

# Change in coordinate
enemyX_change = 0.2
enemyY_change = 15

# Add Bullet -----------------------------------------------------------------------
bulletIMG = pygame.image.load('Images/bacon_Bullet.png')
bulletIMG = pygame.transform.scale(bulletIMG, (25,50)) # Resize the image

# Enemy default coordinates related to screen size (x = 800, y = 600)
bulletX = 0
bulletY = 480

# Change in coordinate
bulletX_change = 0.2
bulletY_change = 0.5
bullet_state = "ready" # ready means you can't see the bullet and fire is the opposite

score = 0

# Functions -----------------------------------------------------------------------
def player(x,y): # takes x and y as parameter to change position
    # Screen.blit() draws the image of the enemy.
    screen.blit(playerIMG,(x,y))

def enemy(x,y): # takes x and y as parameter to change position
    # Screen.blit() draws the image of the enemy.
    screen.blit(enemyIMG,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG,(x + 50, y + 10))

def isCollision(enemyY, enemyX, bulletY, bulletX):
    distance = sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
    if distance < 40:
        return True
    else:
        return False


# Game Loop ------------------------------------------------------------------------
running = True
while running:
    
    # Change screen color = RGB
    screen.fill((0,0,0))
    # Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # To check if keystroke is pressed and whether its right or left or space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = - 0.3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                # checks first if the bullet is not in fired state.
                if bullet_state == "ready":
                    # gets the current x-axis coordinate and assigns to bulletx
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # To check if keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.0

    # Movement and Boundaries for player ---------------------------------------------------------
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 675: # 675 because the player image is 125width (800 - 125 = 675)
        playerX = 675

    # Movement and Boundaries for enemy ----------------------------------------------------------
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 700: # 675 because the player image is 125width (800 - 125 = 675)
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Bullet Movement -----------------------------------------------------------------------
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    # Collision
    collision = isCollision(enemyY,enemyX,bulletY,bulletX)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0,700)
        enemyY = random.randint(50,150) 
        print(score)


    # Call the player and enemies -------------------------------------------------------------------
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() # Update the display.


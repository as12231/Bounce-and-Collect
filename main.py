import pygame
import sys
from player import Player
from game_platform import Platform
from obstacle import Obstacle
from coin import Coin
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Adventure Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

# Player instance
player = Player(100, SCREEN_HEIGHT - 150)

# Platform instances
platforms = [
    Platform(100, SCREEN_HEIGHT - 50, 200, 20),
    Platform(400, SCREEN_HEIGHT - 150, 200, 20),
    Platform(700, SCREEN_HEIGHT - 250, 200, 20),
]

# Coin instances (yellow balls)
coins = [Coin(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 200)) for _ in range(5)]

# Obstacle instances (red dots)
obstacles = [
    Obstacle(random.randint(200, 600), SCREEN_HEIGHT - 150, 20, 20),
    Obstacle(random.randint(200, 600), SCREEN_HEIGHT - 200, 20, 20),
]

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player updates
    player.update(platforms)

    # Check if player falls off the screen
    if player.rect.y > SCREEN_HEIGHT:
        print("Game Over! Final Score:", score)
        running = False

    # Prevent player from going out of bounds
    if player.rect.x < 0:
        player.rect.x = 0  # Keep player inside the left boundary
    if player.rect.x > SCREEN_WIDTH - player.rect.width:
        player.rect.x = SCREEN_WIDTH - player.rect.width  # Keep player inside the right boundary

    player.draw(screen)  # Draw the player

    # Platform updates
    for platform in platforms:
        platform.draw(screen)

    # Obstacle updates
    for obstacle in obstacles:
        obstacle.draw(screen)
        if player.rect.colliderect(obstacle.rect):
            print("Game Over! Final Score:", score)
            running = False

    # Coin collection (only for yellow coins)
    for coin in coins[:]:  # Use a copy of the list to avoid modifying it during iteration
        if player.rect.colliderect(coin.rect):
            score += 5  # Increase score by 5 when the blue hits the yellow coin
            coins.remove(coin)  # Remove the coin once collected
        else:
            coin.draw(screen)

    # Score display
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()

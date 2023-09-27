import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
TRAIL_LENGTH = 10  # Adjust the trail length as needed
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PLAYER1_COLOR = (255, 0, 0)  # Red for Player 1
PLAYER2_COLOR = (0, 0, 255)  # Blue for Player 2

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Racing Game")

# Player positions and trail history
player1_x, player1_y = 50, HEIGHT // 2
player2_x, player2_y = WIDTH - 50, HEIGHT // 2
player1_trail = []
player2_trail = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5
    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5

    # Add the current player positions to their respective trail
    player1_trail.append((player1_x, player1_y))
    player2_trail.append((player2_x, player2_y))

    # Trim the trails to the specified length
    if len(player1_trail) > TRAIL_LENGTH:
        player1_trail.pop(0)
    if len(player2_trail) > TRAIL_LENGTH:
        player2_trail.pop(0)

    # Check if players have reached the center
    if abs(player1_x - WIDTH // 2) < PLAYER_SIZE and abs(player1_y - HEIGHT // 2) < PLAYER_SIZE:
        print("Player 1 wins!")
        running = False
    elif abs(player2_x - WIDTH // 2) < PLAYER_SIZE and abs(player2_y - HEIGHT // 2) < PLAYER_SIZE:
        print("Player 2 wins!")
        running = False

    # Draw the maze (simplified here)
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 5, 0, 10, HEIGHT))  # Maze center
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 10)  # Center point

    # Draw the player trails
    for pos in player1_trail:
        pygame.draw.rect(screen, PLAYER1_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))
    for pos in player2_trail:
        pygame.draw.rect(screen, PLAYER2_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()

# Quit Pygame
pygame.quit()

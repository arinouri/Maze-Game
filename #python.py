#python

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Racing Game")

# Player positions
player1_x, player1_y = 50, HEIGHT // 2
player2_x, player2_y = WIDTH - 50, HEIGHT // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movements (you can implement more precise controls)
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
    pygame.draw.rect(screen, (255, 0, 0), (player1_x, player1_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, (0, 0, 255), (player2_x, player2_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.display.update()

# Quit Pygame
pygame.quit()
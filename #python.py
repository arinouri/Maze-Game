import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PLAYER_SIZE = 20
TRAIL_LENGTH = 10
PLAYER1_COLOR = (255, 0, 0)  # Red for Player 1
PLAYER2_COLOR = (0, 0, 255)  # Blue for Player 2

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Racing Game")

# Generate the maze using Recursive Backtracking algorithm
def generate_maze():
    grid = [[True] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    def recursive_backtracking(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT and grid[new_y][new_x]:
                grid[new_y][new_x] = False
                grid[y + dy // 2][x + dx // 2] = False
                recursive_backtracking(new_x, new_y)

    recursive_backtracking(0, 0)
    return grid

maze = generate_maze()

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
    if keys[pygame.K_w] and player1_y > 0 and not maze[player1_y // CELL_SIZE - 1][player1_x // CELL_SIZE]:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < HEIGHT - PLAYER_SIZE and not maze[player1_y // CELL_SIZE + 1][player1_x // CELL_SIZE]:
        player1_y += 5
    if keys[pygame.K_a] and player1_x > 0 and not maze[player1_y // CELL_SIZE][player1_x // CELL_SIZE - 1]:
        player1_x -= 5
    if keys[pygame.K_d] and player1_x < WIDTH - PLAYER_SIZE and not maze[player1_y // CELL_SIZE][player1_x // CELL_SIZE + 1]:
        player1_x += 5
    if keys[pygame.K_UP] and player2_y > 0 and not maze[player2_y // CELL_SIZE - 1][player2_x // CELL_SIZE]:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PLAYER_SIZE and not maze[player2_y // CELL_SIZE + 1][player2_x // CELL_SIZE]:
        player2_y += 5
    if keys[pygame.K_LEFT] and player2_x > 0 and not maze[player2_y // CELL_SIZE][player2_x // CELL_SIZE - 1]:
        player2_x -= 5
    if keys[pygame.K_RIGHT] and player2_x < WIDTH - PLAYER_SIZE and not maze[player2_y // CELL_SIZE][player2_x // CELL_SIZE + 1]:
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

    # Draw the maze
    screen.fill(WHITE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if maze[y][x]:
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 10)  # Center point

    # Draw the player trails
    for pos in player1_trail:
        pygame.draw.rect(screen, PLAYER1_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))
    for pos in player2_trail:
        pygame.draw.rect(screen, PLAYER2_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()

# Quit Pygame
pygame.quit()
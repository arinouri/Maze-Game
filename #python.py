import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 30  # Increased cell size for player movement
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
PLAYER_SIZE = 20
TRAIL_LENGTH = 10
PLAYER1_COLOR = (255, 0, 0)  # Red for Player 1
PLAYER2_COLOR = (0, 0, 255)  # Blue for Player 2
CENTER_COLOR = (255, 215, 0)  # Gold color for the center point

# Color palette
COLORS = [
    (44, 44, 84),   # dark indigo
    (71, 71, 135),  # deep purple-gray
    (170, 171, 184),  # cool gray
    (236, 236, 236),  # light gray
    (40, 54, 24),  # dark green-gray
    (183, 183, 164),  # light gray-green
    (212, 212, 212),  # soft gray
    (240, 239, 235),  # off-white
    (228, 228, 222),  # ethereal ivory
    (196, 197, 186),  # sophisticated sage
    (27, 27, 27),   # timeless noir
    (89, 95, 57)    # muted moss
]

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

# Randomly select colors for the maze walls and background
background_color = random.choice(COLORS)
wall_color = random.choice(COLORS)

# Randomly select a starting position for both players
player_start_x = random.randint(1, GRID_WIDTH - 2) * CELL_SIZE
player_start_y = random.randint(1, GRID_HEIGHT - 2) * CELL_SIZE

# Find a valid position for the center point (not inside a wall and not where the players start)
center_x, center_y = player_start_x, player_start_y
while maze[center_y // CELL_SIZE][center_x // CELL_SIZE] or (center_x == player_start_x and center_y == player_start_y):
    center_x = random.randint(1, GRID_WIDTH - 2) * CELL_SIZE
    center_y = random.randint(1, GRID_HEIGHT - 2) * CELL_SIZE

# Player positions and trail history
player1_x, player1_y = player_start_x, player_start_y
player2_x, player2_y = player_start_x, player_start_y
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
    if abs(player1_x - center_x) < PLAYER_SIZE and abs(player1_y - center_y) < PLAYER_SIZE:
        print("Player 1 wins!")
        running = False
    elif abs(player2_x - center_x) < PLAYER_SIZE and abs(player2_y - center_y) < PLAYER_SIZE:
        print("Player 2 wins!")
        running = False

    # Draw the maze with random colors
    screen.fill(background_color)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if maze[y][x]:
                pygame.draw.rect(screen, wall_color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the center point
    pygame.draw.circle(screen, CENTER_COLOR, (center_x + CELL_SIZE // 2, center_y + CELL_SIZE // 2), CELL_SIZE // 4)

    # Draw the player trails
    for pos in player1_trail:
        pygame.draw.rect(screen, PLAYER1_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))
    for pos in player2_trail:
        pygame.draw.rect(screen, PLAYER2_COLOR, (*pos, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()

# Quit Pygame
pygame.quit()

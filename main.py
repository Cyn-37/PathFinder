import pygame
import sys
import math
from queue import PriorityQueue

# RGB Colors
WHITE = (220, 220, 220)  # normal path
RED = (255, 100, 100)    # path with cost = 5
BLACK = (60, 60, 60)     # cost = infinity
GREEN = (100, 255, 100)  # start
BLUE = (100, 100, 255)   # end
GRAY = (200, 200, 200)   # cell borders
PURPLE = (180, 100, 180) # a* path
DARK_GRAY = (150, 150, 150)  # button color
LIGHT_GRAY = (180, 180, 180)  # button hover color

# Costs
COST_WHITE = 1
COST_RED = 5
COST_BLACK = float('inf')

# Pygame
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 35, 35
CELL_SIZE = WIDTH // COLS
BUTTON_HEIGHT = 30  

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder Grid")

# Grid and start/end points
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start = None
end = None

# Function to draw the grid
def draw_grid(win, grid, start, end, path):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:  
                color = WHITE
            elif grid[row][col] == 1:  
                color = BLACK
            elif grid[row][col] == 2:  
                color = RED
            
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE + BUTTON_HEIGHT, CELL_SIZE, CELL_SIZE))  # cell color
            pygame.draw.rect(win, GRAY, (col * CELL_SIZE, row * CELL_SIZE + BUTTON_HEIGHT, CELL_SIZE, CELL_SIZE), 1)  # border color

    if start:
        row, col = start
        pygame.draw.rect(win, GREEN, (col * CELL_SIZE, row * CELL_SIZE + BUTTON_HEIGHT, CELL_SIZE, CELL_SIZE))

    if end:
        row, col = end
        pygame.draw.rect(win, BLUE, (col * CELL_SIZE, row * CELL_SIZE + BUTTON_HEIGHT, CELL_SIZE, CELL_SIZE))

    if path:
        for (row, col) in path:
            pygame.draw.rect(win, PURPLE, (col * CELL_SIZE, row * CELL_SIZE + BUTTON_HEIGHT, CELL_SIZE, CELL_SIZE))

# Get clicked position on grid
def get_clicked_pos(pos):
    x, y = pos
    row = (y - BUTTON_HEIGHT) // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

# Manhattan distance heuristic
def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# A* algorithm
def a_star_algorithm(grid, start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[1]
        open_set_hash.remove(current)

        if current == end:
            path = []
            total_cost = 0
            while current in came_from:
                path.append(current)
                row, col = current
                total_cost += COST_RED if grid[row][col] == 2 else COST_WHITE
                current = came_from[current]
            path.reverse()
            return path, total_cost

        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            row, col = neighbor
            if grid[row][col] == 1:
                continue

            temp_g_score = g_score[current] + (COST_RED if grid[row][col] == 2 else COST_WHITE)

            if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, end)

                if neighbor not in open_set_hash:
                    open_set.put((f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)

    return None, 0

# Get valid neighbors
def get_neighbors(pos):
    row, col = pos
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < ROWS - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < COLS - 1:
        neighbors.append((row, col + 1))
    return neighbors

def show_info():
    info_surface = pygame.Surface((WIDTH - 40, 200))
    info_surface.fill(WHITE)
    font = pygame.font.SysFont('Arial', 20)
    lines = [
        "This is a pathfinding visualizer using the A* algorithm.",
        "Left Click: Change cell type (normal, obstacle, or cost).",
        "Right Click: Set start and end points.",
        "The algorithm will find the shortest path and display the total cost."
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))
        info_surface.blit(text, (10, 10 + i * 30))

    return info_surface

def main():
    global start, end

    # Dictionary for cycling through cell states
    cell_cycle = {0: 1, 1: 2, 2: 0}
    show_info_window = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Left click: Change cell type
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                # Check if the clicked position is within the grid bounds
                if 0 <= row < ROWS and 0 <= col < COLS:
                    # Change cell type using the dictionary
                    grid[row][col] = cell_cycle[grid[row][col]]

                # Check if the button is clicked
                if BUTTON_HEIGHT > pos[1] > 0 and (WIDTH // 2 - 50 < pos[0] < WIDTH // 2 + 50):
                    show_info_window = not show_info_window

            # Right click: Select start and end points
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                # Check if the clicked position is within the grid bounds
                if 0 <= row < ROWS and 0 <= col < COLS:
                    if not start:
                        start = (row, col)
                    elif (row, col) == start:
                        start = None
                    elif not end and (row, col) != start:
                        end = (row, col)
                    elif (row, col) == end:
                        end = None
                    else:
                        end = (row, col)

        win.fill(WHITE)

        # Draw button
        button_rect = pygame.Rect(WIDTH // 2 - 50, 5, 100, BUTTON_HEIGHT)
        pygame.draw.rect(win, DARK_GRAY, button_rect)
        font = pygame.font.SysFont('Arial', 20)
        button_text = font.render('Show Info', True, (255, 255, 255))
        win.blit(button_text, (button_rect.x + 10, button_rect.y + 5))

        # Run A* if start and end points are set
        path = None
        total_cost = 0
        if start and end:
            path, total_cost = a_star_algorithm(grid, start, end)

        draw_grid(win, grid, start, end, path)

        # Display total cost
        text_cost = font.render(f'Total Cost: {total_cost}', True, (0, 0, 0))
        win.blit(text_cost, (10, 10))

        # Show information window if needed
        if show_info_window:
            info_surface = show_info()
            win.blit(info_surface, (20, BUTTON_HEIGHT + 10))

        pygame.display.update()

if __name__ == "__main__":
    main()

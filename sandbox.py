import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 10
FPS_CLOCK = pygame.time.Clock()


cell_size = 20
display_x = 41*cell_size + cell_size/2
display_y = 25*cell_size + cell_size/2

center_x = display_x / 2
center_y = display_y / 2

DISPLAY_SURF = pygame.display.set_mode((display_x, display_y), 0, 32)

pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
BLACK = (0,   0,   0)
PALETTE_BLUE_1 = (0,  45, 124)
PALETTE_BLUE_2 = (3,  30,  73)
PALETTE_YELLOW = (255, 203,   0)
PALETTE_ORANGE = (249,  79,  13)
PALETTE_RED = (224,   8,  15)


class Boxy(object):
    """The main character of this great adventure"""
    def __init__(self, nr_cells=1, cells_centers=[[center_y, center_x]],
                 direction='left', cells_size=20):
        self.nr_cells = nr_cells
        self.cells_centers = cells_centers
        self.direction = direction
        self.cells_size = cells_size

    # Implement adding and removing elements as a Queue

    def draw_all_cells(self):
        for i in range(len(self.cells_centers)):
            pygame.draw.rect(DISPLAY_SURF, PALETTE_YELLOW, (self.cells_centers[i][1] - self.cells_size/2,
                                                   self.cells_centers[i][0] - self.cells_size/2,
                                                   self.cells_size, self.cells_size))

    def push_cell(self, coords_new_cell):
        self.nr_cells = self.nr_cells + 1
        self.cells_centers.append(coords_new_cell)

    def pop_cell(self):
        self.nr_cells = self.nr_cells - 1
        self.cells_centers = self.cells_centers[:][1:]

    def move(self):
        if self.direction == 'left':
            # Add new element with the center on the left of the last element
            self.push_cell([self.cells_centers[-1][0],
                           self.cells_centers[-1][1] - self.cells_size])

        if self.direction == 'right':
            # Add new element with the center on the left of the last element
            self.push_cell([self.cells_centers[-1][0],
                           self.cells_centers[-1][1] + self.cells_size])

        if self.direction == 'up':
            # Add new element with the center on the left of the last element
            self.push_cell([self.cells_centers[-1][0] - self.cells_size,
                           self.cells_centers[-1][1]])

        if self.direction == 'down':
            # Add new element with the center on the left of the last element
            self.push_cell([self.cells_centers[-1][0] + self.cells_size,
                           self.cells_centers[-1][1]])

        if self.nr_cells > 2:
            if self.cells_centers[-1][:] == self.cells_centers[-3][:]:
                self.invert_direction()
                self.move()

        # Manage the length of the snake
        if self.nr_cells > 3:
            self.pop_cell()

        # Draw the whole snake
        self.draw_all_cells()

    def invert_direction(self):
        self.cells_centers = self.cells_centers[::-1]

        # To add:
        # - new snake if it touches itself
        # - going to the other side if it touches the border
        # - remove the gap between the snake and the border
        # - growing when eating an apple
        # - adding the "head" to the snake
        # - using the head definition to define the movement to the opposite direction


snake = Boxy()
apples_positions =[[center_x, center_y], [center_x + 2*snake.cells_size, center_y + 2*snake.cells_size]]

while True:  # main game loop
    DISPLAY_SURF.fill(PALETTE_BLUE_1)

    for i in range(len(apples_positions)):
        pygame.draw.rect(DISPLAY_SURF, PALETTE_RED, (apples_positions[i][1] - snake.cells_size / 2,
                                               apples_positions[i][0] - snake.cells_size / 2,
                                               snake.cells_size, snake.cells_size))

    snake.draw_all_cells()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)

    # Changing direction based on buttonpress
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_LEFT:
            snake.direction = 'left'
            snake.move()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            snake.direction = 'right'
            snake.move()

        if event.type == KEYDOWN and event.key == K_UP:
            snake.direction = 'up'
            snake.move()

        if event.type == KEYDOWN and event.key == K_DOWN:
            snake.direction = 'down'
            snake.move()



    # snake.move()  # Always moving

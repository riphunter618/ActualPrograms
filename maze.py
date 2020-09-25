import pygame
import random
import time

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
w = 20
grid = []
visited = []
stack = []
solution = {}


def build_grid(y1, w1):
    for i in range(1, 21):
        x1 = 0
        y1 = y1 + 20
        for j in range(1, 21):
            pygame.draw.line(screen, BLACK, [x1, y1], [x1 + w1, y1], 5)
            pygame.draw.line(screen, BLACK, [x1 + w1, y1], [x1 + w1, y1 + w1], 5)
            pygame.draw.line(screen, BLACK, [x1 + w1, y1 + w1], [x1, y1 + w1], 5)
            pygame.draw.line(screen, BLACK, [x1, y1 + w1], [x1, y1], 5)
            pygame.display.update()
            grid.append((x1, y1))
            x1 = x1 + 20


def push_up(x, y):
    pygame.draw.rect(screen, WHITE, (x + 1, y - w + 1, 17, 37), 0)
    pygame.display.update()


def push_down(x, y):
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, 17, 37), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, 37, 17), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, WHITE, (x - w + 1, y + 1, 37, 17), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, (0, 255, 0), (x + 1, y + 1, 17, 17), 0)
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, 17, 17), 0)
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 8, y + 8, 3, 3), 0)
    pygame.display.update()


def carve(x, y):
    single_cell(x, y)
    visited.append((x, y))
    stack.append((x, y))
    while len(stack) > 0:
        time.sleep(0.07)
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append('right')
        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append('left')
        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append('down')
        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append('up')
        if len(cell) > 0:
            choice = random.choice(cell)
            if choice == 'right':
                push_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))
            elif choice == 'left':
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))
            elif choice == 'down':
                push_down(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))
            elif choice == 'up':
                push_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            single_cell(x, y)
            time.sleep(0.05)
            backtracking_cell(x, y)


def plot(x, y):
    solution_cell(x, y)
    while (x, y) != (0, 0):
        x, y = solution[x, y]
        solution_cell(x, y)
        time.sleep(0.1)


build_grid(-20, 20)
carve(0, 0)
plot(350, 350)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

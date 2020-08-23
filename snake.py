import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30, True)


class Player:
    def __init__(self, x, y, width, color, lifes):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.delta_x = 0
        self.delta_y = 0
        self.snake_List = []
        self.snake_length = 1
        self.block_size = 10
        self.score = 0
        self.lifes = lifes

    def boundary(self):
        if self.x < 0:
            self.x = 0
            return False
        if self.x > 800 - self.width:
            self.x = 800 - self.width
            return False
        if self.y < 0:
            self.y = 0
            return False
        if self.y > 590:
            self.y = 590
            return False

    def draw(self, block_size1, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, self.color, (x[0], x[1], block_size1, block_size1))


class Food:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))


def collision(x1, y1, x2, y2):
    dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    if dist < 15:
        return True
    else:
        return False


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    paused = False
        screen.fill((255, 255, 255))
        text1 = font.render('To resume the game press u', 1, (0, 0, 0))
        screen.blit(text1, (270, 300))
        pygame.display.update()


snake = Player(150, 150, 10, (0, 255, 0), 3)
apple = Food(random.randint(0, 290), random.randint(0, 190), 10, (255, 0, 0))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.delta_x = 5
                    snake.delta_y = 0
                elif event.key == pygame.K_LEFT:
                    snake.delta_x = -5
                    snake.delta_y = 0
                elif event.key == pygame.K_UP:
                    snake.delta_y = -5
                    snake.delta_x = 0
                elif event.key == pygame.K_DOWN:
                    snake.delta_y = 5
                    snake.delta_x = 0
                elif event.key == pygame.K_SPACE:
                    pause()
        screen.fill((0, 0, 0))
        text = font.render('Score: ' + str(snake.score), 1, (0, 0, 255))
        screen.blit(text, (690, 10))
        snake.x += snake.delta_x
        snake.y += snake.delta_y
        if snake.boundary() is False:
            run = False
        col = collision(snake.x, snake.y, apple.x, apple.y)
        snake_head = [snake.x, snake.y]
        snake.snake_List.append(snake_head)
        if len(snake.snake_List) > snake.snake_length:
            del snake.snake_List[0]  # as the older elements will be front so u delete them
        for segment in snake.snake_List[:-1]:  # as the last element in snake list is the head
            if segment == snake_head:
                run = False
        snake.draw(snake.block_size, snake.snake_List)
        if col is True:
            apple.x = random.randint(0, 290)
            apple.y = random.randint(0, 190)
            snake.snake_length += 1
            snake.score += 1
        # pygame.draw.rect(screen, (0, 0, 255), (apple.x, apple.y, apple.width, apple.width))
        apple.draw()
        # pygame.draw.rect(screen, (255, 0, 0), (snake.x, snake.y, snake.width, snake.width))
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()

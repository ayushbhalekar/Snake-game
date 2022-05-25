import time

import pygame

from pygame.locals import *

import random

size = 40
width = 800
height = 600


class game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/Ayush/Downloads/Snake Game - Theme Song.mp3")
        pygame.mixer.music.play(-1, 0)
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.snake = snake(self.surface, 1)
        self.snake.draw()
        self.apple = apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('Arial', 30)
        score = font.render(f"Score:{self.snake.lenght - 1}", True, (255, 255, 255))
        self.surface.blit(score, (680, 10))

    def is_collision(self, block_x, block_y, image_x, image_y):
        if block_x >= image_x and block_x < image_x + size:
            if block_y >= image_y and block_y < image_y + size:
                return True
        return False

    def exit_game(self):
        sound1 = pygame.mixer.Sound("C:/Users/Ayush\Downloads/mixkit-arcade-fast-game-over-233.wav")
        pygame.mixer.Sound.play(sound1)
        pygame.mixer.music.pause()
        self.surface.fill((61, 252, 3))
        font = pygame.font.SysFont("comicsansms", 50)
        screen = font.render(f"Game Over!! Score is {self.snake.lenght - 1}", True, (255, 255, 255))
        self.surface.blit(screen, (160, 250))
        pygame.display.flip()
        time.sleep(3)
        exit(0)

    def won_game(self):
        sound1 = pygame.mixer.Sound("C:/Users/Ayush\Downloads/mixkit-arcade-fast-game-over-233.wav")
        pygame.mixer.Sound.play(sound1)
        pygame.mixer.music.pause()
        self.surface.fill((61, 252, 3))
        font = pygame.font.SysFont("comicsansms", 50)
        screen = font.render(f"You Won!! Score is {self.snake.lenght - 1}", True, (255, 255, 255))
        self.surface.blit(screen, (160, 250))
        pygame.display.flip()
        time.sleep(3)
        exit(0)

    def play(self):
        if self.snake.block_x[0] == self.width or self.snake.block_y[0] == self.height or \
                self.snake.block_x[0] == self.width - 800 or self.snake.block_y[0] == self.height - 600:
            self.exit_game()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake coliding with apple
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.image_x, self.apple.image_y):
            sound = pygame.mixer.Sound("C:/Users/Ayush/Downloads/mixkit-chewing-something-crunchy-2244.wav")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_lenght()
            self.apple.move()

        # snakehead coliding with snake
        for i in range(2, self.snake.lenght):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i],
                                 self.snake.block_y[i]):
                self.exit_game()

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.exit_game()
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                if event.type == QUIT:
                    self.exit_game()

            self.play()
            if self.snake.lenght <= 3:
                time.sleep(0.32)
            elif self.snake.lenght <= 5:
                time.sleep(0.31)
            elif self.snake.lenght <= 7:
                time.sleep(0.3)
            elif self.snake.lenght <= 9:
                time.sleep(0.27)
            elif self.snake.lenght <= 12:
                time.sleep(0.25)
            elif self.snake.lenght <= 17:
                time.sleep(0.22)
            if self.snake.lenght == 20:
                self.won_game()



class apple:
    def __init__(self, surface):
        self.surface = surface
        self.image = pygame.image.load("C:/Users/Ayush/Downloads/download.jpg")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.image_x = size * 3
        self.image_y = size * 3

    def move(self):
        self.image_x = random.randint(1, 19) * size
        self.image_y = random.randint(1, 14) * size

    def draw(self):
        self.surface.blit(self.image, (self.image_x, self.image_y))
        pygame.display.flip()


class snake:
    def __init__(self, surface, lenght):
        self.surface = surface
        self.block = pygame.image.load("C:/Users/Ayush/Downloads/hh.png")
        self.block = pygame.transform.scale(self.block, (size, size))
        self.lenght = lenght
        self.block_x = [size] * lenght
        self.block_y = [size] * lenght
        self.direction = "down"

    def increase_lenght(self):
        self.lenght += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def draw(self):
        self.surface.fill((77, 255, 0))
        for i in range(self.lenght):
            self.surface.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def walk(self):
        for i in range(self.lenght - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == "up":
            self.block_y[0] -= size

        if self.direction == "down":
            self.block_y[0] += size

        if self.direction == "right":
            self.block_x[0] += size

        if self.direction == "left":
            self.block_x[0] -= size

        self.draw()


g = game()
g.run()

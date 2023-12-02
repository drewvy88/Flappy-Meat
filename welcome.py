import pygame
import sys


pygame.init()

# Screen
FPS = 60
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Display
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Meat")
clock = pygame.time.Clock()

# Images
welcome_screen_background = pygame.image.load("game_images/field.jpeg").convert()

# Resize images
welcome_screen_background = pygame.transform.scale(welcome_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


def welcome_screen():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.blit(welcome_screen_background, (0, 0))



welcome_screen()


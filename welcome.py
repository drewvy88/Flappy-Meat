import pygame
import sys

pygame.init()

# Screen
FPS = 60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Constants
cloud1X = 0
cloud2X = 500
#cloud3X =
#cloud4X =
#cloud5X =
x_mov = 1
y_mov = 1

# Display
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Meat")
clock = pygame.time.Clock()

"""class Cloud:
    def __init__(self):
        self.x = 0
        self.y = SCREEN_HEIGHT/2 - 150
        self.y1 = SCREEN_HEIGHT/2 - 150

        self.image1 = pygame.image.load("game_images/cloudleft.png").convert_alpha()
        self.image2 = pygame.image.load("game_images/cloudright.png").convert_alpha()
        self.image3 = pygame.image.load("game_images/doublecloud.png").convert_alpha()
        self.image4 = pygame.image.load("game_images/cloudtrio.png").convert_alpha()
        self.image5 = pygame.image.load("game_images/cloudtrio2.png").convert_alpha()

        self.resize1 = pygame.transform.scale(self.image1, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.resize2 = pygame.transform.scale(self.image2, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.resize3 = pygame.transform.scale(self.image3, (100, 100))
        self.resize4 = pygame.transform.scale(self.image4, (100, 100))
        self.resize5 = pygame.transform.scale(self.image5, (100, 100))

    def moveCloud_right(self):
        self.x += 2
        return True
    def moveCloud_left(self):
        self.x -= 2
        return True"""


def draw_images(cloud):
    display.blit(cloud.resize1, (cloud.x + cloud1X, cloud.y))
    display.blit(cloud.resize2, (cloud.x + cloud2X, cloud.y))
    #display.blit(cloud.resize3, (cloud.x + cloud3X, cloud.y))
    #display.blit(cloud.resize4, (cloud.x + cloud4X, cloud.y))
    #display.blit(cloud.resize5, (cloud.x + cloud5X, cloud.y))


"""def cloud_move(cloud):
    if cloud.x == 100:
        cloud.x += x_mov
    if cloud.x == 800:
        cloud.x -= x_mov"""


def welcome_screen():

    #cloud = Cloud()

    # Sky
    welcome_screen_bg = pygame.image.load("game_images/welcome.png").convert()

    # Resize images
    welcome_screen_bg = pygame.transform.scale(welcome_screen_bg, (SCREEN_WIDTH, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

            display.blit(welcome_screen_bg, (0, 0))

            #draw_images(cloud)

            #if cloud.x <= 100:
            #cloud.moveCloud_right()



            pygame.display.flip()
            clock.tick(FPS)

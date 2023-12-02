import pygame
import sys
import random

# Initialize Flappy Meat
pygame.init()

# Screen
FPS = 60
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Draw Display
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Meat")
clock = pygame.time.Clock()

# Constants
gravity = 0.5
jump_height = 7
fire_width = 150
time_up = 60
fire_gap = 200
player_score = 0

# Messages
font = pygame.font.Font('freesansbold.ttf', 32)
score = font.render("SCORE", True, WHITE)

# Events
time_played = pygame.USEREVENT + 1

# Timers
pygame.time.set_timer(time_played, 60000)

# Images
background_img = pygame.image.load("game_images/field.jpeg").convert()
#meat_img = pygame.image.load("venv/my_meat1.png").convert_alpha()
fire_img = pygame.image.load("game_images/fire1.png").convert_alpha()
fire_img_rect = fire_img.get_rect()
top_fire_img = pygame.image.load("game_images/fire2.png").convert_alpha()

# Masks
#meat_mask = pygame.mask.from_surface(meat_img)
fire_mask = pygame.mask.from_surface(fire_img)
fire_mask_image = fire_mask.to_surface()
top_fire_mask = pygame.mask.from_surface(top_fire_img)

# Resize images
#meat_img = pygame.transform.scale(meat_img, (120, 120))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


class Meat:
    def __init__(self):
        self.image = pygame.image.load("game_images/my_meat1.png").convert_alpha()
        self.image_scale = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 200
        self.y = 250
        self.velocity = 0.5

    def jump(self):
        self.velocity = -jump_height

    def update(self):
        self.velocity += gravity
        self.y += self.velocity


class Fire:
    def __init__(self):
        self.x = SCREEN_WIDTH + 50
        self.height = random.randint(80, 300)
        self.y = SCREEN_HEIGHT - self.height + 30
        self.y2 = -35

    #def get_rect(self):
        #return pygame.Rect(self.x + fire_width, self.y + self.height, fire_width, self.height)

    def update(self):
        self.x -= 5


def add_score(meat, fires):
    global player_score
    meat_pos = meat.x + 60
    for fire in fires:
        fire_pos = fire.x + fire_width / 2
        if meat_pos == fire_pos:
            player_score += 1


#def check_collision(meat, fires):


def draw_images(meat, fires):
    display.blit(background_img, (0, 0))
    meat_img_resized = pygame.transform.scale(meat.image, (120, 120))
    display.blit(meat_img_resized, (meat.x, meat.y))
    display.blit(score, (450, 50))
    points = font.render(f'{player_score}', True, WHITE)
    display.blit(points, (500, 100))

    for fire in fires:
        fire_img_resized = pygame.transform.scale(fire_img, (fire_width, fire.height))
        display.blit(fire_img_resized, (fire.x, fire.y))
        #display.blit(fire_mask_image, (fire.x, fire.y))
        top_fire_img_resized = pygame.transform.scale(top_fire_img, (fire_width, SCREEN_HEIGHT - fire.height - 90))
        display.blit(top_fire_img_resized, (fire.x, fire.y2))


def main():
    global time_up, player_score
    meat = Meat()
    fires = []

    interval_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == time_played:
                print(time_elapsed)
                time_up += 60
            time_elapsed = f"You have been playing for {time_up} seconds."
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    meat.jump()

        meat.update()

        # Fire spawn-rate
        if interval_counter % 60 == 0:
            new_fire = Fire()
            fires.append(new_fire)
            interval_counter = 0
        else:
            pass
        interval_counter += 1

        for fire in fires:
            fire.update()
            if fire.height < 200:
                fire.y = SCREEN_HEIGHT - fire.height + 20

        # Add other functions:
        add_score(meat, fires)
        draw_images(meat, fires)
        #if check_collision(meat, fires):
            #meat.velocity += 50


        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

"""
Add collision boxes

Create welcome screen (separate function)
    - "input name here" (press enter)
    - press space bar to start

Friends leader board

Add scoring system

3 life system? each time you hit the fire the meat gets more "cooked" wings start gettinb burnt?

Can add meteors (meatballs on fire) occasionally raining diagonlly through screen. Players can have 1 "blink" available every 3-5s?
"""

import pygame,os, random


class Enemy(pygame.sprite.Sprite):
    # Enemy spirte object, moves towards Player to attack
    #multiple enemies are to spawn
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 1
        self.speed = 0.5
        self.x_position = 500
        self.y_position = 200
        self.sprite = pygame.transform.smoothscale((pygame.image.load(os.path.join("assets","terrance.png"))),(64,64))
        self.rect = self.sprite.get_rect()

    def move(self,player_x, player_y):
        # move towards player at speed,
        #use x and y position and update them
        direction_x = 1 if player_x > self.x_position else -1
        direction_y = 1 if player_y > self.y_position else -1
        self.x_position += direction_x * self.speed
        self.y_position += direction_y * self.speed
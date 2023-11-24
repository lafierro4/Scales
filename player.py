from typing import Any
import pygame,os
from enemy import Enemy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._hp = 5
        self._speed = 5
        self._x_position = 100
        self._y_position = 300
        self._sprite = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","scaro.png")),(32,32))
        self.rect = self.sprite.get_rect()
    
    def attack(self,direction):
        # Shoot bullet
        scale = Scale(self.x_position,self.y_position,direction)
        scale.add()
        # Implement the bullet shooting logic here



    def update_position(self, keys):
        if keys[pygame.K_w]:
            self.y_position -= self.speed
        elif keys[pygame.K_s]:
            self.y_position += self.speed
        if keys[pygame.K_a]:
            self.x_position -= self.speed
        elif keys[pygame.K_d]:
            self.x_position += self.speed

    def update(self,keys):
        self.update_position(keys)
        


    @property
    def sprite(self) -> pygame.Surface:
        return self._sprite
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self,value):
        self._hp += value
    @property 
    def speed(self) ->int:
        return self._speed
    @property
    def x_position(self) -> int:
        return self._x_position
    @x_position.setter
    def x_position(self, value: int):
        # Add any validation logic if needed
        self._x_position = value
    @property
    def y_position(self) -> int:
        return self._y_position
    @y_position.setter
    def y_position(self, value: int):
        # Add any validation logic if needed
        self._y_position = value

class Scale(pygame.sprite.Sprite):
    def __init__(self,player_x,player_y, direction):
        pygame.sprite.Sprite.__init__(self)
        self._dmg = 1
        self._speed = 6
        self.direction = direction
        self._x_position = player_x
        self._y_position = player_y
        self.sprite = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","scale.png")),(32,32))
        self.rect = self.sprite.get_rect()
    
    def update(self) -> None:
        self.x_position += self.direction[0] * self.speed
        self.y_position += self.direction[1] * self.speed


    def onHit(self,enemy):
        #When the bullet hits an enemy, lower enemy hp, destroy bullet instance
        enemy.hp -= self._dmg

    @property
    def dmg(self):
        return self._dmg
    @dmg.setter
    def dmg(self,value):
        self._dmg += value
    
    @property
    def speed(self):
        return self._speed
    @property
    def x_position(self) -> int:
        return self._x_position
    @x_position.setter
    def x_position(self, value: int):
        # Add any validation logic if needed
        self._x_position = value
    @property
    def y_position(self) -> int:
        return self._y_position
    @y_position.setter
    def y_position(self, value: int):
        # Add any validation logic if needed
        self._y_position = value
    @property
    def direction(self):
        return self._direction
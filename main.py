import pygame, os, random
from player import Player, Scale
from enemy import Enemy

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")

def main():
    scaro = Player()
    enemy = Enemy()

    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    scaro.attack(0)

        keys = pygame.key.get_pressed()

        scaro.update(keys)
        
        enemy.move(scaro.x_position,scaro.y_position)

        if pygame.sprite.collide_rect(scaro.bullet, enemy):
            scaro.bullet.onHit(enemy)

        SCREEN.fill((255, 255, 255))  # Fill the screen with white (optional)
        SCREEN.blit(scaro.sprite, (scaro.x_position, scaro.y_position))
        SCREEN.blit(enemy.sprite, (enemy.x_position, enemy.y_position))

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main()
import pygame, os, random

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")

x,y = 100,100
sclap_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("sclap.png")), (64,64))
run = True
clock = pygame.time.Clock()
while run:
    SCREEN.blit(sclap_image,(x,y))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 10
            elif event.key == pygame.K_s:
                y += 10
            if event.key == pygame.K_a:
                x -= 10
            elif event.key == pygame.K_d:
                x += 10
    pygame.display.update()
    clock.tick(FPS)
            

pygame.quit()
print("broke")
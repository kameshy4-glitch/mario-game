import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

player_x = 100
player_y = 300
velocity_y = 0
gravity = 1
jump = -15

running = True
while running:
    screen.fill((135, 206, 235))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y >= 300:
        velocity_y = jump
        
    velocity_y += gravity
    player_y += velocity_y
    
    if player_y >= 300:
        player_y = 300
        
    pygame.draw.rect(screen, (255,0,0), (player_x, player_y, 40, 40))
    
    pygame.display.update()
    clock.tick(60)

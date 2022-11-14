import pygame
import os

WIDTH, HEIGHT = 1350, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\background-white.png")), (WIDTH, HEIGHT))
wizard_w = 165
wizard_h = 180
wiz_r = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\wizard_r.png")), (wizard_w, wizard_h))
wiz_l = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\wizard_l.png")), (wizard_w, wizard_h))

class Player:
        CD = 60

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.player_img = wiz_r

        def draw(self, window):
                window.blit(self.player_img, (self.x, self.y))
                
        
        def get_width(self):
                return self.player_img.get_width()

        def get_height(self):
                return self.player_img.get_height()  


run = True
FPS = 80
        
move = 3
vel = 8

jumping = False
y_gravity = 1
jump_height = 15
y_velocity = jump_height

player1 = Player(300, 279)

clock = pygame.time.Clock()

def redraw_window():
    WIN.blit(BG, (0,0))

    player1.draw(WIN)


    pygame.display.update()
        
while run:
    clock.tick(FPS)

    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x - move + wizard_w> 0:
        player1.x -= move
        player1.player_img = wiz_l
    if keys[pygame.K_d] and player1.x + move < WIDTH:
        player1.x += move
        player1.player_img = wiz_r
    if keys[pygame.K_w]:
        jumping = True
    
    if jumping:
        player1.y -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height
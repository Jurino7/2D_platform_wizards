import pygame
import os

WIDTH, HEIGHT = 1280, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\background-medieval.png")), (WIDTH, HEIGHT))
player_w = 165
player_h = 180

assasin_r = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\assasin.png")), (player_w, player_h))
assasin_r_walk = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\assasin_walking.png")), (player_w, player_h))
assasin_l = pygame.transform.flip(assasin_r, True, False)
assasin_l_walk = pygame.transform.flip(assasin_r_walk, True, False)
assasin_r_attack = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\assasin_attacking.png")), (player_w, player_h))
assasin_l_attack = pygame.transform.flip(assasin_r_attack, True, False)

wiz_r = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\wizard.png")), (player_w, player_h ))
wiz_l = pygame.transform.flip(wiz_r, True, False)
wiz_r_attack = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\wizard_attack.png")), (player_w, player_h ))
wiz_l_attack = pygame.transform.flip(wiz_r_attack, True, False)

king_l = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\king.png")), (player_w, player_h))
king_r = pygame.transform.flip(king_l, True, False)

attack = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\londa\OneDrive\Documents\py\2D_platform_wizards-main\characters\attack_zone.png")), (10, 14))

#?
class Attack:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = attack
        self.mask = pygame.mask.from_surface(attack)
    
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
         

class Player:
        def __init__(self, x, y, player_img, health):
                self.x = x
                self.y = y
                self.player_img = player_img
                self.health = health
                self.orientation = 'right'
                self.mask = pygame.mask.from_surface(self.player_img)

        def draw(self, window):
                window.blit(self.player_img, (self.x, self.y))
                
        
        def get_width(self):
                return self.player_img.get_width()

        def get_height(self):
                return self.player_img.get_height()
        
        
def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

run = True
FPS = 80
        
move = 3
vel = 8

jumping = False
standing = True
y_gravity = 1
jump_height = 15
y_velocity = jump_height

player1 = Player(300, 530, assasin_r, health=1)
player2 = Player(600, 550, wiz_l, health=1)
 
clock = pygame.time.Clock()

def redraw_window():
    WIN.blit(BG, (0,0))

    player1.draw(WIN)
    player2.draw(WIN)

    pygame.display.update()
        
while run:
    clock.tick(FPS)

    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    #movement of player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x - move + player_w> 0:
        player1.x -= move
        player1.player_img = assasin_l_walk
        player1.orientation = 'left'
        standing = False

    if keys[pygame.K_d] and player1.x + move < WIDTH:
        player1.x += move
        player1.player_img = assasin_r_walk
        player1.orientation = 'right'
        standing = False

    if keys[pygame.K_w]:
        jumping = True
        if player1.orientation == 'right':
            player1.player_img = assasin_r
        if player1.orientation == 'left':
            player1.player_img = assasin_l

    if keys[pygame.K_q]:
        standing = False
        
        if collide(player1, player2):
            player2.health -= 1
        print(player2.health)
        
        if player1.orientation == 'right':
            player1.player_img = assasin_r_attack
        if player1.orientation == 'left':
            player1.player_img = assasin_l_attack
        
    if jumping:
        player1.y -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height

    if standing:
        if player1.orientation == 'right':
            player1.player_img = assasin_r
        if player1.orientation == 'left':
            player1.player_img = assasin_l
    
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        standing = True
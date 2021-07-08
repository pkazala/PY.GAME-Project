import sys
import random
import pygame

def create_rock():
    random_rock_pos = random.choice(rock_height)
    new_rock = rock_surface.get_rect(midtop = (1800,random_rock_pos))
    return new_rock

def move_rocks(rocks):
    for rock in rocks:
        rock.centerx -= 5
    return rocks

def draw_rocks(rocks):
    for rock in rocks:
        screen.blit(rock_surface,rock)

def collision(rocks):
    for rock in rocks:
        if ship_rect.colliderect(rock):
            return False

    if ship_rect.top <= -100 or ship_rect.bottom >= 900:
        return False

    return True

def ship_animation():
    new_ship = ship_frames[ship_index]
    new_ship_rect = new_ship.get_rect(center = (150, ship_rect.centery))
    return new_ship,new_ship_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (525,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(525, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(525, 700))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

def check_score(score):
    return score

pygame.init()
screen = pygame.display.set_mode((1050,789))
clock = pygame.time.Clock()
game_font = pygame.font.Font('ARCADECLASSIC.ttf',40)

ship_movement = 0
fall = 0.20
game_active = True
score = 0
high_score = 0

main_surface = pygame.image.load('4393127.png')
floor_surface = pygame.image.load('unnamed.png')

ship_1 = pygame.image.load('1.png').convert_alpha()
ship_1 = pygame.transform.scale(ship_1, (132,84))
ship_1 = pygame.transform.flip(ship_1,True,False)
ship_2 = pygame.image.load('2.png').convert_alpha()
ship_2 = pygame.transform.scale(ship_2, (132,84))
ship_2 = pygame.transform.flip(ship_2,True,False)
ship_3 = pygame.image.load('3.png').convert_alpha()
ship_3 = pygame.transform.scale(ship_3, (132,84))
ship_3 = pygame.transform.flip(ship_3,True,False)
ship_4 = pygame.image.load('4.png').convert_alpha()
ship_4 = pygame.transform.scale(ship_4, (132,84))
ship_4 = pygame.transform.flip(ship_4,True,False)
ship_5 = pygame.image.load('5.png').convert_alpha()
ship_5 = pygame.transform.scale(ship_5, (132,84))
ship_5 = pygame.transform.flip(ship_5,True,False)
ship_6 = pygame.image.load('6.png').convert_alpha()
ship_6 = pygame.transform.scale(ship_6, (132,84))
ship_6 = pygame.transform.flip(ship_6,True,False)
ship_7 = pygame.image.load('7.png').convert_alpha()
ship_7 = pygame.transform.scale(ship_7, (132,84))
ship_7 = pygame.transform.flip(ship_7,True,False)
ship_8 = pygame.image.load('8.png').convert_alpha()
ship_8 = pygame.transform.scale(ship_8, (132,84))
ship_8 = pygame.transform.flip(ship_8,True,False)
ship_9 = pygame.image.load('9.png').convert_alpha()
ship_9 = pygame.transform.scale(ship_9, (132,84))
ship_9 = pygame.transform.flip(ship_9,True,False)
ship_frames = [ship_1,ship_2,ship_3,ship_4,ship_5,ship_6,ship_7,ship_8,ship_9]
ship_index = 0
ship_surface = ship_frames[ship_index]
ship_rect = ship_surface.get_rect(center = (150,395))

#flame_surface = pygame.image.load('shipp.png').convert_alpha()
#flame_rect = flame_surface.get_rect(center = (pos_x,pos_y))

SHIPFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(SHIPFLAP,100)
#ship_surface = pygame.image.load('shipp.png').convert_alpha()
#ship_surface = pygame.transform.rotate(ship_surface,270)
#ship_surface = pygame.transform.scale(ship_surface,(90,80))
#ship_rect = ship_surface.get_rect(center = (200,395))


rock_surface = pygame.image.load('sakurka.png').convert_alpha()
rock_surface = pygame.transform.scale(rock_surface,(180,180))
rock_list = []
SPAWNROCK = pygame.USEREVENT
if score <= 10:
    pygame.time.set_timer(SPAWNROCK,1500)
    rock_height = [530, 0, 200, 130, 380, 250]
    check_score(score)
else:
    pygame.time.set_timer(SPAWNROCK,50)
    rock_height = [530, 0, 200, 130, 380, 250]
    check_score(score)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                ship_movement = 0
                ship_movement -= 7
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                rock_list.clear()
                ship_rect.center = (200,395)
                ship_movement = 0
                score = 0

        if event.type == SPAWNROCK:
            rock_list.append(create_rock())

        if event.type == SHIPFLAP:
            if ship_index < 8:
                ship_index += 1
            else:
                ship_index = 2

            ship_surface,ship_rect = ship_animation()

    screen.blit(main_surface,(0,0))

    if game_active:
        ship_rect.centery += ship_movement
        screen.blit(ship_surface,ship_rect)
        ship_movement += fall
        game_active = collision(rock_list)

        rock_list = move_rocks(rock_list)
        draw_rocks(rock_list)

        score += 0.03
        score_display('main_game')

    else:
        high_score = update_score(score,high_score)
        score_display('game_over')

    pygame.display.update()
    clock.tick(90)

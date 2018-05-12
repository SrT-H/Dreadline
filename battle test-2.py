import pygame, sys, glob, time, os

os.environ['SDL_VIDEO_CENTERED'] = '1'
gameDisplay = pygame.display.set_mode((1280, 720))

#----- PLAYER 1 -----
class player1(pygame.sprite.Sprite):

    def __init__(self, location, x, y):
        self.x = x
        self.y = y
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob(location)
        self.ani.sort()            
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        #self.img = pygame.transform.scale(self.img, (100, 100))
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.rect = self.img.get_rect()
        self.update(0)

    #update
    def update(self, pos):
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
            #self.img = pygame.transform.scale(self.img, (100, 100))
            self.rect = self.img.get_rect()
            p1_char_check = self.img
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1
        gameDisplay.blit(self.img, (self.x, self.y))

    #health bar
    def full_health_bar(self, in_hp, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('/'+str(in_hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

#----- PLAYER 2 -----
class player2(pygame.sprite.Sprite):

    def __init__(self, location, x, y):
        self.x = x
        self.y = y
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob(location)
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        #self.img = pygame.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.update(0)

    #update
    def update(self, pos):
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
            #self.img = pygame.transform.scale(self.img, (100, 100))
            self.rect = self.img.get_rect()
            p1_char_check = self.img
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1
        gameDisplay.blit(self.img, (self.x, self.y))

    # health bar
    def full_health_bar(self, in_hp, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('/' + str(in_hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))


''' ------------------------- '''
#1-1
p1_1_location = "Picture\\Character\\Female_1\\default\\0\\stand1_0.png"
p1_1_location_atk = "Picture\\Character\\Female_1\\default\\0\\stabO1_R (*).png"
#1-2
p1_2_location = "Picture\\Character\\Female_2\\default\\0\\stand1_1.png"
p1_2_location_atk = "Picture\\Character\\Female_2\\default\\0\\stabO1_R (*).png"
#1-3
p1_3_location = "Picture\\Character\\Female_3\\default\\0\\stand1_1.png"
p1_3_location_atk = "Picture\\Character\\Female_3\\default\\0\\stabO1_R (*).png"

#2-1
p2_1_location = "Picture\\Character\\Male_1\\default\\0\\stand1_0.png"
p2_1_location_atk = "Picture\\Character\\Male_1\\default\\0\\stabO1_R (*).png"
#2-2
p2_2_location = "Picture\\Character\\Male_2\\default\\0\\stand1_0.png"
p2_2_location_atk = "Picture\\Character\\Male_2\\default\\0\\stabO1_R (*).png"
#2-3
p2_3_location = "Picture\\Character\\Male_3\\default\\0\\stand1_0.png"
p2_3_location_atk = "Picture\\Character\\Male_3\\default\\0\\stabO1_R (*).png"

#---------- MAIN ----------
def main():
    gameDisplay = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('D R E A D L I N E ')
    
    run_game()
   
#--------- START -----------
def run_game():
    
    w = 1280
    h = 720

    gameDisplay = pygame.display.set_mode((w, h))
    
    player_1_1 = player1(p1_1_location, 200, 100)
    player_1_2 = player1(p1_2_location, 300, 250)
    player_1_3 = player1(p1_3_location, 200, 400)

    player_2_1 = player2(p2_1_location, 980, 100)
    player_2_2 = player2(p2_2_location, 880, 250)
    player_2_3 = player2(p2_3_location, 980, 400)
    
    clock = pygame.time.Clock()

    gameExit = False


    pygame.display.update()
    while not gameExit:

        player_1_1.full_health_bar(100, 200, 550)
        player_1_2.full_health_bar(80, 200, 600)
        player_1_3.full_health_bar(50, 200, 650)

        player_2_1.full_health_bar(120, 1150, 550)
        player_2_2.full_health_bar(50, 1150, 600)
        player_2_3.full_health_bar(200, 1150, 650)

        for event in pygame.event.get():
            #print("EVENT:  ",event)
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.display.update()
                
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
main()

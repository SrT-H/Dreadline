import pygame, sys, glob, time, os
from Character_Selection import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
gameDisplay = pygame.display.set_mode((1280, 720))

black = (0, 0, 0)
white = (255, 255, 255)

bg = pygame.image.load("Picture\\BG\\background.png")
bg = pygame.transform.scale(bg, (1280, 720))
gameDisplay.blit(bg, (0, 0))
pygame.draw.rect(gameDisplay, white, [100, 200, 400, 500])
pygame.display.update()


#----- PLAYER 1 -----
class player1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = ''
        self.hp = 0
        self.max_hp = 0
        self.ap = 0
        self.dp = 0
        self.location = ''
        self.atk_location = ''
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob('')
        self.ani.sort()            
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        #self.img = pygame.image.load(self.ani[0])
        #self.img = pygame.transform.scale(self.img, (100, 100))
        #self.img = pygame.transform.flip(self.img, 100, 0)
        #self.rect = self.img.get_rect()
        #self.update(0)

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

    #set_location
    def set_location(self, loca1, loca2):
        self.location = loca1
        self.atk_location = loca2

        self.ani = glob.glob(self.location)
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.update(0)

    #set status
    def set_status(self, lst):
        self.name = lst[0]
        self.max_hp = lst[1]
        self.hp = lst[1]
        self.ap = lst[2]
        self.dp = lst[3]

    #name
    def name_display(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render(str(self.name), True, (255, 215, 0))
        gameDisplay.blit(text, (x, y))

    #status bar
    def status_bar(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text1 = myfont.render('AP: ' + str(self.ap), True, (225, 0, 0))
        text2 = myfont.render('  DP: '+ str(self.dp), True, (0, 200, 225))
        gameDisplay.blit(text1, (x, y))
        gameDisplay.blit(text2, (x+80, y))

    #full health bar
    def full_health_bar(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('/'+str(self.max_hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    #health
    def health(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render(str(self.hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    #attack
    def atk(self):
        ani_pos = 0
        self.ani = glob.glob(self.atk_location)
        self.img = pygame.image.load(self.ani[ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani) - 1
        time_delay = 0
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            time_delay = 200
            ani_pos += 1
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(self.img, (self.x, self.y))
            pygame.display.update()
            gameDisplay.blit(bg, (0, 0))
        pygame.display.update()
        self.ani = glob.glob(self.location)
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani) - 1

    '''
    def idle(self):
        ani_pos = 0
        self.img = pygame.transform.flip(self.img, 100, 0)
        time_delay = 200
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            ani_pos += 1
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(self.img, (self.x, self.y))
            pygame.display.update()
    '''

#----- PLAYER 2 -----
class player2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = ''
        self.hp = 0
        self.max_hp = 0
        self.ap = 0
        self.dp = 0
        self.location = ''
        self.atk_location = ''
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob('')
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        #self.img = pygame.image.load(self.ani[0])
        #self.img = pygame.transform.scale(self.img, (100, 100))
        #self.rect = self.img.get_rect()
        #self.update(0)

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

    #set_location
    def set_location(self, loca1, loca2):
        self.location = loca1
        self.atk_location = loca2
        self.ani = glob.glob(self.location)
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.update(0)

    #set status
    def set_status(self, lst):
        self.name = lst[0]
        self.max_hp = lst[1]
        self.hp = lst[1]
        self.ap = lst[2]
        self.dp = lst[3]

    #name
    def name_display(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render(str(self.name), True, (255, 215, 0))
        gameDisplay.blit(text, (x, y))

    #status bar
    def status_bar(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text1 = myfont.render('AP: ' + str(self.ap), True, (225, 0, 0))
        text2 = myfont.render('  DP: '+ str(self.dp), True, (0, 200, 225))
        gameDisplay.blit(text1, (x, y))
        gameDisplay.blit(text2, (x+80, y))

    #full health bar
    def full_health_bar(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('/'+str(self.max_hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    #health
    def health(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render(str(self.hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    #attack
    def atk(self):
        ani_pos = 0
        self.ani = glob.glob("")
        self.img = pygame.image.load(self.ani[ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani) - 1
        time_delay = 0
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            pygame.time.delay(time_delay)
            time_delay = 200
            ani_pos += 1
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(self.img, (self.x, self.y))
            pygame.display.update()

        self.ani = glob.glob("")
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.ani_max = len(self.ani) - 1

        '''
        def idle(self):
            ani_pos = 0
            self.img = pygame.transform.flip(self.img, 100, 0)
            time_delay = 200
            while ani_pos <= self.ani_max:
                self.img = pygame.image.load(self.ani[ani_pos])
                self.img = pygame.transform.flip(self.img, 100, 0)
                pygame.time.delay(time_delay)
                ani_pos += 1
                gameDisplay.blit(bg, (0, 0))
                gameDisplay.blit(self.img, (self.x, self.y))
                pygame.display.update()
            '''


class Battle():
    #----- PIC LOCATION -----
    def character_location(num):
        if num == 1:
            # Zalana
            txt = "Picture\\Character\\Female_1\\default\\0\\stand1_*.png"
        elif num == 2:
            # Elentriana
            txt = "Picture\\Character\\Female_2\\default\\0\\stand1_*.png"
        elif num == 3:
            # Shaca
            txt = "Picture\\Character\\Female_3\\default\\0\\stand1_*.png"
        elif num == 4:
            # Kazuki
            txt = "Picture\\Character\\Male_1\\default\\0\\stand1_*.png"
        elif num == 5:
            # Lucifer
            txt = "Picture\\Character\\Male_2\\default\\0\\stand1_*.png"
        elif num == 6:
            # Refaian
            txt = "Picture\\Character\\Male_3\\default\\0\\stand2_*.png"
        return txt

    #----- PIC ATK LOCATION -----
    def character_location_atk(num):
        if num == 1:
            txt = "Picture\\Character\\Female_1\\default\\0\\stabOF_*.png"
        elif num == 2:
            txt = "Picture\\Character\\Female_2\\default\\0\\stabOF_*.png"
        elif num == 3:
            txt = "Picture\\Character\\Female_3\\default\\0\\stabOF_*.png"
        elif num == 4:
            txt = "Picture\\Character\\Male_1\\default\\0\\stabOF_*.png"
        elif num == 5:
            txt = "Picture\\Character\\Male_2\\default\\0\\stabOF_*.png"
        elif num == 6:
            txt = "Picture\\Character\\Male_3\\default\\0\\stabOF_*.png"
        return txt

    #----- STATUS -----
    def get_status(num):
        #NAME - HP - AP - DP
        if num == 1:
            lst = ['Zalana', 110, 5, 100]
        elif num == 2:
            lst = ['Elentriana', 80, 15, 50]
        elif num == 3:
            lst = ['Shaca', 75, 20, 35]
        elif num == 4:
            lst = ['Kazuki', 60, 35, 75]
        elif num == 5:
            lst = ['Lucifer', 60, 40, 50]
        elif num == 6:
            lst = ['Refaian', 100, 7, 100]
        return lst

    #------ GAME OVER -----
    def gamover():
        ''' play again (y/n) '''

    #---------- MAIN ----------
    def main():
        pygame.display.set_caption('D R E A D L I N E ')
        run_game()
    
    #--------- START -----------
    def run_game():
        #1 - 1
        player_1_1 = player1(200, 100)
        player_1_1.set_location(character_location(2), character_location_atk(2))
        player_1_1.set_status(get_status(2))
        #1 - 2
        player_1_2 = player1(300, 250)
        player_1_2.set_location(character_location(5), character_location_atk(5))
        player_1_2.set_status(get_status(5))
        #1 - 3
        player_1_3 = player1(200, 400)
        player_1_3.set_location(character_location(6), character_location_atk(6))
        player_1_3.set_status(get_status(6))

        #2 - 1
        player_2_1 = player2(980, 100)
        player_2_1.set_location(character_location(1), character_location_atk(1))
        player_2_1.set_status(get_status(1))
        #2 - 2
        player_2_2 = player2(880, 250)
        player_2_2.set_location(character_location(3), character_location_atk(3))
        player_2_2.set_status(get_status(3))
        #2 - 3
        player_2_3 = player2(980, 400)
        player_2_3.set_location(character_location(4), character_location_atk(4))
        player_2_3.set_status(get_status(4))

        gameDisplay.blit(bg, (0, 0))
        pygame.draw.rect(gameDisplay, white, [100, 200, 400, 500])

        clock = pygame.time.Clock()
        gameExit = False

        pygame.display.update()

        while not gameExit:
            # Background
            gameDisplay.blit(bg, (0, 0))
            pygame.draw.rect(gameDisplay, black, [30, 520, 450, 180])
            pygame.draw.rect(gameDisplay, black, [800, 520, 450, 180])

            # 1
            player_1_1.name_display(50, 550)
            player_1_1.full_health_bar(200, 550)
            player_1_1.health(165, 550)
            player_1_1.status_bar(280, 550)

            player_1_2.name_display(50, 600)
            player_1_2.full_health_bar(200, 600)
            player_1_2.health(165, 600)
            player_1_2.status_bar(280, 600)

            player_1_3.name_display(50, 650)
            player_1_3.full_health_bar(200, 650)
            player_1_3.health(165, 650)
            player_1_3.status_bar(280, 650)

            # 2
            player_2_1.name_display(850, 550)
            player_2_1.full_health_bar(985, 550)
            player_2_1.health(950, 550)
            player_2_1.status_bar(1050, 550)

            player_2_2.name_display(850, 600)
            player_2_2.full_health_bar(985, 600)
            player_2_2.health(950, 600)
            player_2_2.status_bar(1050, 600)

            player_2_3.name_display(850, 650)
            player_2_3.full_health_bar(985, 650)
            player_2_3.health(950, 650)
            player_2_3.status_bar(1050, 650)

            for event in pygame.event.get():

                #print("EVENT:  ",event)
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.display.update()
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    player_1_1.atk()

            player_1_1.update(0)
            player_1_2.update(0)
            player_1_3.update(0)
            player_2_1.update(0)
            player_2_2.update(0)
            player_2_3.update(0)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()
        
    main()

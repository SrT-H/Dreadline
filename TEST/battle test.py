import pygame
import time

class player1(pygame.sprite.Sprite):
    def __init__(self):
        self.white =(255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        self.display_width = 1280
        self.display_height = 720

        self.clock = pygame.time.Clock()
        self.FPS = 30

        #self.font = pygame.font.SysFont(None, 25)
        
        self.gameExit = False
        
    #----- ATK -----
    def atk(self):
            
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.img = pygame.transform.scale(self.img, (wh_char, 200))
        while  self.ani_pos <= self.ani_max:
            stage_show = pygame.image.load(stage_location)
            stage_show = pygame.transform.scale(stage_show, (800, 600))
            gameDisplay.blit(stage_show, (0, 0))
            player_2.update(pos_P2)
            self.img = pygame.image.load(self.ani[self.ani_pos])
            self.img = pygame.transform.scale(self.img, (wh_char, 200))
            self.rect = self.img.get_rect()
            p1_char_check = self.img
            pygame.time.delay(time_delay)
            self.ani_pos += 1
            gameDisplay.blit(self.img, (self.x, self.y))
            pygame.display.update()
            
    #----- CHECK CHARACTER -----
    def check_char():
        #1-1
        p1_1_location = "Picture\\Character\\Female_1\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Female_1\\default\\0\\stabO1_R (*).png"
        #1-2
        p1_1_location = "Picture\\Character\\Female_2\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Female_2\\default\\0\\stabO1_R (*).png"
        #1-3
        p1_1_location = "Picture\\Character\\Female_3\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Female_3\\default\\0\\stabO1_R (*).png"
        
        #2-1
        p1_1_location = "Picture\\Character\\Male_1\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Male_1\\default\\0\\stabO1_R (*).png"
        #2-2
        p1_1_location = "Picture\\Character\\Male_2\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Male_2\\default\\0\\stabO1_R (*).png"
        #2-3
        p1_1_location = "Picture\\Character\\Male_3\\default\\0\\stand1_R (*).png"
        p1_1_location_atk = "Picture\\Character\\Male_3\\default\\0\\stabO1_R (*).png"
        
    #----- MAIN -----
    def main(self):
        self.mainMenu = True
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('D R E A D L I N E ')

        
        #UPDATE WINDOW
        pygame.display.update()
        
        while not self.gameExit:
            for event in pygame.event.get():
                #print(event) #check event in window
                '''mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()
                mLPress = pygame.mouse.get_pressed()[0] #check left click | 1 = click
                print(mPos, mLPress)'''

                if event.type == pygame.QUIT:
                    self.gameExit = True
                             
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()
        
battle().main()

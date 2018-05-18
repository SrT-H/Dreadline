import pygame
import time
pygame.init()


class dreadline:
    
    #----- init -----
    def __init__(self):
        pygame.init()
        self.white =(255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        self.display_width = 1280
        self.display_height = 720

        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.font = pygame.font.SysFont(None, 25)
        
        self.gameExit = False
        
    #----- MAIN -----
    def menu(self):
        self.mainMenu = True
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('D R E A D L I N E ')

        #START BUTTON
        startButton = pygame.image.load("Picture\Text\START.png")
        startButton = pygame.transform.scale(startButton, (300, 70))
        gameDisplay.blit(startButton, (480, 350))
        
        #GUIDE BUTTON
        guideButton = pygame.image.load("Picture\Text\GUIDE.png")
        guideButton = pygame.transform.scale(guideButton, (300, 70))
        gameDisplay.blit(guideButton, (480, 450))
        
        #EXIT BUTTON
        exitButton = pygame.image.load("Picture\Text\EXIT.png")
        exitButton = pygame.transform.scale(exitButton, (200, 70))
        gameDisplay.blit(exitButton, (530, 550))
        
        #UPDATE WINDOW
        pygame.display.update()
        
        while not self.gameExit:
            for event in pygame.event.get():
                #print(event) #check event in window
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()
                mLPress = pygame.mouse.get_pressed()[0] #check left click | 1 = click
                print(mPos, mLPress)

                if event.type == pygame.QUIT:
                    self.gameExit = True
                             
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()


dreadline().menu()

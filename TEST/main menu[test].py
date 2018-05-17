import pygame
import time
pygame.init()

class main_menu:
    def __init__(self):
        pygame.init()
        self.white =(255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        self.display_width = 800
        self.display_height = 600

        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Dreadline')

        self.clock = pygame.time.Clock()

        
        self.FPS = 30

        self.font = pygame.font.SysFont(None, 25)

        self.gameStart = False
        self.gameExit = False
        self.gameHelp = False
        self.mainMenu = True

    def startGame(self):
        pygame.init()
        self.gameDisplay.fill(self.black)
        self.mainMenu = False
        Select_Character_Stage().p1_character_select_menu()
        
    def gameHelper(self):
        pygame.init()
        self.gameDisplay.fill(self.black)
        self.mainMenu = False
        self.gameExit = False
    
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Game Helper')

        while not self.gameExit:
            #Player1
            player1_TEXT = pygame.image.load("UI\Helper\player1.png")
            player1_TEXT = pygame.transform.scale(player1_TEXT, (200, 200))
            gameDisplay.blit(player1_TEXT, (70, 0))
            
            letterA_Key = pygame.image.load("UI\Helper\Letter keys\letter_a.png")
            letterA_Key = pygame.transform.scale(letterA_Key, (50, 50))
            gameDisplay.blit(letterA_Key, (100, 150))

            p1_left_text = pygame.image.load("UI\Helper\P1_left.png")
            p1_left_text = pygame.transform.scale(p1_left_text, (200, 200))
            gameDisplay.blit(p1_left_text, (150, 80))
            
            letterS_Key = pygame.image.load("UI\Helper\Letter keys\letter_s.png")
            letterS_Key = pygame.transform.scale(letterS_Key, (50, 50))
            gameDisplay.blit(letterS_Key, (100, 250))

            p1_right_text = pygame.image.load("UI\Helper\P1_right.png")
            p1_right_text = pygame.transform.scale(p1_right_text, (200, 200))
            gameDisplay.blit(p1_right_text, (150, 180))
            
            letterX_Key = pygame.image.load("UI\Helper\Letter keys\letter_x.png")
            letterX_Key = pygame.transform.scale(letterX_Key, (50, 50))
            gameDisplay.blit(letterX_Key, (100, 350))
            
            p1_atk_text = pygame.image.load("UI\Helper\P1_ATK.png")
            p1_atk_text = pygame.transform.scale(p1_atk_text, (200, 200))
            gameDisplay.blit(p1_atk_text, (150, 280))
            
            #Player2
            player2_TEXT = pygame.image.load("UI\Helper\player2.png")
            player2_TEXT = pygame.transform.scale(player2_TEXT, (200, 200))
            gameDisplay.blit(player2_TEXT, (430, 0))        
            
            letterH_Key = pygame.image.load("UI\Helper\Letter keys\letter_h.png")
            letterH_Key = pygame.transform.scale(letterH_Key, (50, 50))
            gameDisplay.blit(letterH_Key, (450, 150))
            
            p2_left_text = pygame.image.load("UI\Helper\P2_left.png")
            p2_left_text = pygame.transform.scale(p2_left_text, (200, 200))
            gameDisplay.blit(p2_left_text, (500, 80))
            
            letterJ_Key = pygame.image.load("UI\Helper\Letter keys\letter_j.png")
            letterJ_Key = pygame.transform.scale(letterJ_Key, (50, 50))
            gameDisplay.blit(letterJ_Key, (450, 250))
            
            p2_right_text = pygame.image.load("UI\Helper\P2_right.png")
            p2_right_text = pygame.transform.scale(p2_right_text, (200, 200))
            gameDisplay.blit(p2_right_text, (500, 180))
            
            letterM_Key = pygame.image.load("UI\Helper\Letter keys\letter_m.png")
            letterM_Key = pygame.transform.scale(letterM_Key, (50, 50))
            gameDisplay.blit(letterM_Key, (450, 350))

            p2_atk_text = pygame.image.load("UI\Helper\P2_ATK.png")
            p2_atk_text = pygame.transform.scale(p2_atk_text, (200, 200))
            gameDisplay.blit(p2_atk_text, (500, 280))

            #back
            left_arrow = pygame.image.load("UI\Symbols & Text\SYMB_LEFTARROW.png")
            gameDisplay.blit(left_arrow, (10, 520))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                print(mPos)
                print(mPress)
                
                if event.type == pygame.QUIT:
                    gameExit = True
                    
                if ((mPos[0] >= 10 and mPos[0] <= 100 and mPos[1] >= 520
                     and mPos[1] <= 580) and mPress == 1):
                    print("Back")
                    Fighter_Game().menu()
                    
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()

    def menu(self):
        self.mainMenu = True
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('2 Fighter')
        headPic = pygame.image.load("UI\Symbols & Text\Head.png")
        headPic = pygame.transform.scale(headPic, (500, 300))
        gameDisplay.blit(headPic, (175, 50))
        
        startButton = pygame.image.load("UI\Symbols & Text\TEXT_START.png")
        gameDisplay.blit(startButton, (275, 300))
        
        helpButton = pygame.image.load("UI\Symbols & Text\TEXT_HELP.png")
        gameDisplay.blit(helpButton, (300, 400))
        
        exitButton = pygame.image.load("UI\Symbols & Text\SYMB_ BIGX.png")
        gameDisplay.blit(exitButton, (710, 515))
        pygame.display.update()
        
        while not self.gameExit:
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                print(mPos)
                print(mPress)
                if event.type == pygame.QUIT:
                    self.gameExit = True
                        
                if (self.mainMenu == True and (mPos[0] >= 275 and mPos[0] <= 516
                                          and mPos[1] >= 300 and mPos[1] <= 350) and mPress == 1):                
                    print("Start")
                    self.mainMenu = False
                    Fighter_Game().startGame()
                    
                if (self.mainMenu == True and (mPos[0] >= 300 and mPos[0] <= 495
                                          and mPos[1] >= 400 and mPos[1] <= 451) and mPress == 1):
                    print("Helper")
                    self.mainMenu = False
                    Fighter_Game().gameHelper()
                    
                if (self.mainMenu == True and (mPos[0] >= 710 and mPos[0] <= 790
                                          and mPos[1] >= 515 and mPos[1] <= 591) and mPress == 1):
                    print("Exit")
                    self.mainMenu = False
                    self.gameExit = True

                
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()


Fighter_Game().menu()

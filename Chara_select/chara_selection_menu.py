import pygame
import time

class Select_Character_Stage:
    def __init__(self):
        pygame.init()
        self.white =(255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.display_width = 800
        self.display_height = 600
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.font = pygame.font.SysFont(None, 25)
        self.p1_character = 0
        self.p2_character = 0
        self.stage = 0
        self.gameExit = False

    def character_select_menu(self):
        self.gameExit = False
        
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Character Selection')
        
        while not self.gameExit:
            elentriana = pygame.image.load("Elentriana\stand1_0.png")#red hair girl
            elentriana = pygame.transform.scale(elentriana, (150,150))
            gameDisplay.blit(elentriana, (0,5))

            zalana = pygame.image.load("Zalana\stand1_0.png")#pink hair girl
            zalana = pygame.transform.scale(zalana, (150,150))
            gameDisplay.blit(zalana, (200,20))

            shaca = pygame.image.load("Shaca\stand1_0.png")#yellow hair girl
            shaca = pygame.transform.scale(shaca, (150,150))
            gameDisplay.blit(shaca, (350,15))

            kazuki = pygame.image.load("Kazuki\stand1_0.png")#black hair man
            kazuki = pygame.transform.scale(kazuki, (150,150))
            gameDisplay.blit(kazuki, (500,0))

            lucifer = pygame.image.load("Lucifer\stand1_0.png")#silver hair demon
            lucifer = pygame.transform.scale(lucifer, (150,150))
            gameDisplay.blit(lucifer, (500,0))

            refaian = pygame.image.load("Refaian\stand1_0.png")#oriharukon knight with broken blade
            refaian = pygame.transform.scale(refaian, (150,150))
            gameDisplay.blit(refaian, (500,0))

            select_button = pygame.image.load("text\Select.png")
            gameDisplay.blit(select_button, (700,530))

            pygame.display.update()
            
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                print(mPos)
                print(mPress)
                if event.type == pygame.QUIT:
                    self.gameExit = True

                #Elentriana__________    
                if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):                
                    print("Elentriana")
                    gameDisplay.fill(self.black)
                    elentrianaShow = pygame.image.load("Elentriana\stand1_0.png")#Real one shows small block of character
                    elentrianaShow = pygame.transform.scale(elentrianaShow, (300,300))
                    gameDisplay.blit(elentrianaShow, (100,200))
                    
                    profile_show = pygame.image.load("Elentriana\stand1_0.png")#show unknown(Question Mark)picture while current has no pic. [Real one is full profile of character show].
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))
                    
                    pygame.display.update()
                    self.p1_character = 1

                #Zalana__________                        
                if ((mPos[0] >= 200 and mPos[0] <= 300 and mPos[1] >= 25
                     and mPos[1] <= 140) and mPress == 1):
                    print("Zalana")
                    gameDisplay.fill(self.black)
                    zalanaShow = pygame.image.load("Zalana\stand1_0.png")
                    zalanaShow = pygame.transform.scale(zalanaShow, (200,300))
                    gameDisplay.blit(zalanaShow, (200,200))
                    
                    profile_show = pygame.image.load("Zalana\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))
                    
                    pygame.display.update()
                    self.p1_character = 2

                #Shaca__________    
                if ((mPos[0] >= 385 and mPos[0] <= 455 and mPos[1] >= 35
                     and mPos[1] <= 145) and mPress == 1):
                    print("Shaca")
                    gameDisplay.fill(self.black)
                    shacaShow = pygame.image.load("Shaca\stand1_0.png")
                    shacaShow = pygame.transform.scale(shacaShow, (300,300))
                    gameDisplay.blit(shacaShow, (200,200))

                    profile_show = pygame.image.load("Shaca\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))
                    
                    pygame.display.update()
                    self.p1_character = 3

                #Kazuki__________    
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Kazuki")
                    gameDisplay.fill(self.black)
                    kazukiShow = pygame.image.load("Kazuki\stand1_0.png")
                    kazukiShow = pygame.transform.scale(kazukiShow, (300,300))
                    gameDisplay.blit(kazukiShow, (150,200))

                    profile_show = pygame.image.load("Kazuki\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))

                    pygame.display.update()
                    self.p1_character = 4

                #Lucifer__________
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Lucifer")
                    gameDisplay.fill(self.black)
                    luciferShow = pygame.image.load("Lucifer\stand1_0.png")
                    luciferShow = pygame.transform.scale(luciferShow, (300,300))
                    gameDisplay.blit(luciferShow, (150,200))

                    profile_show = pygame.image.load("Lucifer\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))

                    pygame.display.update()
                    self.p1_character = 5

                #Refaian__________
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Refaian")
                    gameDisplay.fill(self.black)
                    refaianShow = pygame.image.load("Refaian\stand1_0.png")
                    refaianShow = pygame.transform.scale(refaianShow, (300,300))
                    gameDisplay.blit(refaianShow, (150,200))

                    profile_show = pygame.image.load("Refaian\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (50,50))
                    gameDisplay.blit(profile_show, (500,300))

                    pygame.display.update()
                    self.p1_character = 6

                #Select Button__________
                if ((mPos[0] >= 700 and mPos[0] <= 795 and mPos[1] >= 530
                     and mPos[1] <= 585) and mPress == 1 and self.p1_character != 0):
                    print("You have selected a character!")
                    print(self.p1_character)
                    
                    
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()
Select_Character_Stage()#How to run this?

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
        
        self.display_width = 1280
        self.display_height = 768
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Character Selection')
        
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.font = pygame.font.SysFont(None, 25)
        self.p1_character = 0
        self.p2_character = 0
        self.stage = 0
        self.gameExit = False

    def P1_character_select_menu(self):
        self.gameExit = False

        while not self.gameExit:
            select_your_character = pygame.image.load("text\Select-Your-Character.png")#Show this text in the middle of the screen.
            #select_your_character = pygame.transform.scale(select_your_character, (300,300))
            self.gameDisplay.blit(select_your_character, (390,55))
            
            elentriana = pygame.image.load("Elentriana\stand1_0.png")#red hair girl
            elentriana = pygame.transform.scale(elentriana, (150,150))
            self.gameDisplay.blit(elentriana, (143,421))

            zalana = pygame.image.load("Zalana\stand1_0.png")#pink hair girl
            zalana = pygame.transform.scale(zalana, (150,150))
            self.gameDisplay.blit(zalana, (250,421))

            shaca = pygame.image.load("Shaca\stand1_0.png")#yellow hair girl
            shaca = pygame.transform.scale(shaca, (150,150))
            self.gameDisplay.blit(shaca, (357,421))

            kazuki = pygame.image.load("Kazuki\stand1_0.png")#black hair man
            kazuki = pygame.transform.scale(kazuki, (150,150))
            self.gameDisplay.blit(kazuki, (464,421))

            lucifer = pygame.image.load("Lucifer\stand1_0.png")#silver hair demon
            lucifer = pygame.transform.scale(lucifer, (150,150))
            self.gameDisplay.blit(lucifer, (571,421))

            refaian = pygame.image.load("Refaian\stand1_0.png")#oriharukon knight with broken blade
            refaian = pygame.transform.scale(refaian, (150,150))
            self.gameDisplay.blit(refaian, (678,421))

            select_button = pygame.image.load("text\Select.png")#confirm selecting character button
            self.gameDisplay.blit(select_button, (380,555))

            pygame.display.update()
            
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                print(mPos)
                print(mPress)
                if event.type == pygame.QUIT:
                    self.gameExit = True

                #Elentriana----------    
                if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):                
                    print("Elentriana")
                    self.gameDisplay.fill(self.black)
                    elentrianaShow = pygame.image.load("Elentriana\stand1_0.png")#Real one shows character artwork.
                    elentrianaShow = pygame.transform.scale(elentrianaShow, (300,300))
                    self.gameDisplay.blit(elentrianaShow, (248,281))
                    
                    profile_show = pygame.image.load("Elentriana\stand1_0.png")#Real one is full profile of character show.
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,261))
                    
                    pygame.display.update()
                    self.p1_character = 1

                #Zalana----------                        
                if ((mPos[0] >= 200 and mPos[0] <= 300 and mPos[1] >= 25
                     and mPos[1] <= 140) and mPress == 1):
                    print("Zalana")
                    self.gameDisplay.fill(self.black)
                    zalanaShow = pygame.image.load("Zalana\stand1_0.png")
                    zalanaShow = pygame.transform.scale(zalanaShow, (300,300))
                    self.gameDisplay.blit(zalanaShow, (248,281))
                    
                    profile_show = pygame.image.load("Zalana\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))
                    
                    pygame.display.update()
                    self.p1_character = 2

                #Shaca----------    
                if ((mPos[0] >= 385 and mPos[0] <= 455 and mPos[1] >= 35
                     and mPos[1] <= 145) and mPress == 1):
                    print("Shaca")
                    self.gameDisplay.fill(self.black)
                    shacaShow = pygame.image.load("Shaca\stand1_0.png")
                    shacaShow = pygame.transform.scale(shacaShow, (300,300))
                    self.gameDisplay.blit(shacaShow, (248,281))

                    profile_show = pygame.image.load("Shaca\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))
                    
                    pygame.display.update()
                    self.p1_character = 3

                #Kazuki----------    
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Kazuki")
                    self.gameDisplay.fill(self.black)
                    kazukiShow = pygame.image.load("Kazuki\stand1_0.png")
                    kazukiShow = pygame.transform.scale(kazukiShow, (300,300))
                    self.gameDisplay.blit(kazukiShow, (248,281))

                    profile_show = pygame.image.load("Kazuki\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p1_character = 4

                #Lucifer----------
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Lucifer")
                    self.gameDisplay.fill(self.black)
                    luciferShow = pygame.image.load("Lucifer\stand1_0.png")
                    luciferShow = pygame.transform.scale(luciferShow, (300,300))
                    self.gameDisplay.blit(luciferShow, (248,281))

                    profile_show = pygame.image.load("Lucifer\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p1_character = 5

                #Refaian----------
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Refaian")
                    self.gameDisplay.fill(self.black)
                    refaianShow = pygame.image.load("Refaian\stand1_0.png")
                    refaianShow = pygame.transform.scale(refaianShow, (300,300))
                    self.gameDisplay.blit(refaianShow, (248,281))

                    profile_show = pygame.image.load("Refaian\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p1_character = 6

                #Select Button----------
                if ((mPos[0] >= 700 and mPos[0] <= 795 and mPos[1] >= 530
                     and mPos[1] <= 585) and mPress == 1 and self.p1_character != 0):
                    p1_show = pygame.image.load("text\P1.png")
                    p1_show = pygame.transform.scale(p1_show, (30,30))
                    if self.p1_character == 1:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (143,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 2:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (250,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 3:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (357,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 4:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (464,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 5:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (571,421))
                        pygame.display.update()
                    elif self.p1_character == 6:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p1_show, (678,421))
                        pygame.display.update()

                    print("You have selected a character!")
                    print(self.p1_character)


    def P2_character_select_menu(self):
        self.gameExit = False

        while not self.gameExit:
            select_your_character = pygame.image.load("text\Select-Your-Character.png")#Show this text in the middle of the screen.
            select_your_character = pygame.transform.scale(select_your_character, (300,300))
            self.gameDisplay.blit(select_your_character, (390,55))
            
            elentriana = pygame.image.load("Elentriana\stand1_0.png")#red hair girl
            elentriana = pygame.transform.scale(elentriana, (150,150))
            self.gameDisplay.blit(elentriana, (143,421))

            zalana = pygame.image.load("Zalana\stand1_0.png")#pink hair girl
            zalana = pygame.transform.scale(zalana, (150,150))
            self.gameDisplay.blit(zalana, (250,421))

            shaca = pygame.image.load("Shaca\stand1_0.png")#yellow hair girl
            shaca = pygame.transform.scale(shaca, (150,150))
            self.gameDisplay.blit(shaca, (357,421))

            kazuki = pygame.image.load("Kazuki\stand1_0.png")#black hair man
            kazuki = pygame.transform.scale(kazuki, (150,150))
            self.gameDisplay.blit(kazuki, (464,421))

            lucifer = pygame.image.load("Lucifer\stand1_0.png")#silver hair demon
            lucifer = pygame.transform.scale(lucifer, (150,150))
            self.gameDisplay.blit(lucifer, (571,421))

            refaian = pygame.image.load("Refaian\stand1_0.png")#oriharukon knight with broken blade
            refaian = pygame.transform.scale(refaian, (150,150))
            self.gameDisplay.blit(refaian, (678,421))

            select_button = pygame.image.load("text\Select.png")
            self.gameDisplay.blit(select_button, (380,555))

            pygame.display.update()
            
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                print(mPos)
                print(mPress)
                if event.type == pygame.QUIT:
                    self.gameExit = True

                #Elentriana----------    
                if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):                
                    print("Elentriana")
                    self.gameDisplay.fill(self.black)
                    elentrianaShow = pygame.image.load("Elentriana\stand1_0.png")#Real one shows character artwork.
                    elentrianaShow = pygame.transform.scale(elentrianaShow, (300,300))
                    self.gameDisplay.blit(elentrianaShow, (248,281))
                    
                    profile_show = pygame.image.load("Elentriana\stand1_0.png")#Real one is full profile of character show.
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,261))
                    
                    pygame.display.update()
                    self.p2_character = 1

                #Zalana----------                        
                if ((mPos[0] >= 200 and mPos[0] <= 300 and mPos[1] >= 25
                     and mPos[1] <= 140) and mPress == 1):
                    print("Zalana")
                    self.gameDisplay.fill(self.black)
                    zalanaShow = pygame.image.load("Zalana\stand1_0.png")
                    zalanaShow = pygame.transform.scale(zalanaShow, (300,300))
                    self.gameDisplay.blit(zalanaShow, (248,281))
                    
                    profile_show = pygame.image.load("Zalana\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))
                    
                    pygame.display.update()
                    self.p2_character = 2

                #Shaca----------    
                if ((mPos[0] >= 385 and mPos[0] <= 455 and mPos[1] >= 35
                     and mPos[1] <= 145) and mPress == 1):
                    print("Shaca")
                    self.gameDisplay.fill(self.black)
                    shacaShow = pygame.image.load("Shaca\stand1_0.png")
                    shacaShow = pygame.transform.scale(shacaShow, (300,300))
                    self.gameDisplay.blit(shacaShow, (248,281))

                    profile_show = pygame.image.load("Shaca\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))
                    
                    pygame.display.update()
                    self.p2_character = 3

                #Kazuki----------    
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Kazuki")
                    self.gameDisplay.fill(self.black)
                    kazukiShow = pygame.image.load("Kazuki\stand1_0.png")
                    kazukiShow = pygame.transform.scale(kazukiShow, (300,300))
                    self.gameDisplay.blit(kazukiShow, (248,281))

                    profile_show = pygame.image.load("Kazuki\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p2_character = 4

                #Lucifer----------
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Lucifer")
                    self.gameDisplay.fill(self.black)
                    luciferShow = pygame.image.load("Lucifer\stand1_0.png")
                    luciferShow = pygame.transform.scale(luciferShow, (300,300))
                    self.gameDisplay.blit(luciferShow, (248,281))

                    profile_show = pygame.image.load("Lucifer\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p2_character = 5

                #Refaian----------
                if ((mPos[0] >= 530 and mPos[0] <= 655 and mPos[1] >= 10
                     and mPos[1] <= 150) and mPress == 1):
                    print("Refaian")
                    self.gameDisplay.fill(self.black)
                    refaianShow = pygame.image.load("Refaian\stand1_0.png")
                    refaianShow = pygame.transform.scale(refaianShow, (300,300))
                    self.gameDisplay.blit(refaianShow, (248,281))

                    profile_show = pygame.image.load("Refaian\stand1_0.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (500,281))

                    pygame.display.update()
                    self.p2_character = 6

                #Select Button----------
                if ((mPos[0] >= 700 and mPos[0] <= 795 and mPos[1] >= 530
                     and mPos[1] <= 585) and mPress == 1 and self.p2_character != 0):
                    p2_show = pygame.image.load("text\P2.png")
                    p2_show = pygame.transform.scale(p2_show, (30,30))
                    if self.p1_character == 1:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (143,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 2:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (250,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 3:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (357,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 4:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (464,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 5:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (571,421))
                        pygame.display.update()
                                         
                    elif self.p1_character == 6:
                        if ((mPos[0] >= 30 and mPos[0] <= 131 and mPos[1] >= 42
                     and mPos[1] <= 135) and mPress == 1):
                            pass
                        self.gameDisplay.blit(p2_show, (678,421))
                        pygame.display.update()
                    print("You have selected a character!")
                    print(self.p2_character)
                    
                    
        self.clock.tick(self.FPS)

        pygame.quit()
        quit()

    def main(self):
        Select_Character_Stage().P1_character_select_menu()
            
Select_Character_Stage().main()#can run but show only black screen and freeze, can't do anything even close.

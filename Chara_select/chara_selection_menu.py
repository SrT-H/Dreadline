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
        self.lightskyblue = (135,206,250)
        
        self.display_width = 1280
        self.display_height = 768
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Character Selection')
        self.gameDisplay.fill(self.lightskyblue)
        
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.font = pygame.font.SysFont(None, 25)
        self.p1_character = 0
        self.p2_character = 0
        self.p1_character_pick = 0
        self.p2_character_pick = 0
        self.stage = 0
        self.gameExit = False

    def p1_character_select_menu(self):
        self.gameExit = False
        Elentriana = True
        Zalana = True
        Shaca = True
        Kazuki = True
        Lucifer = True
        Refaian = True

        while not self.gameExit:
            select_your_character = pygame.image.load("text\Select-Your-Character.png")#Show this text in the middle of the screen.
            select_your_character = pygame.transform.scale(select_your_character, (800,50))
            self.gameDisplay.blit(select_your_character, (235,30))

            if Elentriana:
                elentriana = pygame.image.load("Pic\Chara.png")#red hair girl
                elentriana = pygame.transform.scale(elentriana, (100,100))
                self.gameDisplay.blit(elentriana, (330,498))

            if Zalana:
                zalana = pygame.image.load("Pic\Chara.png")#pink hair girl
                zalana = pygame.transform.scale(zalana, (100,100))
                self.gameDisplay.blit(zalana, (430,498))

            if Shaca:
                shaca = pygame.image.load("Pic\Chara.png")#yellow hair girl
                shaca = pygame.transform.scale(shaca, (100,100))
                self.gameDisplay.blit(shaca, (530,498))

            if Kazuki:
                kazuki = pygame.image.load("Pic\Chara.png")#black hair man
                kazuki = pygame.transform.scale(kazuki, (100,100))
                self.gameDisplay.blit(kazuki, (630,498))

            if Lucifer:
                lucifer = pygame.image.load("Pic\Chara.png")#silver hair demon
                lucifer = pygame.transform.scale(lucifer, (100,100))
                self.gameDisplay.blit(lucifer, (730,498))

            if Refaian:
                refaian = pygame.image.load("Pic\Chara.png")#oriharukon knight with broken blade
                refaian = pygame.transform.scale(refaian, (100,100))
                self.gameDisplay.blit(refaian, (830,498))

            select_button = pygame.image.load("text\Select.png")#confirm selecting character button
            self.gameDisplay.blit(select_button, (555,640))

            pygame.display.update()
            
            for event in pygame.event.get():
                print(event)
                mPos = pygame.mouse.get_pos()
                mPress = pygame.mouse.get_pressed()[0]
                #print(mPos)
                #print(mPress)
                if event.type == pygame.QUIT:
                    self.gameExit = True

                #Elentriana----------    
                if ((mPos[0] >= 330 and mPos[0] <= 429 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):                
                    print("Elentriana")
                    self.gameDisplay.fill(self.lightskyblue)
                    elentrianaShow = pygame.image.load("Pic\Chara.png")#Real one shows character artwork.
                    elentrianaShow = pygame.transform.scale(elentrianaShow, (300,300))
                    self.gameDisplay.blit(elentrianaShow, (330,135))
                    
                    profile_show = pygame.image.load("Pic\Chara.png")#Real one is full profile of character show.
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 1

                #Zalana----------                        
                if ((mPos[0] >= 430 and mPos[0] <= 529 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Zalana")
                    self.gameDisplay.fill(self.lightskyblue)
                    zalanaShow = pygame.image.load("Pic\Chara.png")
                    zalanaShow = pygame.transform.scale(zalanaShow, (300,300))
                    self.gameDisplay.blit(zalanaShow, (330,135))
                    
                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 2

                #Shaca----------    
                if ((mPos[0] >= 530 and mPos[0] <= 629 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Shaca")
                    self.gameDisplay.fill(self.lightskyblue)
                    shacaShow = pygame.image.load("Pic\Chara.png")
                    shacaShow = pygame.transform.scale(shacaShow, (300,300))
                    self.gameDisplay.blit(shacaShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 3

                #Kazuki----------    
                if ((mPos[0] >= 630 and mPos[0] <= 729 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Kazuki")
                    self.gameDisplay.fill(self.lightskyblue)
                    kazukiShow = pygame.image.load("Pic\Chara.png")
                    kazukiShow = pygame.transform.scale(kazukiShow, (300,300))
                    self.gameDisplay.blit(kazukiShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 4

                #Lucifer----------
                if ((mPos[0] >= 730 and mPos[0] <= 829 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Lucifer")
                    self.gameDisplay.fill(self.lightskyblue)
                    luciferShow = pygame.image.load("Pic\Chara.png")
                    luciferShow = pygame.transform.scale(luciferShow, (300,300))
                    self.gameDisplay.blit(luciferShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 5

                #Refaian----------
                if ((mPos[0] >= 830 and mPos[0] <= 930 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Refaian")
                    self.gameDisplay.fill(self.lightskyblue)
                    refaianShow = pygame.image.load("Pic\Chara.png")
                    refaianShow = pygame.transform.scale(refaianShow, (300,300))
                    self.gameDisplay.blit(refaianShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 6

                #Select Button----------
                if ((mPos[0] >= 555 and mPos[0] <= 700 and mPos[1] >= 640
                     and mPos[1] <= 681) and mPress == 1 and self.p1_character != 0):
                    p1_show = pygame.image.load("text\P1.png")
                    p1_show = pygame.transform.scale(p1_show, (30,30))
                    
                    if self.p1_character == 1:
                        self.gameDisplay.blit(p1_show, (368,536))
                        Elentriana = False
                                         
                    elif self.p1_character == 2:
                        self.gameDisplay.blit(p1_show, (468,536))
                        Zalana = False
                                         
                    elif self.p1_character == 3:
                        self.gameDisplay.blit(p1_show, (568,536))
                        Shaca = False
                                         
                    elif self.p1_character == 4:
                        self.gameDisplay.blit(p1_show, (668,536))
                        Kazuki = False
                                         
                    elif self.p1_character == 5:
                        self.gameDisplay.blit(p1_show, (768,536))
                        Lucifer = False
                        
                    elif self.p1_character == 6:
                        self.gameDisplay.blit(p1_show, (868,536))
                        Refaian = False
                    #Select_Character_Stage().p2_character_select_menu()

                    pygame.display.update()

                    print("You have selected a character!")
                    print(self.p1_character)


    def p2_character_select_menu(self):
        self.gameExit = False
        Elentriana = True
        Zalana = True
        Shaca = True
        Kazuki = True
        Lucifer = True
        Refaian = True

        while not self.gameExit:
            select_your_character = pygame.image.load("text\Select-Your-Character.png")#Show this text in the middle of the screen.
            select_your_character = pygame.transform.scale(select_your_character, (800,50))
            self.gameDisplay.blit(select_your_character, (235,30))

            if Elentriana:
                elentriana = pygame.image.load("Pic\Chara.png")#red hair girl
                elentriana = pygame.transform.scale(elentriana, (100,100))
                self.gameDisplay.blit(elentriana, (330,498))

            if Zalana:
                zalana = pygame.image.load("Pic\Chara.png")#pink hair girl
                zalana = pygame.transform.scale(zalana, (100,100))
                self.gameDisplay.blit(zalana, (430,498))

            if Shaca:
                shaca = pygame.image.load("Pic\Chara.png")#yellow hair girl
                shaca = pygame.transform.scale(shaca, (100,100))
                self.gameDisplay.blit(shaca, (530,498))

            if Kazuki:
                kazuki = pygame.image.load("Pic\Chara.png")#black hair man
                kazuki = pygame.transform.scale(kazuki, (100,100))
                self.gameDisplay.blit(kazuki, (630,498))

            if Lucifer:
                lucifer = pygame.image.load("Pic\Chara.png")#silver hair demon
                lucifer = pygame.transform.scale(lucifer, (100,100))
                self.gameDisplay.blit(lucifer, (730,498))

            if Refaian:
                refaian = pygame.image.load("Pic\Chara.png")#oriharukon knight with broken blade
                refaian = pygame.transform.scale(refaian, (100,100))
                self.gameDisplay.blit(refaian, (830,498))

            select_button = pygame.image.load("text\Select.png")#confirm selecting character button
            self.gameDisplay.blit(select_button, (555,640))

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
                if ((mPos[0] >= 330 and mPos[0] <= 429 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):                
                    print("Elentriana")
                    self.gameDisplay.fill(self.lightskyblue)
                    elentrianaShow = pygame.image.load("Pic\Chara.png")#Real one shows character artwork.
                    elentrianaShow = pygame.transform.scale(elentrianaShow, (300,300))
                    self.gameDisplay.blit(elentrianaShow, (330,135))
                    
                    profile_show = pygame.image.load("Pic\Chara.png")#Real one is full profile of character show.
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 1

                #Zalana----------                        
                if ((mPos[0] >= 430 and mPos[0] <= 529 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Zalana")
                    self.gameDisplay.fill(self.lightskyblue)
                    zalanaShow = pygame.image.load("Pic\Chara.png")
                    zalanaShow = pygame.transform.scale(zalanaShow, (300,300))
                    self.gameDisplay.blit(zalanaShow, (330,135))
                    
                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 2

                #Shaca----------    
                if ((mPos[0] >= 530 and mPos[0] <= 629 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Shaca")
                    self.gameDisplay.fill(self.lightskyblue)
                    shacaShow = pygame.image.load("Pic\Chara.png")
                    shacaShow = pygame.transform.scale(shacaShow, (300,300))
                    self.gameDisplay.blit(shacaShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))
                    
                    pygame.display.update()
                    self.p1_character = 3

                #Kazuki----------    
                if ((mPos[0] >= 630 and mPos[0] <= 729 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Kazuki")
                    self.gameDisplay.fill(self.lightskyblue)
                    kazukiShow = pygame.image.load("Pic\Chara.png")
                    kazukiShow = pygame.transform.scale(kazukiShow, (300,300))
                    self.gameDisplay.blit(kazukiShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 4

                #Lucifer----------
                if ((mPos[0] >= 730 and mPos[0] <= 829 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Lucifer")
                    self.gameDisplay.fill(self.lightskyblue)
                    luciferShow = pygame.image.load("Pic\Chara.png")
                    luciferShow = pygame.transform.scale(luciferShow, (300,300))
                    self.gameDisplay.blit(luciferShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 5

                #Refaian----------
                if ((mPos[0] >= 830 and mPos[0] <= 930 and mPos[1] >= 498
                     and mPos[1] <= 598) and mPress == 1):
                    print("Refaian")
                    self.gameDisplay.fill(self.lightskyblue)
                    refaianShow = pygame.image.load("Pic\Chara.png")
                    refaianShow = pygame.transform.scale(refaianShow, (300,300))
                    self.gameDisplay.blit(refaianShow, (330,135))

                    profile_show = pygame.image.load("Pic\Chara.png")
                    profile_show = pygame.transform.scale(profile_show, (300,300))
                    self.gameDisplay.blit(profile_show, (630,135))

                    pygame.display.update()
                    self.p1_character = 6

                #Select Button----------
                if ((mPos[0] >= 555 and mPos[0] <= 700 and mPos[1] >= 640
                     and mPos[1] <= 681) and mPress == 1 and self.p1_character != 0):
                    p1_show = pygame.image.load("text\P1.png")
                    p1_show = pygame.transform.scale(p1_show, (30,30))
                    
                    if self.p1_character == 1:
                        self.gameDisplay.blit(p1_show, (368,536))
                        Elentriana = False
                                         
                    elif self.p1_character == 2:
                        self.gameDisplay.blit(p1_show, (468,536))
                        Zalana = False
                                         
                    elif self.p1_character == 3:
                        self.gameDisplay.blit(p1_show, (568,536))
                        Shaca = False
                                         
                    elif self.p1_character == 4:
                        self.gameDisplay.blit(p1_show, (668,536))
                        Kazuki = False
                                         
                    elif self.p1_character == 5:
                        self.gameDisplay.blit(p1_show, (768,536))
                        Lucifer = False
                        
                    elif self.p1_character == 6:
                        self.gameDisplay.blit(p1_show, (868,536))
                        Refaian = False
                    #Select_Character_Stage().p1_character_select_menu()

                    pygame.display.update()
                    
                    print("You have selected a character!")
                    print(self.p2_character)
                    
                    
        #self.clock.tick(self.FPS)

        #pygame.quit()
        #quit()

    def main(self):
        Select_Character_Stage().p1_character_select_menu()#.p2_character_select_menu()
            
Select_Character_Stage().main()

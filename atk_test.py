import sys, pygame, glob, time, os
pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class player_1:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        #self.img = pygame.image.load(self.ani[0])
        #self.img = pygame.transform.flip(self.img, 100, 0)
        #self.update(0)

    def set_pic_location(self, location):
        self.ani = glob.glob(location)
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.update(0)

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def update(self, pos):
        if pos != 0:
            self.ani_speed -= 1
            self.x += pos
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.img = pygame.transform.flip(self.img, 100, 0)
                self.ani_speed = self.ani_speed_init
                if self.ani_pos >= self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
        #screen.blit(self.img, (self.x, self.y))
    
    def atk(self):
        ani_pos = 0
        self.ani = glob.glob("")
        self.img = pygame.image.load(self.ani[ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani)-1
        time_delay = 0
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            time_delay = 200
            ani_pos += 1
            #screen.fill(black)
            #screen.blit(self.img, (self.x, self.y))
            #pygame.display.update()
    
        self.ani = glob.glob("")
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani)-1

    def idle(self):
        ani_pos = 0
        self.img = pygame.transform.flip(self.img, 100, 0)
        time_delay = 200
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            ani_pos += 1
            #screen.fill(black)
            #screen.blit(self.img, (self.x, self.y))
            #pygame.display.update()

    def render(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.display.update()
#-----------------------------------------------------------------------
class player_2:
    def __init__(self):
        self.x = 300
        self.y = 500
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.update(0)

    def update_location(self, location):
        self.ani = glob.glob(location)

    def update(self, pos):
        if pos != 0:
            self.ani_speed -= 1
            self.x += pos
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.img = pygame.transform.flip(self.img, 100, 0)
                self.ani_speed = self.ani_speed_init
                if self.ani_pos >= self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
        #screen.blit(self.img, (self.x, self.y))

    def atk(self):
        ani_pos = 0
        self.ani = glob.glob("Picture\\Character\\Female_2\\default\\0\\stabOF_*.png")
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
            #screen.fill(black)
            #screen.blit(self.img, (self.x, self.y))
            #pygame.display.update()

    def idle(self):
        ani_pos = 0
        self.img = pygame.transform.flip(self.img, 100, 0)
        time_delay = 200
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            ani_pos += 1
            #screen.fill(black)
            #screen.blit(self.img, (self.x, self.y))
            #pygame.display.update()

#----- PIC LOCATION -----
def character_location(num):
    if num == 1:
        txt = "Picture\\Character\\Female_1\\default\\0\\stand1_*.png"
    elif num == 2:
        txt = "Picture\\Character\\Female_2\\default\\0\\stand1_*.png"
    elif num == 3:
        txt = "Picture\\Character\\Female_3\\default\\0\\stand1_*.png"
    elif num == 4:
        txt = "Picture\\Character\\Male_1\\default\\0\\stand1_*.png"
    elif num == 5:
        txt = "Picture\\Character\\Male_2\\default\\0\\stand1_*.png"
    elif num == 6:
        txt = "Picture\\Character\\Male_3\\default\\0\\stand1_*.png"
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

#====== MAIN ======
def  main():
    player1 = player_1()
    player1.set_pic_location(character_location(1))
    player1.set_xy(200, 100)
    #player2 = player_2()
    pos = 0

    while True:
        #screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                player1.atk()
            '''
            elif event.type == pygame.KEYDOWN and event.key ==  pygame.K_RIGHT:
                pos = 1
            elif event.type ==  pygame.KEYUP and event.key ==  pygame.K_RIGHT:
                pos = 0
            elif event.type == pygame.KEYDOWN and event.key ==  pygame.K_LEFT:
                pos = -1
            elif event.type ==  pygame.KEYUP and event.key ==  pygame.K_LEFT:
                pos = 0'''


        #player2.idle()
        screen.fill(black)
        player1.idle()
        player1.update(pos)
        player1.render()
        #player2.update(pos)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

main()
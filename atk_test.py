import sys, pygame, glob, time, os
pygame.init()

size = width, height = 1280, 720
black = 0,0,0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class player:
    def __init__(self):
        self.x = 800
        self.y = 300
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("Picture\\Character\\Female_1\\default\\0\\stand1_*.png")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.img = pygame.image.load(self.ani[0])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.update(0)

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
        screen.blit(self.img,(self.x, self.y))
    
    def atk(self):
        ani_pos = 0
        self.ani = glob.glob("Picture\\Character\\Female_1\\default\\0\\stabOF_*.png")
        self.img = pygame.image.load(self.ani[ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani)-1
        time_delay = 200
        while ani_pos <= self.ani_max:
            self.img = pygame.image.load(self.ani[ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            pygame.time.delay(time_delay)
            ani_pos += 1
            screen.fill(black)
            screen.blit(self.img, (self.x, self.y))
            pygame.display.update()
    
        self.ani = glob.glob("Picture\\Character\\Female_1\\default\\0\\walk1_*.png")
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
            screen.fill(black)
            screen.blit(self.img, (self.x, self.y))
            pygame.display.update()
        
#-----------------------------        
player1 = player()
pos = 0
    
while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type ==  pygame.KEYUP and event.key ==  pygame.K_UP:
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
       

    player1.idle()      
    player1.update(pos)
    
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()

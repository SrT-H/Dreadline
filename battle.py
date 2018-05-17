import pygame, sys, glob, time, os, random

os.environ['SDL_VIDEO_CENTERED'] = '1'
gameDisplay = pygame.display.set_mode((1280, 720))

black = (0, 0, 0)
white = (255, 255, 255)

pygame.display.set_caption('D R E A D L I N E ')
bg = pygame.image.load("Picture\\BG\\background.png")
bg = pygame.transform.scale(bg, (1280, 720))
gameDisplay.blit(bg, (0, 0))
pygame.draw.rect(gameDisplay, white, [100, 200, 400, 500])
pygame.display.update()

'''============================ CLASS ============================'''
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
        self.die = False
        self.temp = 0

    #update
    def updated(self, pos):
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
            self.img = pygame.transform.flip(self.img, 100, 0)
            self.ani_speed = self.ani_speed_init
            if self.ani_pos >= self.ani_max:
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
        self.updated(0)

    #set status
    def set_status(self, lst):
        self.name = lst[0]
        self.max_hp = lst[1]
        self.hp = lst[1]
        self.ap = lst[2]
        self.dp = lst[3]

    #name
    def name_display(self, x, y, color = (255, 215, 0)):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render(str(self.name), True, color)
        gameDisplay.blit(text, (x, y))

    #status bar
    def status_bar(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text1 = myfont.render('AP: ' + str(self.ap), True, (225, 0, 0))
        text2 = myfont.render('  DP: '+ str(self.dp), True, (0, 200, 225))
        gameDisplay.blit(text1, (x, y))
        gameDisplay.blit(text2, (x+80, y))

    # health
    def health(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('HP: ' + str(self.hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    '''
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
            #gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(self.img, (self.x, self.y))
            pygame.display.update()

        self.img = pygame.image.load(self.ani[0])
        self.img = pygame.transform.flip(self.img, 100, 0)
        pygame.time.delay(time_delay)
        ani_pos += 1
        #gameDisplay.blit(bg, (0, 0))
        #self.updated(0)
        #gameDisplay.blit(self.img, (self.x, self.y))
        #pygame.display.update()

        self.ani_pos = 0
        self.ani = glob.glob(self.location)
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.img = pygame.transform.flip(self.img, 100, 0)
        self.ani_max = len(self.ani) - 1
    
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
            pygame.display.updated()
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
        self.die = False
        self.temp = 0

    #update
    def updated(self, pos):
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
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
        self.updated(0)

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

    #health
    def health(self, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('HP: ' +str(self.hp), True, (0, 225, 0))
        gameDisplay.blit(text, (x, y))

    '''
    #attack
    def atk(self):
        ani_pos = 0
        self.ani = glob.glob(self.atk_location)
        self.img = pygame.image.load(self.ani[ani_pos])
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

        self.img = pygame.image.load(self.ani[0])
        pygame.time.delay(time_delay)
        ani_pos += 1
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(self.img, (self.x, self.y))
        pygame.display.update()

        self.ani = glob.glob(self.location)
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.ani_max = len(self.ani) - 1

        
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
                pygame.display.updated()
            '''

'''============================ FUNCTION ============================'''
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

#----- DEAD PIC LOCATION -----
def dead_character_location(num):
    if num == 1:
        # Zalana
        txt = "Picture\\Character\\Female_1\\default\\0\\dead.png"
    elif num == 2:
        # Elentriana
        txt = "Picture\\Character\\Female_2\\default\\0\\dead.png"
    elif num == 3:
        # Shaca
        txt = "Picture\\Character\\Female_3\\default\\0\\dead.png"
    elif num == 4:
        # Kazuki
        txt = "Picture\\Character\\Male_1\\default\\0\\dead.png"
    elif num == 5:
        # Lucifer
        txt = "Picture\\Character\\Male_2\\default\\0\\dead.png"
    elif num == 6:
        # Refaian
        txt = "Picture\\Character\\Male_3\\default\\0\\dead.png"
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
def gameOver(winner):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 150)

    if winner == 1:
        text = myfont.render("PLAYER 1 WIN!", True, (255, 67, 67))
    else:
        text = myfont.render("PLAYER 2 WIN!", True, (255, 67, 67))

    myfont = pygame.font.SysFont('Comic Sans MS', 80)
    text2 = myfont.render("Press Y to EXIT.", True, (255, 67, 67))
    gameDisplay.blit(text, (640 - text.get_width() // 2, 360 - text.get_height() // 2))
    gameDisplay.blit(text2, ((640 - text.get_width() // 2)+200, (360 - text.get_height() // 2)+300))
    pygame.display.update()

#----- TURN -----
def show_turn(count):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)

    if count % 2 == 0:
        text = myfont.render("PLAYER 1", True, (255, 51, 255))
    else:
        text = myfont.render("PLAYER 2", True, (255, 51, 255))

    gameDisplay.blit(text, (530 , 20))
    pygame.display.update()

#------ SET CHARACTER ------
def set_character(n1, n2, n3, n4, n5, n6):
    global player_1_1, player_1_2, player_1_3, \
            player_2_1, player_2_2, player_2_3
    # 1 - 1
    player_1_1 = player1(200, 100)
    player_1_1.set_location(character_location(n1), character_location_atk(n1))
    player_1_1.set_status(get_status(n1))
    player_1_1.temp = n1
    # 1 - 2
    player_1_2 = player1(300, 250)
    player_1_2.set_location(character_location(n2), character_location_atk(n2))
    player_1_2.set_status(get_status(n2))
    player_1_2.temp = n2
    # 1 - 3
    player_1_3 = player1(200, 400)
    player_1_3.set_location(character_location(n3), character_location_atk(n3))
    player_1_3.set_status(get_status(n3))
    player_1_3.temp = n3

    # 2 - 1
    player_2_1 = player2(980, 100)
    player_2_1.set_location(character_location(n4), character_location_atk(n4))
    player_2_1.set_status(get_status(n4))
    player_2_1.temp = n4
    # 2 - 2
    player_2_2 = player2(880, 250)
    player_2_2.set_location(character_location(n5), character_location_atk(n5))
    player_2_2.set_status(get_status(n5))
    player_2_2.temp = n5
    # 2 - 3
    player_2_3 = player2(980, 400)
    player_2_3.set_location(character_location(n6), character_location_atk(n6))
    player_2_3.set_status(get_status(n6))
    player_2_3.temp = n6

#------ ALL RENDER ------
def all_render():
    # Background & Rect
    gameDisplay.blit(bg, (0, 0))
    pygame.draw.rect(gameDisplay, black, [30, 520, 450, 180])
    pygame.draw.rect(gameDisplay, black, [800, 520, 450, 180])

    # 1
    player_1_1.name_display(50, 550)
    player_1_1.health(165, 550)
    player_1_1.status_bar(280, 550)
    # 1 - 2
    player_1_2.name_display(50, 600)
    player_1_2.health(165, 600)
    player_1_2.status_bar(280, 600)
    # 1 - 3
    player_1_3.name_display(50, 650)
    player_1_3.health(165, 650)
    player_1_3.status_bar(280, 650)
    # 2 - 1
    player_2_1.name_display(850, 550)
    player_2_1.health(950, 550)
    player_2_1.status_bar(1050, 550)
    #2 - 2
    player_2_2.name_display(850, 600)
    player_2_2.health(950, 600)
    player_2_2.status_bar(1050, 600)
    #2 - 3
    player_2_3.name_display(850, 650)
    player_2_3.health(950, 650)
    player_2_3.status_bar(1050, 650)

    player_1_1.updated(0)
    player_1_2.updated(0)
    player_1_3.updated(0)
    player_2_1.updated(0)
    player_2_2.updated(0)
    player_2_3.updated(0)
    show_turn(turn)

#----- ATTACKING ANIMATION -----
def attack_animation(num):
    if num == 1:
        temp = player_1_1
    elif num == 2:
        temp = player_1_2
    elif num == 3:
        temp = player_1_3
    elif num == 4:
        temp = player_2_1
    elif num == 5:
        temp = player_2_2
    elif num == 6:
        temp = player_2_3

    if temp.die == False:
        ani_pos = 0
        temp.ani = glob.glob(temp.atk_location)
        temp.img = pygame.image.load(temp.ani[ani_pos])
        if num in range(1, 4):
            temp.img = pygame.transform.flip(temp.img, 100, 0)
        temp.ani_max = len(temp.ani) - 1
        time_delay = 0
        while ani_pos <= temp.ani_max:
            temp.img = pygame.image.load(temp.ani[ani_pos])
            if num in range(1, 4):
                temp.img = pygame.transform.flip(temp.img, 100, 0)
            pygame.time.delay(time_delay)
            time_delay = 200
            ani_pos += 1
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(temp.img, (temp.x, temp.y))
            all_render()
            pygame.display.update()
            temp.img = pygame.image.load(temp.ani[0])
            if num in range(1, 4):
                temp.img = pygame.transform.flip(temp.img, 100, 0)
        pygame.time.delay(time_delay)
        ani_pos += 1

        temp.ani_pos = 0
        temp.ani = glob.glob(temp.location)
        temp.img = pygame.image.load(temp.ani[temp.ani_pos])
        if num in range(1, 4):
            temp.img = pygame.transform.flip(temp.img, 100, 0)
            temp.ani_max = len(temp.ani) - 1

#----- DAMAGE CALCULATION -----
def dmg_cal(char1, char2, turn):
    # Attacker, Defender
    if turn == 1:
        # Attacker
        if char1 == 1:
            attacker = player_1_1
        elif char1 == 2:
            attacker = player_1_2
        elif char1 == 3:
            attacker = player_1_3
        # Defender
        if char2 == 1:
            defender = player_2_1
        elif char2 == 2:
            defender = player_2_2
        elif char2 == 3:
            defender = player_2_3

    elif turn == 2:
        # Attacker
        if char1 == 1:
            attacker = player_2_1
        elif char1 == 2:
            attacker = player_2_2
        elif char1 == 3:
            attacker = player_2_3
        # Defender
        if char2 == 1:
            defender = player_1_1
        elif char2 == 2:
            defender = player_1_2
        elif char2 == 3:
            defender = player_1_3

    if defender.hp > 0 and attacker.die == False:
        dmg = (attacker.ap + random.randint(-5, 5)) - (defender.dp * 0.05)
        if defender.hp - dmg <= 0:
            defender.hp = 0
            defender.die = True
            if turn == 1:
                dead(defender)
            elif turn == 2:
                dead(defender)
        else:
            defender.hp -= dmg

#----- Dead body -----
def dead(char):
    char.set_location(dead_character_location(char.temp), character_location_atk(char.temp))
    char.die = True
    char.updated(0)

#----- CHECK DEAD COUNT P1 -----
def check_p1():
    count = 0
    lst = [player_1_1, player_1_2, player_1_3]
    for i in lst:
        if i.die == True:
            count += 1
    return count

#----- CHECK DEAD COUNT P2 -----
def check_p2():
    count = 0
    lst = [player_2_1, player_2_2, player_2_3]
    for i in lst:
        if i.die == True:
            count += 1
    return count

#---- RUN GAME -----
def run_game():
    gameExit = False
    gameOver_check = False
    gameOver_check_2 = 0
    global turn
    turn = 0
    select = []
    global p1_count, p2_count
    p1_count, p2_count = 0, 0

    clock = pygame.time.Clock()
    pygame.display.update()

    while not gameExit:
        all_render()
        # show_turn(turn)
        if check_p1() == 3:
            gameOver_check = True
            gameOver_check_2 = 2

        elif check_p2() == 3:
            gameOver_check = True
            gameOver_check_2 = 1

        while gameOver_check == True:
            if gameOver_check_2 == 1:
                gameOver(1)
            else:
                gameOver(2)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameExit = True
                        gameOver_check = False

        for event in pygame.event.get():
            # print("EVENT:  ",event)
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                if turn % 2 == 0:
                    if player_1_1.die == False:
                        select.append(1)
                    else:
                        dead(player_1_1)
                elif turn % 2 == 1:
                    if player_2_1.die == False:
                        select.append(1)
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                if turn % 2 == 0:
                    if player_1_2.die == False:
                        select.append(2)
                elif turn % 2 == 1:
                    if player_2_2.die == False:
                        select.append(2)
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                if turn % 2 == 0:
                    if player_1_3.die == False:
                        select.append(3)
                elif turn % 2 == 1:
                    if player_2_3.die == False:
                        select.append(3)

        if len(select) == 2:
            if turn % 2 == 0:
                print('PLAYER 1', 'TURN:', turn)
                print(select)
                attack_animation(select[0])
                dmg_cal(select[0], select[1], 1)
            else:
                print('PLAYER 2', 'TURN:', turn)
                print(select)
                attack_animation(select[0] + 3)
                dmg_cal(select[0], select[1], 2)
            select = []
            turn += 1
        all_render()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

#--------- TEST -----------
'''
def TEST():

    set_character(5, 2, 6, 3, 1, 4)

    gameExit = False
    gameOver_check = False
    gameOver_check_2 = 0
    global turn
    turn = 0
    select = []
    global p1_count, p2_count
    p1_count, p2_count = 0, 0

    clock = pygame.time.Clock()
    pygame.display.update()

    while not gameExit:
        all_render()
        #show_turn(turn)
        if check_p1() == 3:
            gameOver_check = True
            gameOver_check_2 = 2

        elif check_p2() == 3:
            gameOver_check = True
            gameOver_check_2 = 1

        while gameOver_check == True:
            if gameOver_check_2 == 1:
                gameOver(1)
            else:
                gameOver(2)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameExit = True
                        gameOver_check = False

        for event in pygame.event.get():
            #print("EVENT:  ",event)
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                if turn % 2 == 0:
                    if player_1_1.die == False:
                        select.append(1)
                    else:
                        dead(player_1_1)
                elif turn % 2 == 1:
                    if player_2_1.die == False:
                        select.append(1)
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                if turn % 2 == 0:
                    if player_1_2.die == False:
                        select.append(2)
                elif turn % 2 == 1:
                    if player_2_2.die == False:
                        select.append(2)
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                if turn % 2 == 0:
                    if player_1_3.die == False:
                        select.append(3)
                elif turn % 2 == 1:
                    if player_2_3.die == False:
                        select.append(3)

        if len(select) == 2:
            if turn % 2 == 0:
                print('PLAYER 1', 'TURN:', turn)
                print(select)
                attack_animation(select[0])
                dmg_cal(select[0], select[1], 1)
            else:
                print('PLAYER 2', 'TURN:', turn)
                print(select)
                attack_animation(select[0]+3)
                dmg_cal(select[0], select[1], 2)
            select = []
            turn += 1
        all_render()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
'''


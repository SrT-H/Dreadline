import pygame  # import external library pygame
import Test
#from Rock_Paper_Scissors_mini_game import RockPaperScissors

black = (0, 0, 0)  # set black color
lightskyblue = (135, 206, 250)  # set light sky blue color

display_width = 1280  # set display width
display_height = 768  # set display height
caption = 'Character Selection'  # set top bar caption

# init game
pygame.init()
logo = pygame.image.load("Chara_select\Pic\dreadline_logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(black)


class Image:
    pos_x = 0
    pos_y = 0
    width = 0
    height = 0
    bg_image = ''

    def draw(self):
        char_image = pygame.image.load(self.bg_image)
        char_image = pygame.transform.scale(char_image, (self.width, self.height))
        screen.blit(char_image, (self.pos_x, self.pos_y))


class CharacterAndStatImage(Image):
    def __init__(self, pos_x, pos_y, char_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 300
        self.height = 300
        self.bg_image = 'Chara_select\Pic\%s.png' % char_name

        self.draw()


class SelectYourCharImage(Image):
    def __init__(self, pos_x, pos_y, char_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 800
        self.height = 50
        self.bg_image = 'Chara_select\\text\%s.png' % char_name

        self.draw()


class Button:
    pos_x = 0
    pos_y = 0
    width = 0
    height = 0
    bg_image = ''
    bg_image_area = None
    image = None

    def draw(self):
        self.image = pygame.image.load(self.bg_image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.pos_x, self.pos_y))

        self.bg_image_area = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


class CharacterButton(Button):
    p1_image = 'Chara_select\\text\P1.png'
    p2_image = 'Chara_select\\text\P2.png'
    player_image_width = 30
    player_image_height = 30
    player_image_pos_y = 536

    def __init__(self, pos_x, pos_y, char_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 100
        self.height = 100
        self.bg_image = 'Chara_select\Pic\%s.png' % char_name
        self.player_image_pos_x = self.pos_x+38
        self.draw()

    def select_by_player1(self):
        # self.draw()
        p1_image = pygame.image.load(self.p1_image)
        p1_image = pygame.transform.scale(p1_image, (self.player_image_width, self.player_image_height))
        screen.blit(p1_image, (self.player_image_pos_x, self.player_image_pos_y))
        pygame.display.update()

    def select_by_player2(self):
        # self.draw()
        p2_image = pygame.image.load(self.p2_image)
        p2_image = pygame.transform.scale(p2_image, (self.player_image_width, self.player_image_height))
        screen.blit(p2_image, (self.player_image_pos_x, self.player_image_pos_y))
        pygame.display.update()


class SelectButton(Button):
    def __init__(self, pos_x, pos_y, char_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 149
        self.height = 43
        self.bg_image = 'Chara_select\\text\%s.png' % char_name

        self.draw()


class SelectCharacterPage:
    def __init__(self):
        print('init select char page')
        self.caption = 'Character Selection'

        screen.fill(lightskyblue)

        self.player_selected_list = [0, 0, 0, 0, 0, 0]
        self.char_picked = 0
        self.player_num = Test.RockPaperScissors()
        self.player_number = self.player_num.rules()

        self.select_ur_char = SelectYourCharImage(235, 30, 'Select-Your-Character')
        self.elentriana = CharacterButton(330, 498, 'Chara')
        self.zalana = CharacterButton(430, 498, 'Chara')
        self.shaca = CharacterButton(530, 498, 'Chara')
        self.kazuki = CharacterButton(630, 498, 'Chara')
        self.lucifer = CharacterButton(730, 498, 'Chara')
        self.refaian = CharacterButton(830, 498, 'Chara')

        self.select_button = SelectButton(555, 640, 'Select')

    def draw(self):
        pygame.display.update()

    def mouse_click_event_handle(self, x, y):
        print('mouse click down', x, y)
        if self.elentriana.bg_image_area.collidepoint(x, y):
            print('click elentriana')
            self.char_picked = 1
        elif self.zalana.bg_image_area.collidepoint(x, y):
            print('click zalana')
            self.char_picked = 2
        elif self.shaca.bg_image_area.collidepoint(x, y):
            print('click shaca')
            self.char_picked = 3
        elif self.kazuki.bg_image_area.collidepoint(x, y):
            print('click kazuki')
            self.char_picked = 4
        elif self.lucifer.bg_image_area.collidepoint(x, y):
            print('click lucifer')
            self.char_picked = 5
        elif self.refaian.bg_image_area.collidepoint(x, y):
            print('click refaian')
            self.char_picked = 6
        print('char pick : ', self.char_picked)
        self.select_char_image()

        if self.select_button.bg_image_area.collidepoint(x, y):
            print('click select button')
            if self.char_picked > 0:
                self.select_select_button()

    def select_char_image(self):
        pos_char_x = 330
        pos_char_y = 135
        pos_stat_x = 630
        pos_stat_y = 135

        if self.char_picked == 1:
            print('show elentriana profile!')
            char_image = 'Chara'
            stat_image = 'Chara'
        elif self.char_picked == 2:
            print('show zalana profile!')
            char_image = 'Chara'
            stat_image = 'Chara'
        elif self.char_picked == 3:
            print('show shaca profile!')
            char_image = 'Chara'
            stat_image = 'Chara'
        elif self.char_picked == 4:
            print('show kazuki profile!')
            char_image = 'Chara'
            stat_image = 'Chara'
        elif self.char_picked == 5:
            print('show lucifer profile!')
            char_image = 'Chara'
            stat_image = 'Chara'
        elif self.char_picked == 6:
            print('show refaian profile!')
            char_image = 'Chara'
            stat_image = 'Chara'

        self.char_image_show = CharacterAndStatImage(pos_char_x, pos_char_y, char_image)
        self.stat_image_show = CharacterAndStatImage(pos_stat_x, pos_stat_y, stat_image)
        self.draw()

    def select_select_button(self):
        def check_char_selected():
            if self.player_selected_list[self.char_picked-1] > 0:
                return True
            else:
                return False
        if not check_char_selected():
            if self.char_picked == 1:
                if self.player_number == 1:
                    self.elentriana.select_by_player1()
                elif self.player_number == 2:
                    self.elentriana.select_by_player2()
            elif self.char_picked == 2:
                if self.player_number == 1:
                    self.zalana.select_by_player1()
                elif self.player_number == 2:
                    self.zalana.select_by_player2()
            elif self.char_picked == 3:
                if self.player_number == 1:
                    self.shaca.select_by_player1()
                elif self.player_number == 2:
                    self.shaca.select_by_player2()
            elif self.char_picked == 4:
                if self.player_number == 1:
                    self.kazuki.select_by_player1()
                elif self.player_number == 2:
                    self.kazuki.select_by_player2()
            elif self.char_picked == 5:
                if self.player_number == 1:
                    self.lucifer.select_by_player1()
                elif self.player_number == 2:
                    self.lucifer.select_by_player2()
            elif self.char_picked == 6:
                if self.player_number == 1:
                    self.refaian.select_by_player1()
                elif self.player_number == 2:
                    self.refaian.select_by_player2()

            print('player number : ', self.player_number)
            self.player_selected_list[self.char_picked-1] = self.player_number

            if self.player_number == 1:
                self.player_number = 2
            elif self.player_number == 2:
                self.player_number = 1
        print('check_char_selected : ', check_char_selected())
        print(str(self.player_selected_list))


class PageController2:
    def __init__(self):
        print('init page controller')
        self.select_char_page = SelectCharacterPage()

    def get_select_char_page(self):
        self.select_char_page.draw()

    def get_select_char_page_mouse_click_action(self, x, y):
        self.select_char_page.mouse_click_event_handle(x, y)


class CharacterSelect: # for test running
    def __init__(self):
        print('init Dreadline')
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.page_controller2 = PageController2()
        self.page_controller2.get_select_char_page()

    def selection(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.page_controller2.get_select_char_page_mouse_click_action(x, y)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    CharacterSelect().selection()

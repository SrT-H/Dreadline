import pygame
import Character_Selection
#from Dreadline import Image, Button

pygame.init()

white = (255, 255, 255)

display_width = 1280
display_height = 768
caption = 'Find First to Go!'

logo = pygame.image.load("Chara_select\Pic\dreadline_logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)

t = ["Rock", "Paper", "Scissors"]


# class RPSShowImage(Image):
#     def __init__(self, pos_x, pos_y, image_name):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.width = 300
#         self.height = 300
#         self.bg_image = 'Picture\RPS\%s.png' % image_name
#         self.draw()


# class RockPaperScissorsImage(Image):
#     def __init__(self, pos_x, pos_y, image_name):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.width = 250
#         self.height = 250
#         self.bg_image = 'Picture\RPS\%s.png' % image_name
#         self.draw()


# class RockPaperScissorsButton(Button):
#     def __init__(self, pos_x, pos_y, image_name):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.width = 250
#         self.height = 250
#         self.bg_image = 'Picture\RPS\%s.png' % image_name
#         self.draw()


class RockPaperScissors:
    def __init__(self):
        screen.fill(white)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.P1_RPS_picked = ''
        self.P2_RPS_picked = ''
        self.player_number = 0

        # self.rock = RockPaperScissorsButton(96, 345, 'rock alternate')
        # self.paper = RockPaperScissorsButton(510, 345, 'paper alternate')
        # self.scissors = RockPaperScissorsButton(930, 345, 'scissors alternate')

    def draw(self):
        pygame.display.update()

    def start_character_selection(self):
        screen.fill(white)
        char_select_page = Character_Selection.CharacterSelect()
        char_select_page.selection()

    def keyboard_press_event_handle(self, keyboard):
        print('key press')
        if keyboard == pygame.K_z:
            print('P1 press rock')
            self.P1_RPS_picked = 'Rock'
        elif keyboard == pygame.K_x:
            print('P1 press paper')
            self.P1_RPS_picked = 'Paper'
        elif keyboard == pygame.K_c:
            print('P1 press scissors')
            self.P1_RPS_picked = 'Scissors'
        print('P1 RPS pick: ', self.P1_RPS_picked)

        if keyboard == pygame.K_KP1:
            print('P2 press rock')
            self.P2_RPS_picked = 'Rock'
        elif keyboard == pygame.K_KP2:
            print('P2 press paper')
            self.P2_RPS_picked = 'Paper'
        elif keyboard == pygame.K_KP3:
            print('P2 press scissors')
            self.P2_RPS_picked = 'Scissors'
        print('P2 RPS pick: ', self.P2_RPS_picked)
        self.rules()
        # self.selected_RPS_image()

    def rules(self):
        if self.P1_RPS_picked == 'Rock' and self.P2_RPS_picked == 'Rock':
            print('Draw! Try again!')
            self.player_number = 0
        elif self.P1_RPS_picked == 'Paper' and self.P2_RPS_picked == 'Paper':
            print('Draw! Try again!')
            self.player_number = 0
        elif self.P1_RPS_picked == 'Scissors' and self.P2_RPS_picked == 'Scissors':
            print('Draw! Try again!')
            self.player_number = 0
        elif self.P1_RPS_picked == 'Rock' and self.P2_RPS_picked == 'Scissors':
            print('P1 win! P1 can select a character first!')
            self.player_number = 1
        elif self.P1_RPS_picked == 'Rock' and self.P2_RPS_picked == 'Paper':
            print('P2 win! P2 can select a character first!')
            self.player_number = 2
        elif self.P1_RPS_picked == 'Paper' and self.P2_RPS_picked == 'Scissors':
            print('P2 win! P2 can select a character first!')
            self.player_number = 2
        elif self.P1_RPS_picked == 'Paper' and self.P2_RPS_picked == 'Rock':
            print('P1 win! P1 can select a character first!')
            self.player_number = 1
        elif self.P1_RPS_picked == 'Scissors' and self.P2_RPS_picked == 'Rock':
            print('P2 win! P2 can select a character first!')
            self.player_number = 2
        elif self.P1_RPS_picked == 'Scissors' and self.P2_RPS_picked == 'Paper':
            print('P1 win! P1 can select a character first!')
            self.player_number = 1
        # return self.player_number
        if self.player_number != 0 and self.player_number == 1 or self.player_number == 2:
            RockPaperScissors().start_character_selection()



    # def selected_RPS_image(self):
    #     pos_RPS_x = 300
    #     pos_RPS_y = 135

    #     if self.RPS_picked == 1:
    #         print('show rock pic!')
    #         RPS_image = 'rock alternate'
    #     elif self.RPS_picked == 2:
    #         print('show paper pic!')
    #         RPS_image = 'paper alternate'
    #     elif self.RPS_picked == 3:
    #         print('show scissors pic!')
    #         RPS_image = 'scissors alternate'

    #     self.RPS_Picked_Image = RPSShowImage(pos_RPS_x, pos_RPS_y, RPS_image)
    #     self.draw()



class PageController3:
    def __init__(self):
        print('init page controller')
        self.rock_paper_scissors = RockPaperScissors()

    def get_rock_paper_scissors(self):
        self.rock_paper_scissors.draw()

    def get_rock_paper_scissors_keyboard_press_action(self, keyboard):
        self.rock_paper_scissors.keyboard_press_event_handle(keyboard)


class MiniGame:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.page_controller3 = PageController3()
        self.page_controller3.get_rock_paper_scissors()

    def rps_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    keyboard = event.key
                    self.page_controller3.get_rock_paper_scissors_keyboard_press_action(keyboard)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    MiniGame().rps_game()

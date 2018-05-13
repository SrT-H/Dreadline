import pygame
from Dreadline import Image, Button

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


class RPSShowImage(Image):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 300
        self.height = 300
        self.bg_image = 'Picture\RPS\%s.png' % image_name
        self.draw()


class RockPaperScissorsImage(Image):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 250
        self.height = 250
        self.bg_image = 'Picture\RPS\%s.png' % image_name
        self.draw()


class RockPaperScissorsButton(Button):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 250
        self.height = 300
        self.bg_image = 'Picture\RPS\%s.png' % image_name
        self.draw()


class RockPaperScissors:
    def __init__(self):
        screen.fill(white)
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.rock = RockPaperScissorsButton(96, 345, 'rock alternate')
        self.paper = RockPaperScissorsButton(510, 345, 'paper alternate')
        self.scissors = RockPaperScissorsButton(930, 345, 'scissors alternate')

    def draw(self):
        pygame.display.update()

    def keyboard_press_event_handle(self, keyboard):
        print('key press')
        if keyboard == pygame.K_KP1:
            print('press rock')
            self.RPS_picked = 1
        elif keyboard == pygame.K_KP2:
            print('press paper')
            self.RPS_picked = 2
        elif keyboard == pygame.K_KP3:
            print('press scissors')
            self.RPS_picked = 3
        print('RPS pick: ', self.RPS_picked)
        self.selected_RPS_image()

    def selected_RPS_image(self):
        pos_RPS_x = 300
        pos_RPS_y = 135

        if self.RPS_picked == 1:
            print('show rock pic!')
            RPS_image = 'rock alternate'
        elif self.RPS_picked == 2:
            print('show paper pic!')
            RPS_image = 'paper alternate'
        elif self.RPS_picked == 3:
            print('show scissors pic!')
            RPS_image = 'scissors alternate'

        self.RPS_Picked_Image = RPSShowImage(pos_RPS_x, pos_RPS_y, RPS_image)
        self.draw()



class PageController:
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
        self.page_controller = PageController()
        self.page_controller.get_rock_paper_scissors()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    keyboard = event.key
                    self.page_controller.get_rock_paper_scissors_keyboard_press_action(keyboard)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    MiniGame().main()

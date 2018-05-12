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


class RockPaperScissorsImage(Image):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 300
        self.height = 300
        self.bg_image = 'Picture\RPS\%s.jpg' % image_name
        self.draw()


class RockPaperScissorsButton(Button):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 300
        self.height = 300
        self.bg_image = 'Picture\RPS\%s.jpg' % image_name
        self.draw()


class RockPaperScissors:
    def __init__(self):
        screen.fill(white)
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.rock = RockPaperScissorsButton(96, 345, 'rock')
        self.paper = RockPaperScissorsButton(510, 345, 'paper')
        self.scissors = RockPaperScissorsButton(930, 345, 'scissors')

    def draw(self):
        pygame.display.update()

    def mouse_click_event_handle(self, x, y):
        print('mouse click down', x, y)
        if self.rock.bg_image_area.collidepoint(x, y):
            print('click rock')
        elif self.paper.bg_image_area.collidepoint(x, y):
            print('click paper')
        elif self.scissors.bg_image_area.collidepoint(x, y):
            print('click scissors')


class PageController:
    def __init__(self):
        print('init page controller')
        self.rock_paper_scissors = RockPaperScissors()

    def get_rock_paper_scissors(self):
        self.rock_paper_scissors.draw()

    def get_rock_paper_scissors_mouse_click_action(self, x, y):
        self.rock_paper_scissors.mouse_click_event_handle(x, y)


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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.page_controller.get_rock_paper_scissors_mouse_click_action(x, y)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    MiniGame().main()

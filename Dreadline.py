import pygame
from Character_Selection import *


pygame.init()

black = (0, 0, 0)

display_width = 1280
display_height = 720
caption = 'D R E A D L I N E '

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
        screen.blit(char_image, (self.pos_x, self.pos_y))


class DreadlineImage(Image):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bg_image = 'Picture\Text\%s.png' % image_name
        self.draw()


class StartGuideExitButton(Button):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 300
        self.height = 70
        self.bg_image = 'Picture\Text\%s.png' % image_name
        self.draw()


class MainMenu:
    def __init__(self):
        screen.fill(black)
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.dreadline = DreadlineImage(310, 105, 'DREADLINE')
        self.start = StartGuideExitButton(480, 350, 'START')
        self.guide = StartGuideExitButton(480, 450, 'GUIDE')
        self.exit = StartGuideExitButton(480, 550, 'EXIT')

    def draw(self):
        pygame.display.update()
    
    def start_game(self):
        screen.fill(black)
        CharacterSelect().selection()

    def mouse_click_event_handle(self, x, y):
        print('mouse click down', x, y)
        if self.start.bg_image_area.collidepoint(x, y):
            print('click start button!')
            MainMenu().start_game()
        elif self.guide.bg_image_area.collidepoint(x, y):
            print('click guide button!')
        elif self.exit.bg_image_area.collidepoint(x, y):
            print('click exit button')
            self.clock.tick(self.FPS)
            pygame.quit()
            quit()


class PageController:
    def __init__(self):
        print('init page controller')
        self.main_menu = MainMenu()

    def get_main_menu(self):
        self.main_menu.draw()

    def get_main_menu_mouse_click_action(self, x, y):
        self.main_menu.mouse_click_event_handle(x, y)


class Dreadline:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.page_controller = PageController()
        self.page_controller.get_main_menu()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.page_controller.get_main_menu_mouse_click_action(x, y)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    Dreadline().main()

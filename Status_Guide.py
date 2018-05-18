import pygame
from Dreadline import Image
from Character_Selection import Button
from Guide import *
from Type_Guide import *


pygame.init()

black = (0, 0, 0)

display_width = 1280
display_height = 720
caption = 'Guide'

logo = pygame.image.load("Chara_select\Pic\dreadline_logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(black)


class GuideImage(Image):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bg_image = 'Picture\Guide\%s.png' % image_name
        self.draw()


class NextPageButton(Button):
    def __init__(self, pos_x, pos_y, image_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 70
        self.height = 70
        self.bg_image = 'Picture\Guide\%s.png' % image_name
        self.draw()


class StatusGuide:
    def __init__(self):
        screen.fill(black)

        self.status_guide = GuideImage(0, 0, 'Status_guide')
        self.next = NextPageButton(1210, 655, 'modern_right_arrow')

    def draw(self):
        pygame.display.update()

    def mouse_click_event_handle(self, x, y):
        print('mouse click down', x, y)
        if self.next.bg_image_area.collidepoint(x, y):
            print('click next page!')
            LastPageGuide().main()


class PageController:
    def __init__(self):
        print('init page controller')
        self.guide = StatusGuide()

    def get_guide(self):
        self.guide.draw()

    def get_guide_mouse_click_action(self, x, y):
        self.guide.mouse_click_event_handle(x, y)


class SecondPageGuide:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.page_controller = PageController()
        self.page_controller.get_guide()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.page_controller.get_guide_mouse_click_action(x, y)
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    SecondPageGuide().main()

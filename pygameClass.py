import pygame
from emulatorClass import Emulator
from random import randint


class Pygame():
    def __init__(self) -> None:
        pygame.init()
        self.WIDTH = 600
        self.HEIGHT = 500
        self.win = pygame.display.set_mode(( self.WIDTH,  self.HEIGHT))
        pygame.display.set_caption("EmuLauncher")
        self.bg = pygame.image.load("assets/launcher/background.png")
        self.clock = pygame.time.Clock()
        self.running = True
        self.active_window = "ds"

        emulator = Emulator()
        self.game_arrow = gameArrow()
        self.emulator_buttons = [emulatorButtons(name, i) for i, name in enumerate(["n64", "gamecube", "ds"])]
        self.ds_buttons = [gameCard("ds", game, index) for index, game in enumerate(emulator.game_dict["ds"].keys())]
        self.ds_page = 0
    


class emulatorButtons:
    def __init__(self, name, index):
        self.name = name
        self.image = pygame.image.load(f"assets/launcher/btn-{name}.png")
        self.x = 75
        self.y = 200 + 70 * index
        self.width = 450
        self.height = 60
        self.hoverImg = pygame.image.load(f"assets/launcher/btn-hovering.png")

        self.hovered = False

    def show(self, win):
        win.blit(self.image, (self.x, self.y))
        if self.hovered:
            win.blit(self.hoverImg, (self.x, self.y))

    def mouseOver(self, mouseCoords):
        if mouseCoords[0] >= self.x and mouseCoords[0] < self.x + self.width and mouseCoords[1] >= self.y and mouseCoords[1] < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def click(self, pg):
        if self.hovered:
            pg.active_window = self.name
        else:
            return


class gameArrow:
    def __init__(self) -> None:
        self.right_arrow = pygame.image.load(f"assets/games/right_arrow.png")
        self.left_arrow = pygame.image.load(f"assets/games/left_arrow.png")

    def show(self, win):       
        win.blit(self.right_arrow, (555, 300))
        win.blit(self.left_arrow, (5, 300))
        
        # if self.hovered:
        #     win.blit(self.hoverImg, (self.x, self.y))

    def mouseOver(self, mouseCoords):
        if mouseCoords[0] >= self.x and mouseCoords[0] < self.x + self.width and mouseCoords[1] >= self.y and mouseCoords[1] < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def click(self, pg):
        if self.hovered:
            pg.active_window = self.name
        else:
            return


class gameCard:
    def __init__(self, emulator, name, index):
        self.card = pygame.image.load(f"assets/games/card.png")
        self.card_body = pygame.image.load(f"assets/games/card_body.png")
        self.launch = pygame.image.load(f"assets/games/launch.png")
        self.image = pygame.image.load(f"assets/{emulator}/{name}.jpg")
        self.font = pygame.font.Font("assets/fonts/PixelOperator8-Bold.ttf", 12)

        self.emulator = emulator
        self.name = name
        self.index = index

        self.x = ( 290 * ( index % 2 ) ) + (50 if index == 0 else 20)
        self.y = 140
        self.width = 140
        self.height = 60
        self.hoverImg = pygame.image.load(f"assets/launcher/btn-hovering.png")
        self.hovered = False

    def show(self, win):       
        win.blit(self.card_body, (self.x, self.y + 90))
        win.blit(self.image, (self.x + 5, self.y + 10))
        win.blit(self.card, (self.x, self.y))

        name = self.font.render(self.name, True, (255, 255, 255))
        text_rect = name.get_rect(center=(self.x + 120, self.y + 230))
        win.blit(name, text_rect)

        win.blit(self.launch, (self.x + 50, self.y + 270))
        
        # if self.hovered:
        #     win.blit(self.hoverImg, (self.x, self.y))

    def mouseOver(self, mouseCoords):
        if mouseCoords[0] >= self.x and mouseCoords[0] < self.x + self.width and mouseCoords[1] >= self.y and mouseCoords[1] < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def click(self, pg):
        if self.hovered:
            pg.active_window = self.name
        else:
            return

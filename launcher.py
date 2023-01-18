import pygame
import socket
from threading import Thread
from pygameClass import Pygame

pg = Pygame()

while pg.running:
    pg.clock.tick(60)
    pg.win.blit(pg.bg, (0, 0))

    if pg.active_window == "emulator":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for btn in pg.emulator_buttons:
                    btn.click(pg)

        mouseCoords = pygame.mouse.get_pos()

        for btn in pg.emulator_buttons:
            btn.mouseOver(mouseCoords)
            btn.show(pg.win)

    if pg.active_window == "ds":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        mouseCoords = pygame.mouse.get_pos()
        for i in range(pg.ds_page * 2, (pg.ds_page * 2) + 2):
            pg.ds_buttons[i].show(pg.win)
        pg.game_arrow.show(pg.win)


    pygame.display.update()
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screenResolution = (400, 600)
#Colors:
BCKGRND = (125, 125, 125)
MOON = (255, 255, 255)
CLOUD1 = (100, 100, 100)
CLOUD2 = (70, 70, 70)
GHOST = (200, 200, 200)
BLACK = (0, 0, 0)
BALCONY = (50, 50, 50)
HSCOLOR = (54, 44, 18)
WINDOWS = (53, 23, 12)
YELLOW = (255, 255, 0)
SCNDFLRWINDOWS = (172, 138, 100)




def drawBckgrnd(scr):
    """
    Function draws BackGround
    :param scr: screen
    """
    rect(scr, BCKGRND, (0, 0, 400, 250))


def drawHs(scr, stPnt, scl=1):
    """
    Function draws House
    :param scr: screen
    :param stPnt: start point (x, y)
    :param scl: size
    """
    rect(scr, HSCOLOR, (stPnt[0], stPnt[1], 200 * scl, 300 * scl))
    rect(
        scr,
        WINDOWS,
        (stPnt[0] + 30 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        WINDOWS,
        (stPnt[0] + 80 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        YELLOW,
        (stPnt[0] + 130 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        BALCONY,
        (stPnt[0] - 20 * scl, stPnt[1] + 150 * scl, 240 * scl, 30 * scl),
    )
    for i in range(4):
        rect(
            scr,
            SCNDFLRWINDOWS,
            (stPnt[0] + (20 + i * 130 / 3) * scl, stPnt[1], 30 * scl, 150 * scl),
        )
    for i in range(7):
        rect(
            scr,
            BALCONY,
            (stPnt[0] - (10 - i * 35) * scl, stPnt[1] + 120 * scl, 10 * scl, 30 * scl),
        )
    rect(scr, BALCONY, (stPnt[0], stPnt[1] + 110 * scl, 200 * scl, 10 * scl))
    polygon(
        scr,
        BLACK,
        (
            (stPnt[0] - 20 * scl, stPnt[1]),
            (stPnt[0] + 20 * scl, stPnt[1] - 30 * scl),
            (stPnt[0] + 180 * scl, stPnt[1] - 30 * scl),
            (stPnt[0] + 220 * scl, stPnt[1]),
        ),
    )


def drawGhst(scr, stPnt, scl=1, hScl=1):
    """
    Function draws Ghost
    :param scr: screen
    :param stPnt: start point (x, y)
    :param scl: size
    :param hScl: orientation
    """
    polygon(
        scr,
        GHOST,
        (
            (stPnt[0], stPnt[1]),
            (stPnt[0] + 20 * scl * hScl, stPnt[1] - 100 * scl),
            (stPnt[0] + 40 * scl * hScl, stPnt[1] - 110 * scl),
            (stPnt[0] + 100 * scl * hScl, stPnt[1] - 25 * scl),
            (stPnt[0] + 90 * scl * hScl, stPnt[1] - 5 * scl),
            (stPnt[0] + 60 * scl * hScl, stPnt[1] - 25 * scl),
            (stPnt[0] + 50 * scl * hScl, stPnt[1] - 15 * scl),
            (stPnt[0] + 20 * scl * hScl, stPnt[1] - 25 * scl),
        ),
    )
    circle(
        scr,
        GHOST,
        (stPnt[0] + 30 * scl * hScl, stPnt[1] - 105 * scl),
        20 * scl,
    )
    circle(scr, BLACK, (stPnt[0] + 20 * scl * hScl, stPnt[1] - 110 * scl), 5 * scl)
    circle(scr, BLACK, (stPnt[0] + 35 * scl * hScl, stPnt[1] - 110 * scl), 5 * scl)


def ex5(screenSize):
    """
    :param screenSize: screen sesolution
    Function draws picture with background, houses and ghosts
    """
    screen = pygame.display.set_mode(screenSize)
    drawBckgrnd(screen)
    drawHs(screen, (20, 220), 0.5)
    drawHs(screen, (150, 170), 0.5)
    drawHs(screen, (290, 120), 0.5)
    circle(screen, MOON, (360, 40), 30)
    ellipse(screen, CLOUD1, (180, 20, 200, 30))
    ellipse(screen, CLOUD2, (50, 30, 200, 30))
    drawGhst(screen, (250, 550), 1, -1)
    drawGhst(screen, (250, 550))
    drawGhst(screen, (100, 550), 0.5)


ex5(screenResolution)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
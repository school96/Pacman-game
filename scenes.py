import pygame
import sprites
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 193, 5)


# Title screen class
class TitleScreen():
    # Initalize class
    def __init__(self):
        self.font1 = pygame.font.Font(None,35)
        self.active = 1
        self.changescene = False
        self.changeto = None
        self.pacmanswitch = 0
        self.image1 = pygame.image.load("pacman3.png")
        self.image2 = pygame.image.load("pacmanghost4.png")
        self.image3 = pygame.image.load("pacman4.png")
        self.apacimg = 1

    # Pygame event handler
    def HandleEvents(self):
        keys = pygame.key.get_pressed()
        # Menu controls
        if keys[pygame.K_UP] and self.active != 1:
            self.active -= 1
        if keys[pygame.K_DOWN] and self.active != 2:
            self.active += 1
        if keys[pygame.K_RETURN]:
            if self.active == 1:
                self.changeto = "GameScene()"
                self.changescene = True
            if self.active == 2:
                self.changeto = "exit"
                self.changescene = True
        
    def RenderScreen(self, screen):
        screen.fill(BLACK)
        if self.active == 1:
            screen.blit(self.font1.render("Start", True, YELLOW, None), (10, 10))
        else:
            screen.blit(self.font1.render("Start", True, WHITE, None), (10, 10))
        if self.active == 2:
            screen.blit(self.font1.render("Quit", True, YELLOW, None), (10, 50))
        else:
            screen.blit(self.font1.render("Quit", True, WHITE, None), (10, 50))
        if self.pacmanswitch != 10:
            if self.apacimg == 1:
                screen.blit(pygame.transform.scale(self.image1, (618 / 4, 570 / 4)), (100, 300))
            else:
                screen.blit(pygame.transform.scale(self.image3, (618 / 4, 570 / 4)), (100, 300))
            self.pacmanswitch += 1
        else:
            self.pacmanswitch = 0
            if self.apacimg == 1:
                self.apacimg = 2
            else:
                self.apacimg = 1
        screen.blit(pygame.transform.scale(self.image2, (684 / 6, 915 / 6)), (500, 300))

class GameScene():
    def __init__(self):
        self.changescene = False
        self.changeto = None
        self.pgs = pygame.sprite.Group()
        self.player = sprites.PacMan()
        self.pgs.add(self.player)

    def HandleEvents(self):
        pass

    def RenderScreen(self, screen):
        screen.fill(BLACK)

        self.pgs.update()
        self.pgs.draw(screen)

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
        self.bgs = pygame.sprite.Group()
        self.dgs = pygame.sprite.Group()
        self.player = sprites.PacMan()
        self.pgs.add(self.player)
        self.altclock = 0
        self.pacsound = pygame.mixer.Sound("pacman_sound.ogg")
        self.gamesound = pygame.mixer.Sound("game_over_sound.ogg")
        self.score = 0
        self.font = pygame.font.Font(None, 20)

        # Border to prevent user from going off screen
        self.bgs.add(sprites.Barrier(-20, 0, 20, 800))
        self.bgs.add(sprites.Barrier(800, 0, 20, 800))
        self.bgs.add(sprites.Barrier(0, -20, 800, 20))
        self.bgs.add(sprites.Barrier(0, 800, 800, 20))
        # Barriers for the actual level
        self.bgs.add(sprites.Barrier(20, 20, 760, 20))
        self.bgs.add(sprites.Barrier(20, 760, 760, 20))
        self.bgs.add(sprites.Barrier(20, 60, 20, 320))
        self.bgs.add(sprites.Barrier(20, 400, 20, 340))
        self.bgs.add(sprites.Barrier(760, 60, 20, 320))
        self.bgs.add(sprites.Barrier(760, 400, 20, 340))
        self.bgs.add(sprites.Barrier(60, 60, 680, 20))
        self.bgs.add(sprites.Barrier(60, 720, 680, 20))
        self.bgs.add(sprites.Barrier(60, 80, 20, 300))
        self.bgs.add(sprites.Barrier(60, 400, 20, 320))


        self.sx = 20
        self.sy = 0
        while True:
            self.addsprite = sprites.Dot(self.sx + 5, self.sy + 5)
            self.dgs.add(self.addsprite)
            self.sx += 20
            if self.sx == 800:
                self.sx = 0
                self.sy += 20
            if self.sy == 800:
                break

    def HandleEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.player.dir != "e":
                self.player.redir("e")
                self.altclock = 0
            self.player.rect.x += 1.5
            if pygame.sprite.spritecollideany(self.player, self.bgs):
                self.player.rect.x -= 1
        if keys[pygame.K_a]:
            if self.player.dir != "w":
                self.player.redir("w")
                self.altclock = 0
            self.player.rect.x -= 1
            if pygame.sprite.spritecollideany(self.player, self.bgs):
                self.player.rect.x += 1
        if keys[pygame.K_w]:
            if self.player.dir != "n":
                self.player.redir("n")
                self.altclock = 0
            self.player.rect.y -= 1
            if pygame.sprite.spritecollideany(self.player, self.bgs):
                self.player.rect.y += 1
        if keys[pygame.K_s]:
            if self.player.dir != "s":
                self.player.redir("s")
                self.altclock = 0
            self.player.rect.y += 1.5
            if pygame.sprite.spritecollideany(self.player, self.bgs):
                self.player.rect.y -= 1
        if keys[pygame.K_ESCAPE]:
            self.gamesound.play()
            self.changeto = "TitleScreen()"
            self.changescene = True

        if pygame.sprite.spritecollide(self.player, self.dgs, True):
            self.score += 1
            print(self.score)
        
        if self.altclock != 8:
            self.altclock += 1
        else:
            self.altclock = 0
            self.player.alternate()
            self.pacsound.play()

    def RenderScreen(self, screen):
        screen.fill(BLACK)
        self.scorerender = self.font.render("Score: " + str(self.score), True, WHITE, None)
        self.dgs.update()
        self.dgs.draw(screen)
        self.pgs.update()
        self.pgs.draw(screen)
        self.bgs.update()
        self.bgs.draw(screen)
        screen.blit(self.scorerender, (10, 802))

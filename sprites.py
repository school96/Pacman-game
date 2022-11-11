import pygame

class PacMan(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.spriteviews = (pygame.image.load("pacman1.png"), pygame.image.load("pacman2.png"), pygame.image.load("pacman3.png"), pygame.image.load("pacman4.png"), pygame.image.load("pacman5.png"), pygame.image.load("pacman6.png"), pygame.image.load("pacman7.png"), pygame.image.load("pacman8.png"))
        self.dir = "e"
        self.loaded = 3
        self.image.blit(pygame.transform.scale(self.spriteviews[self.loaded - 1], (20, 20)), (0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def redir(self, dir):
        self.image.fill((0, 0, 0))
        if dir == "e":
            self.loaded = 4
            self.dir = "e"
        if dir == "w":
            self.loaded = 2
            self.dir = "w"
        if dir == "n":
            self.loaded = 6
            self.dir = "n"
        if dir == "s":
            self.loaded = 8
            self.dir = "s"
        self.image.blit(pygame.transform.scale(self.spriteviews[self.loaded - 1], (20, 20)), (0, 0))

    def alternate(self):
        self.image.fill((0, 0, 0))
        if self.dir == "e":
            if self.loaded == 4:
                self.loaded = 3
            else:
                self.loaded = 4
        if self.dir == "w":
            if self.loaded == 2:
                self.loaded = 1
            else:
                self.loaded = 2
        if self.dir == "n":
            if self.loaded == 6:
                self.loaded = 5
            else:
                self.loaded = 6
        if self.dir == "s":
            if self.loaded == 8:
                self.loaded = 7
            else:
                self.loaded = 8
        self.image.blit(pygame.transform.scale(self.spriteviews[self.loaded - 1], (20, 20)), (0, 0))
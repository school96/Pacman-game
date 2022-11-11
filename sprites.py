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
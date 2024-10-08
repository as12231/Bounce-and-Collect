import pygame

class Coin:
    def __init__(self, x, y):
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 223, 0))  # Yellow coin color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

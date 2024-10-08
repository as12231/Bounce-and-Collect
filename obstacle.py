import pygame

class Obstacle:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0 or self.rect.x >= 800:
            self.speed *= -1
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

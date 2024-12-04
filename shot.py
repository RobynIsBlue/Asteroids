from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED
        self.rotation = pygame.transform.rotate(self, )
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, width=2, radius=SHOT_RADIUS)

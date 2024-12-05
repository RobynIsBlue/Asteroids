from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, width=2, radius=self.radius)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        a1_angle_mod = random.uniform(20, 50)
        a2_angle_mod = random.uniform(20, 50)
        a1_angle = pygame.math.Vector2.rotate(self.velocity, a1_angle_mod)
        a2_angle = pygame.math.Vector2.rotate(self.velocity, -a2_angle_mod)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_angle * 1.2
        a2.velocity = a2_angle * 1.2
               
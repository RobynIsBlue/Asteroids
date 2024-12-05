import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroid_field = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, drawable, updatable)

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    dt = clock.tick(60) / 1000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for x in drawable:
            x.draw(screen)
        for x in updatable:
            x.update(dt)
        for x in asteroids:
            if player.is_colliding(x):
                print("get FUCKED")
                pygame.QUIT
                return
            for y in shots:
                if y.is_colliding(x):
                    x.split()
                    y.kill()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
import asteroidfield 
from shot import Shot

clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
asteroidfield.AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    aster_field = asteroidfield.AsteroidField()
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(0)
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.kill()
                    bullet.kill()
        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

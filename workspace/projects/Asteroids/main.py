import pygame
from logger import log_state, log_event
from constants import  SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroidfield_obj = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while(True):
        log_state()
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                return 
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip() #flip brings out the hidden drawings, and it accounts for changing the frame also htus bringing out hidden drawing. Hidden drawing as in as the cpu first store the drawing in  abuffer rather directly makin on the screen
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision_with(shot):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()

        

        

if __name__ == "__main__":
    main()


import pygame
from logger import log_state 
from constants import  SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        log_state()
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                return 
        screen.fill("black")
        pygame.display.flip()
    

if __name__ == "__main__":
    main()


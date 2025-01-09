import pygame
from constants import *

def main():

    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()




if __name__ == "__main__":
    main()


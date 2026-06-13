from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS,LINE_WIDTH
class Shot(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity*dt


    def draw(self, screen: pygame.Surface) -> None:
       return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )

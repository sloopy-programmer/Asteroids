import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape 
from logger import log_event
import random 

class Asteroid(CircleShape):
    def init(self, x:float, y: float, radius: float)-> None:
        super().__init__(x, y, radius)

    def draw(self, screen ):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20.0, 50.0)
            first_velocity_vector = self.velocity.rotate(angle)
            second_velocity_vector = self.velocity.rotate(-1*angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_first = Asteroid(self.position.x, self.position.y, self.radius )
            new_asteroid_second = Asteroid(self.position.x, self.position.y, self.radius)
            new_asteroid_first.velocity = first_velocity_vector*1.2
            new_asteroid_second.velocity = second_velocity_vector*1.2


import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dirTick = 0
fps = 60

class MyCircle:
    def __init__(self, pos, size,colour = (0,0,0), width=1,velocity = pygame.Vector2(0,0)):
        self.pos = pos
        self.size = size
        self.colour = colour
        self.width=width
        self.velocity = velocity

    def display(self):
        dx = self.pos[0]
        dy = self.pos[1]
        pygame.draw.circle(screen, self.colour, (dx,dy), self.size, self.width)
    
    def motion(self):
        self.pos += self.velocity * dt

    def deltaVelocity(self,velocity):
        self.velocity = velocity
    
    

circle = MyCircle((1280/2, 720/2),100,colour="red")

while running:
    # screen.lock()
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(fps) / 1000

    circle.motion()
    circle.display()

    pygame.display.flip()
    

pygame.quit()
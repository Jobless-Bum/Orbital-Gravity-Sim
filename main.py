import pygame
import random
import numpy as np
pygame.init()
screen = pygame.display.set_mode((1760,900))
clock = pygame.time.Clock()
running = True
dirTick = 0
fps = 144

class MyCircle:
    def __init__(self, pos, density, size,colour = (0,0,0), width=0,velocity = pygame.Vector2(0,0)):
        self.pos = pos
        self.density = density
        self.size = size
        self.colour = colour
        self.width=width
        self.velocity = velocity
        self.mass = (density * size) *100

    def display(self):
        dx = float(self.pos[0])
        dy = float(self.pos[1])
        pygame.draw.circle(screen, self.colour, (dx,dy), self.size, self.width)
    
    def displayOrbitLines(self,m2pos=(0,0)):
        pygame.draw.line(screen,"purple",m2pos,self.pos,width=2)
        
    
    def orbitalMotion(self, m2 = 0, m2pos=0):
        # F = (G * mass_1 * mass_2) / r^2
        # G = gravitational constant
        # mass = density * volume
            # density = self.density
            # volume = self.size
        # r = distance between the centers of mass
            # center = self.pos #(x,y)
        # G = 6.6743 * pow(10,-11)
        # r = ((self.pos[0] - m2pos[0]) ** 2) + ((self.pos[1] - m2pos[1]) ** 2)
        # F = (G * self.mass * m2) / r
        
        
        rad = np.radians(1)
        x = (self.pos[0] - m2pos[0])
        y = (self.pos[1] - m2pos[1])
        self.pos[0] =  m2pos[0] + ((x * np.cos(rad)) - (y * np.sin(rad)))
        self.pos[1] =  m2pos[1] + ((y * np.cos(rad)) + (x * np.sin(rad)))
        # self.displayOrbitLines(m2pos)

    def deltaVelocity(self,velocity):
        self.velocity = velocity
    
    def bounce(self):
        if self.pos[0] < self.size:
            self.pos[0] = 2*self.size - self.pos[0]
            self.velocity =self.velocity.reflect(pygame.Vector2(1,0))
        elif self.pos[0] >= (screen.get_width()/1.5) - self.size:
            self.pos[0] = 2*((screen.get_width()/1.5) - self.size) - self.pos[0]
            self.velocity =self.velocity.reflect(pygame.Vector2(1,0))
        
        if self.pos[1] < self.size:
            self.pos[1] = 2*self.size - self.pos[1]
            self.velocity =self.velocity.reflect(pygame.Vector2(0,1))
        elif self.pos[1] >= (screen.get_height()/1.5) - self.size:
            self.pos[1] = 2*((screen.get_height()/1.5) - self.size) - self.pos[1]
            self.velocity =self.velocity.reflect(pygame.Vector2(0,1))
    
    def move(self,m2pos):
        self.pos += self.velocity *dt
        self.bounce()
        self.displayOrbitLines(m2pos)
        



circle_list = []
# circle = MyCircle(pos = pygame.Vector2(1280/2, 720/2),density=random.randint(500,1000) ,size=100,colour="red")
# circle2 = MyCircle(pos = pygame.Vector2(720/2, 360/2),density=random.randint(300,500) ,size=50,colour="blue")
circle = MyCircle(pos = pygame.Vector2(1280/2, 720/2),density=1000 ,size=10,colour="red",velocity=pygame.Vector2(np.random.randint(-500,500),np.random.randint(-500,500)))
circle2 = MyCircle(pos = pygame.Vector2(720/2, 360/2),density=1000 ,size=5,colour="blue",velocity=pygame.Vector2(np.random.randint(-500,500),np.random.randint(-500,500)))
circle_list.append(circle)
circle_list.append(circle2)
while running:
    # screen.lock()
    screen.fill('gray')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(fps) / 1000
    
    # for circle in circle_list:
    #     circle.orbitalMotion()
    #     circle.display()

    # circle.orbitalMotion(circle2.mass,circle2.pos)
    circle.orbitalMotion(circle.mass,circle2.pos)
    circle2.orbitalMotion(circle.mass,circle.pos)
    circle.move(circle2.pos)
    
    # circle2.move(circle2.pos)
    
    circle.display()
    circle2.display()

    pygame.draw.line(screen,"black",(0,screen.get_height()/1.5),(screen.get_width()/1.5,screen.get_height()/1.5),width=2)
    pygame.draw.line(screen,"black",(screen.get_width()/1.5,0),(screen.get_width()/1.5,screen.get_height()/1.5),width=2)
    pygame.display.flip()
    

pygame.quit()
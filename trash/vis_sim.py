import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Package Simulation")

# Colors and package settings
black = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Different package types

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(black)
    
    # Simulate package movement
    for i in range(10):  # Simulate 10 packages
        pygame.draw.rect(screen, random.choice(colors), (random.randint(50, 750), random.randint(50, 550), 20, 20))
    
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
sys.exit()

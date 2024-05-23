import pygame
import sys
import random

# Initialize Pygame
pygame.init()


# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Package Conveyor Simulation")

# Conveyor belt dimensions


# Define colors and initial positions
# Sizes corresponding to diameters, and shapes
packages = [
    {'color': (255, 0, 0), 'pos': [50, 100], 'size': (20, 20), 'shape': 'rect'},  # Small square
    {'color': (0, 255, 0), 'pos': [50, 250], 'size': (40, 40), 'shape': 'circle'},  # Medium circle
    {'color': (0, 0, 255), 'pos': [50, 400], 'size': (60, 30), 'shape': 'rect'}  # Large rectangle
]

# Conveyor speed
speed = 5

def draw_package(package):
    x, y = package['pos']
    if package['shape'] == 'circle':
        pygame.draw.ellipse(screen, package['color'], pygame.Rect(x, y, *package['size']))
    else:
        pygame.draw.rect(screen, package['color'], pygame.Rect(x, y, *package['size']))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Update and draw packages
    for package in packages:
        # Move package rightward
        package['pos'][0] += speed
        # Reset package to the left if it goes beyond the screen width
        if package['pos'][0] > screen_width:
            package['pos'][0] = -50
        
        # Draw the package
        draw_package(package)
        belt_height = 20
        belt_color = (100, 100, 100)  # Dark grey

# Drawing the conveyor belt in the main loop
        pygame.draw.rect(screen, belt_color, pygame.Rect(0, screen_height - belt_height, screen_width, belt_height))

    
    # Refresh display
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()
sys.exit()

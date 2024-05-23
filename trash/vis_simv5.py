import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Package Conveyor Simulation")

# Conveyor belt design
conveyor = {'left': 50, 'width': screen_width - 100, 'top': screen_height / 2 - 50, 'height': 100}
conveyor_color = (150, 150, 150)  # Grey color

# Define package templates for random generation
package_templates = [
    {'color': (255, 0, 0), 'size': (20, 20), 'shape': 'rect'},
    {'color': (0, 255, 0), 'size': (30, 30), 'shape': 'circle'},
    {'color': (0, 0, 255), 'size': (50, 20), 'shape': 'rect'}
]

def draw_package(package):
    x, y = package['pos']
    if package['shape'] == 'circle':
        pygame.draw.ellipse(screen, package['color'], pygame.Rect(x, y, *package['size']))
    else:
        pygame.draw.rect(screen, package['color'], pygame.Rect(x, y, *package['size']))

# List to store active packages
active_packages = []

# Timing for new package generation
next_package_time = 0

# Main loop
running = True
while running:
    current_time = pygame.time.get_ticks()  # Get current time in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Generate new packages at random intervals
    if current_time > next_package_time:
        new_package = random.choice(package_templates).copy()
        new_package['pos'] = [conveyor['left'], random.randint(int(conveyor['top']), int(conveyor['top'] + conveyor['height'] - new_package['size'][1]))]
        active_packages.append(new_package)
        next_package_time = current_time + random.randint(1000, 3000)  # Next package in 1-3 seconds
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw conveyor belt
    pygame.draw.rect(screen, conveyor_color, (conveyor['left'], conveyor['top'], conveyor['width'], conveyor['height']))

    # Update and draw packages
    for package in active_packages[:]:
        package['pos'][0] += 2  # Move package rightward
        if package['pos'][0] > conveyor['left'] + conveyor['width']:
            active_packages.remove(package)  # Remove package when it moves off the conveyor
        
        draw_package(package)
    
    # Refresh display
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
sys.exit()

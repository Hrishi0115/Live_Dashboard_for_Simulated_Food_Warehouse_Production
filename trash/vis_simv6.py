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
conveyor = {'left': 50, 'width': screen_width - 100, 'top': screen_height / 2 - 100, 'height': 200}
conveyor_color = (150, 150, 150)  # Grey color

# Define package templates for random generation
package_templates = [
    {'color': (255, 0, 0), 'size': (30, 20), 'shape': 'rect'},
    {'color': (0, 255, 0), 'size': (40, 30), 'shape': 'circle'},
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
next_package_pos_x = conveyor['left']  # Initial position for the first package

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
    
    # Generate new packages at the edge of the last package
    if not active_packages or next_package_pos_x < conveyor['left'] + conveyor['width']:
        new_package = random.choice(package_templates).copy()
        y_position = random.randint(int(conveyor['top']), int(conveyor['top'] + conveyor['height'] - new_package['size'][1]))
        new_package['pos'] = [next_package_pos_x, y_position]
        active_packages.append(new_package)
        # Update the position for the next package
        next_package_pos_x += new_package['size'][0] + random.randint(5, 10)  # Small gap

    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw conveyor belt
    pygame.draw.rect(screen, conveyor_color, (conveyor['left'], conveyor['top'], conveyor['width'], conveyor['height']))

    # Update and draw packages
    for package in active_packages[:]:
        package['pos'][0] += 2  # Move package rightward
        if package['pos'][0] > conveyor['left'] + conveyor['width']:
            active_packages.remove(package)  # Remove package when it moves off the conveyor
            next_package_pos_x = conveyor['left']  # Reset the position for new packages

        draw_package(package)
    
    # Refresh display
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
sys.exit()

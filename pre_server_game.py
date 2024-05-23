import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Package Conveyor Simulation")

# Conveyor belt and sensor design
conveyor = {'left': 50, 'width': screen_width - 100, 'top': screen_height / 2 - 100, 'height': 200}
conveyor_color = (150, 150, 150)
sensor_position = conveyor['left'] + conveyor['width'] - 50  # Sensor position

# Define package templates for random generation
package_templates = [
    {'color': (255, 0, 0), 'size': (30, 30), 'shape': 'square'},
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
package_details = []  # Store details of packages that pass the sensor

# Function to check overlap
def check_overlap(new_package):
    for package in active_packages:
        if new_package['pos'][1] < package['pos'][1] + package['size'][1] and new_package['pos'][1] + new_package['size'][1] > package['pos'][1]:
            if new_package['pos'][0] < package['pos'][0] + package['size'][0]:
                return True
    return False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
    
    # Generate new packages with controlled overlap
    if not active_packages or all(package['pos'][0] > conveyor['left'] + 60 for package in active_packages):
        new_package = random.choice(package_templates).copy()
        y_position = random.randint(int(conveyor['top']), int(conveyor['top'] + conveyor['height'] - new_package['size'][1]))
        new_package['pos'] = [conveyor['left'], y_position]
        if not check_overlap(new_package):
            active_packages.append(new_package)

    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw conveyor belt and sensor line
    pygame.draw.rect(screen, conveyor_color, (conveyor['left'], conveyor['top'], conveyor['width'], conveyor['height']))
    pygame.draw.line(screen, (255, 0, 0), (sensor_position, conveyor['top']), (sensor_position, conveyor['top'] + conveyor['height']), 3)

    # Update and draw packages
    for package in active_packages[:]:
        package['pos'][0] += random.randint(2, 5)  # Vary the speed slightly for natural movement
        if package['pos'][0] > conveyor['left'] + conveyor['width']:
            active_packages.remove(package)  # Remove package when it moves off the conveyor
        if package['pos'][0] + package['size'][0] > sensor_position and 'counted' not in package:
            package['counted'] = True
            package_details.append((package['shape'], package['size']))  # Store the shape and size

        draw_package(package)
    
    # Refresh display
    pygame.display.flip()
    pygame.time.wait(10)

# Output details of counted packages
for detail in package_details:
    print(f"Counted a {detail[0]} package of size {detail[1]}")

pygame.quit()
sys.exit()

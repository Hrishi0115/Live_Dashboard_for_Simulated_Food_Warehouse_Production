import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Package Conveyor Simulation")

# Define colors and initial positions
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue for different package types
packages = [{'color': color, 'pos': [50, i*100 + 50], 'size': (20, 20)} for i, color in enumerate(colors)]

# Conveyor speed
speed = 5

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
        pygame.draw.rect(screen, package['color'], pygame.Rect(package['pos'], package['size']))
    
    # Refresh display
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()
sys.exit()

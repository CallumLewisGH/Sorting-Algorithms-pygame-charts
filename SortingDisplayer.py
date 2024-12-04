import pygame
import sys
from sys import exit
import math
import random
from SortingAlgorithms import Sorts
from noises import SoundGenerator

count = 0

scrambledList = list(range(128))
random.shuffle(scrambledList)

soundGenerator = SoundGenerator()

sorts = Sorts()
states = sorts.SelectionSort(scrambledList) #Replace with the desired sort. Any sort can be added to sortingalgorithms.py class sorts as long as it returns the correct information

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=1)

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BAR_COUNT = len(scrambledList)
BAR_WIDTH = WIDTH // BAR_COUNT

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BAR_COLOR = (0, 204, 255)
TEXT_COLOR = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bar Chart Visualization")

# Font setup for displaying the count
font = pygame.font.SysFont('Arial', 24)

def draw_bars(values):
    screen.fill(BACKGROUND_COLOR)

    # Draw the bars
    for i, value in enumerate(values):
        value = value * 4
        x = i * BAR_WIDTH
        y = HEIGHT - value
        pygame.draw.rect(screen, BAR_COLOR, (x + (WIDTH/100 * 2), y, BAR_WIDTH, value))

    # Render the count as text
    count_text = font.render(f'Operations: {count}', True, TEXT_COLOR)
    screen.blit(count_text, (10, 10))

    pygame.display.flip()

clock = pygame.time.Clock()
running = True

while running and count < len(states):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_bars(states[count][0])

    soundGenerator.play_tone(states[count][1])

    count += 1  # Increment the count
    clock.tick(144)

pygame.quit()
sys.exit()

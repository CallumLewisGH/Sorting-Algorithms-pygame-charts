import pygame
import numpy as np
import time
import array

class SoundGenerator:
    def __init__(self, sample_rate=22050):
        # Initialize pygame mixer
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
        self.sample_rate = sample_rate

    # Method to generate a sine wave for a given frequency
    def generate_sine_wave(self, frequency, duration=0.1):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        return np.sin(2 * np.pi * frequency * t)

    # Method to play a tone for a given frequency
    def play_tone(self, frequency, duration=0.01):
        sine_wave = self.generate_sine_wave(frequency)
        # Convert to 16-bit PCM format
        sine_wave = np.int16(sine_wave * 32767)  # Scale to 16-bit PCM range
        # Convert to byte data for pygame
        sound_data = array.array("h", sine_wave)
        sound = pygame.mixer.Sound(buffer=sound_data)
        sound.play()
        time.sleep(duration)  # Play for the duration of the tone

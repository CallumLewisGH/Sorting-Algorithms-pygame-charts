import pygame
import numpy as np
import time
import array

class SoundGenerator:
    def __init__(self, sample_rate=22050):
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
        self.sample_rate = sample_rate

    def generate_sine_wave(self, frequency, duration=0.1):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        return np.sin(2 * np.pi * frequency * t)

    def play_tone(self, frequency, duration=0.01):
        sine_wave = self.generate_sine_wave(frequency)
        sine_wave = np.int16(sine_wave * 32767)
        sound_data = array.array("h", sine_wave)
        sound = pygame.mixer.Sound(buffer=sound_data)
        sound.play()
        time.sleep(duration)

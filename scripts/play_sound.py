import pygame, time,  sys
from pathlib import Path

home_directory=str(Path.home()) #this is potentially dangerous

file_directory= home_directory+"/.config/i3/sounds/" + sys.argv[1]


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

pygame.init()

sound=pygame.mixer.Sound(file_directory)
pygame.mixer.Channel(0).play(sound)
print(sound.get_length())
time.sleep(sound.get_length()+0.2)


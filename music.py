import pygame

pygame.mixer.init()

def start():
  pygame.mixer.music.load('./rain.ogg')
  pygame.mixer.music.play(loops=-1)

def stop():
  pygame.mixer.music.stop()

def toggle():
  if pygame.mixer.music.get_busy():
    stop()
  else:
    start()
import pygame
import time
pygame.init()
'''creating the program window''
back = (200, 255, 255) ##background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
clock = pygame.time.Clock()
'''Rectangle class'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height) 
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness):  #outline of an existing rectangle
      pygame.draw.rect(mw, frame_color, self.rect, thickness)   
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
'''Class label'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
cards = []
num_cards = 4
x = 70


start_time = time.time()
cur_time = start_time


''' Game interface'''

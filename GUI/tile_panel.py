import pygame
from tile_palette import TilePalette

class TilePanel:
   """
   A class for holding information to be written to a pygame.Surface
   """
   
   def __init__(self, tile_palette, tiles_wide, tiles_tall):
      """
      Initializer
      """
      self.palette = tile_palette
      self.tiles_wide = tiles_wide
      self.tiles_tall = tiles_tall
      self.base_width = self.tiles_wide * palette.tile_width_px
      self.base_height = self.tiles_tall * palette.tile_height_px
      self.width = 500
      self.height = 500
      self.background_color = (0, 0, 0)
      self.default_foreground_color = (255, 255, 255)
      create_tile_array()
   
   
   def create_tile_array(self):
      """
      Create the array of tiles. Overwrites old one whenever called
      """
      self.index_array = [[' ' for _ in range(self.tiles_wide)] for _ in range(self.tiles_tall)]
      self.fg_array = [[self.default_foreground_color for _ in range(self.tiles_wide)] for _ in range(self.tiles_tall)]
      self.bg_array = [[self.background_color for _ in range(self.tiles_wide)] for _ in range(self.tiles_tall)]
      self.tile_array = [[None for _ in range(self.tiles_wide)] for _ in range(self.tiles_tall)]
      for x in range(self.tiles_wide):
         for y in range(self.tiles_tall):
            set_tile(self, x, y)
         
   def set_tile(self, x, y):
      """
      Create surface by stored values
      """
      self.tile_array[x][y] = palette.get_tile_by_index(self.index_array[x][y], self.fg_array[x][y])
   
   def set_tile_index(self, x, y, index):
      self.index_array[x][y] = index
   
   def set_tile_fg(self, x, y, color):
      self.fg_array[x][y] = color
   
   def set_tile_bg(self, x, y, color):
      self.bg_array[x][y] = color
   
   def get_image(self, width, height):
      image = pygame.Surface((self.base_width, self.base_height))
      image.convert()
      image.fill(self.background_color)
      
      w = palette.tile_width_px
      h = palette.tile_height_px
      bg_stamp = pygame.Surface((w, h))
      for x in range(self.tiles_wide):
         for y in range(self.tiles_tall):
            if self.bg_array[x][y] != self.background_color:
               bg_stamp.fill(self.bg_array[x][y])
               image.blit(bg_stamp, (w * x, h * y))
            image.blit(self.tile_array[x][y], (w * x, h * y))
      return pygame.transform.scale(image, (width, height))
   
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import pygame
from Engine import utility

class TilePalette:
   """
   A class for containing a single set of mask-style tile sprites.
   """
   
   def __init__(self, spritesheet_file_name, spritesheet_size_tiles, tile_size_px):
      """
      spritesheet_file_name: string
      spritesheet_size_tiles (tuple of ints): number of tiles wide and tall
      tile_size_px (tuple of ints): width and height of each tile in pixels
      returns -> self
      """
      self.tile_size_px = tile_size_px
      self.spritesheet_size_tiles = spritesheet_size_tiles
      self.spritesheet = self._load_image_from_file(spritesheet_file_name, colorkey=-1)
      self.tile_array = self._get_tile_array(self.spritesheet)
   
   def _load_image_from_file(self, file_name, colorkey=None):
      """
      Load image from file. Use colorkey = -1 to set color in pixel 0, 0 as transparency color
      filename (string): unqualified file name of spritesheet
      colorkey (int tuple, -1, or None): color to be treated as fully transparent
      returns -> Surface
      """
      main_dir = os.path.split(os.path.abspath(__file__))[0]
      image_dir = os.path.join(main_dir, "../res/images")
      fullname = os.path.join(image_dir, file_name)
      image = pygame.image.load(fullname)
      image = image.convert()
   
      if colorkey is not None:
         if colorkey == -1:
            colorkey = image.get_at((0, 0))
         image.set_colorkey(colorkey, pygame.RLEACCEL)
      
      return image
   
   def _get_tile_array(self, spritesheet):
      """
      Create and fill tile array
      spritesheet (Surface): the spritesheet containing the tiles
      returns -> Surface[][]
      """
      tile_array = utility.create_2d_array(self.spritesheet_size_tiles[0], self.spritesheet_size_tiles[1], 0)
      copy_rect = pygame.Rect(0, 0, self.tile_size_px[0], self.tile_size_px[1])
      colorkey = spritesheet.get_colorkey()
      for x in range(0, self.spritesheet_size_tiles[0]):
         for y in range(0, self.spritesheet_size_tiles[0]):
            tile_array[x][y] = pygame.Surface((self.tile_size_px[0], self.tile_size_px[1]))
            copy_rect.left = x * self.tile_size_px[0]
            copy_rect.top = y * self.tile_size_px[1]
            tile_array[x][y].blit(spritesheet, (0, 0), copy_rect)
            tile_array[x][y].set_colorkey(colorkey, pygame.RLEACCEL)
      return tile_array
   
   def get_tile_background(self, bg_color):
      """
      Returns a rectangular tile a solid color, because blitting backgrounds is faster than drawing rects.
      bg_color (tuple of ints): color
      returns -> Surface
      """
      tile_bg = pygame.Surface((self.tile_size_px[0], self.tile_size_px[1]))
      tile_bg.fill(bg_color)
      return tile_bg
   
   def get_tile(self, x_index, y_index, fg_color):
      """
      Returns colored tile, with a transparent background
      x_index (int): x location of tile on spritesheet
      y_index (int): y location of tile on spritesheet
      fg_color (tuple of ints): x location of tile on spritesheet
      returns -> Surface
      """
      base_image = self.tile_array[x_index][y_index]
      colored_image = pygame.Surface(base_image.get_size())
      colored_image.fill(fg_color)
      final_image = base_image.copy()
      final_image.blit(colored_image, (0, 0), special_flags = pygame.BLEND_MULT)
      return final_image
   
   def get_tile_by_index(self, index, fg_color):
      """
      Returns colored tile, with a transparent background
      index (int or char): index of tile on spritesheet
      returns -> Surface
      """
      if isinstance(index, str):
         index = ord(index)
      return self.get_tile(index % self.spritesheet_size_tiles[0], index // self.spritesheet_size_tiles[0], fg_color)

# testing
if __name__ == "__main__":
   pygame.init()
   screen = pygame.display.set_mode((800, 400), pygame.SCALED)
   pygame.display.set_caption("Palette Test")
   test_palette = TilePalette("WSFont_8x16.png", (16, 16), (8, 16))
   test_palette2 = TilePalette("WSFont_16x16.png", (16, 16), (16, 16))
   
   background = pygame.Surface(screen.get_size())
   background = background.convert()
   background.fill((64, 64, 64))

   screen.blit(background, (0, 0))
   pygame.display.flip()
   clock = pygame.time.Clock()

   # Main Loop
   going = True
   while going:
      clock.tick(60)

      # Handle Input Events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            going = False
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False

      # Draw Everything
      second_group_inset = 8 * 17
      third_group_inset = second_group_inset + (8 * 16) + 8
      fourth_group_inset = third_group_inset + (16 * 16) + 8
      screen.blit(background, (0, 0))
      for x in range(0, 16):
         for y in range(0, 16):
            # basic, direct tiles
            screen.blit(test_palette.tile_array[x][y], (x * 8, y * 16))

            # blue fg on white bg
            bg_blit = test_palette.get_tile_background((255, 255, 255))
            fg_blit = test_palette.get_tile(x, y, (0, 0, 255))
            screen_pos = (second_group_inset + (x * 8), y * 16)
            screen.blit(bg_blit, screen_pos)
            screen.blit(fg_blit, screen_pos)
            
            # basic, direct tiles
            screen.blit(test_palette2.tile_array[x][y], (third_group_inset + (x * 16), y * 16))

            # red fg on yellow bg
            bg_blit = test_palette2.get_tile_background((255, 255, 0))
            fg_blit = test_palette2.get_tile(x, y, (255, 0, 0))
            screen_pos = (fourth_group_inset + (x * 16), y * 16)
            screen.blit(bg_blit, screen_pos)
            screen.blit(fg_blit, screen_pos)
      for x in range(0, 26):
         val_arr = "abcdefghijklmnopqrstuvwxyz"
         bg_blit = test_palette.get_tile_background((0, 0, 0))
         fg_blit = test_palette.get_tile_by_index(val_arr[x], (255, 255, 255))
         screen_pos = (x * 8, 16 * 17)
         screen.blit(bg_blit, screen_pos)
         screen.blit(fg_blit, screen_pos)
      pygame.display.flip()
   pygame.quit()

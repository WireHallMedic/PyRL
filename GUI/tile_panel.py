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
      self.base_width = self.tiles_wide * self.palette.tile_size_px[0]
      self.base_height = self.tiles_tall * self.palette.tile_size_px[1]
      self.width = 500
      self.height = 500
      self.background_color = (0, 0, 0)
      self.default_foreground_color = (255, 255, 255)
      self.create_tile_array()
   
   def create_2d_array(self, width, height, default_val=0):
      return [[default_val for _ in range(height)] for _ in range(width)]
   
   
   def create_tile_array(self):
      """
      Create the array of tiles. Overwrites old one whenever called
      """
      self.index_array = self.create_2d_array(self.tiles_wide, self.tiles_tall, ' ')
      self.fg_array = self.create_2d_array(self.tiles_wide, self.tiles_tall, self.default_foreground_color)
      self.bg_array = self.create_2d_array(self.tiles_wide, self.tiles_tall, self.background_color)
      self.dirty_array = self.create_2d_array(self.tiles_wide, self.tiles_tall, True)
      self.tile_array = self.create_2d_array(self.tiles_wide, self.tiles_tall, None)
      for x in range(self.tiles_wide):
         for y in range(self.tiles_tall):
            self.set_tile(x, y)
         
   def set_tile(self, x, y):
      """
      Create surface by stored values
      x (int): x location
      x (int): y location
      """
      self.tile_array[x][y] = self.palette.get_tile_by_index(self.index_array[x][y], self.fg_array[x][y])
      self.dirty_array[x][y] = False
   
   def set_tile_index(self, x, y, index):
      self.index_array[x][y] = index
      self.dirty_array[x][y] = True
   
   def set_tile_fg(self, x, y, color):
      self.fg_array[x][y] = color
      self.dirty_array[x][y] = True
   
   def set_tile_bg(self, x, y, color):
      self.bg_array[x][y] = color
      self.dirty_array[x][y] = True
   
   def set_rect_index(self, x, y, w, h, index):
      for _x in range(x, x + w):
         for _y in range(y, y + h):
            self.set_tile_index(_x, _y, index)
   
   def set_rect_fg(self, x, y, w, h, color):
      for _x in range(x, x + w):
         for _y in range(y, y + h):
            self.set_tile_fg(_x, _y, color)
   
   def set_rect_bg(self, x, y, w, h, color):
      for _x in range(x, x + w):
         for _y in range(y, y + h):
            self.set_tile_bg(_x, _y, color)
   
   def write(self, x, y, w, h, text, fg_color=None, bg_color=None):
      # set fg and bg
      if fg_color is None:
         fg_color = self.default_foreground_color
      if bg_color is None:
         bg_color = self.background_color
      self.set_rect_fg(x, y, w, h, fg_color)
      self.set_rect_bg(x, y, w, h, bg_color)
      # break up text for wrapping
      char_array = self.create_2d_array(w, h, ' ')
      text = text.replace('\n', ' \n ')
      base_word_array = text.split(' ')
      word_array = []
      for word in base_word_array:
         # break long words
         while len(word) > w:
            word_array.append(word[0:w])
            word = word[w:]
         word_array.append(word)
      row = 0
      col = 0
      # put text in char array
      for word in word_array:
         # wrap if word too long for remaining space
         if len(word) >= w - col:
            col = 0
            row += 1
         # process newline
         if word == '\n':
            col = 0
            row += 1
            continue
         # end looping if no more rows
         if row >= h:
            break
         # add chars to char_array
         for x_index in range(len(word)):
            char_array[col][row] = word[x_index]
            col += 1
         # add space after word if there is room
         if col < w - 1:
            col += 1
      for _x in range(w):
         for _y in range(h):
            self.set_tile_index(x + _x, y + _y, char_array[_x][_y])
            
         
   
   def get_image(self, size):
      """
      Returns the image, scaled to the specified size
      Size is a tuple
      """
      image = pygame.Surface((self.base_width, self.base_height))
      image.convert()
      image.fill(self.background_color)
      
      w = self.palette.tile_size_px[0]
      h = self.palette.tile_size_px[1]
      bg_stamp = pygame.Surface((w, h))
      for x in range(self.tiles_wide):
         for y in range(self.tiles_tall):
            if self.dirty_array[x][y]:
               self.set_tile(x, y)
            if self.bg_array[x][y] !=  None and self.bg_array[x][y] != self.background_color:
               bg_stamp.fill(self.bg_array[x][y])
               image.blit(bg_stamp, (w * x, h * y))
            image.blit(self.tile_array[x][y], (w * x, h * y))
      return pygame.transform.scale(image, size)
   
# testing
if __name__ == "__main__":
   pygame.init()
   screen = pygame.display.set_mode((8 * 80, 16 * 24), pygame.SCALED | pygame.RESIZABLE)
   pygame.display.set_caption("TilePanel Test")
   test_palette = TilePalette("WSFont_8x16.png", (16, 16), (8, 16))
   testPanel = TilePanel(test_palette, 80, 24)
   
   char_index = 0
   for x in range(0, 80):
      for y in range(0, 24):
         testPanel.set_tile_index(x, y, char_index)
         char_index += 1
         if char_index == 256:
            char_index = 0
   testPanel.set_rect_index(0, 0, 5, 5, '!')
   testPanel.set_rect_fg(0, 0, 5, 5, (0, 0, 255))
   testPanel.set_rect_bg(0, 0, 5, 5, (0, 255, 0))
   
   background = pygame.Surface(screen.get_size())
   background = background.convert()
   background.fill((64, 64, 64))
   screen.blit(background, (0, 0))
   pygame.display.flip()
   clock = pygame.time.Clock()
   
   out_str = "The quick brown fox jumped over the lazy dog's back. abcdefghijklmnopqrstuvwxyz"
   testPanel.write(10, 10, 10, 11, out_str, bg_color=(64, 64, 64))

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
         elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE) # don't put SCALED here or the user can't shrink the window

      # Draw Everything
      screen.blit(background, (0, 0))
      screen.blit(testPanel.get_image(screen.get_size()), (0, 0))
      pygame.display.flip()
   pygame.quit()

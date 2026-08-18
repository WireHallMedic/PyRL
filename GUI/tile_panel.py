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
            if self.bg_array[x][y] != self.background_color:
               bg_stamp.fill(self.bg_array[x][y])
               image.blit(bg_stamp, (w * x, h * y))
            image.blit(self.tile_array[x][y], (w * x, h * y))
      return pygame.transform.scale(image, size)
   
# testing
if __name__ == "__main__":
   pygame.init()
   screen = pygame.display.set_mode((8 * 80, 16 * 24), pygame.SCALED)
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
      screen.blit(background, (0, 0))
      screen.blit(testPanel.get_image(screen.get_size()), (0, 0))
      pygame.display.flip()
   pygame.quit()

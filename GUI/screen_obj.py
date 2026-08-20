import gui_constants

class ScreenObj:
   """
   A simple class for holding the basic values for generating an image, and the image itself.
   """
   
   def __init__(self, index = ' ', fg = gui_constants.WHITE, bg = None):
      """
      Initializer
      index (int or char): spritesheet index of icon
      fg (int()): foreground color
      bg (int() or None): background color
      returns -> None
      """
      self.index = index
      self.fg_color = fg
      self.bg_color = bg
      self.image = None
   
   def create_image(self, tile_palette):
      """
      Generate the image stored in self.image
      tile_palette (TilePalette): the palette generating the image
      returns -> None
      
      """
      self.image = tile_palette.get_tile_by_index(self.index, self.fg_color)
from gui_constants import *

class ScreenObj:
   """
   A simple class for holding the basic values for generating an image, and the image itself.
   """
   
   def __init__(self, palette, index = ' ', fg = ColorConstants.WHITE, bg = None):
      """
      Initializer
      index (int or char): spritesheet index of icon
      fg (int()): foreground color
      bg (int() or None): background color
      returns -> None
      """
      self._index = index
      self._fg_color = fg
      self._bg_color = bg
      self._image = None
      self._dirty = True
      self.palette = palette
   
   def get_image(self):
      if self._dirty:
         self.create_image()
      return self._image
   
   def get_index(self):
      return self._index
   
   def get_fg_color(self):
      return self._fg_color
   
   def get_bg_color(self):
      return self._bg_color
   
   def set_index(self, index):
      self._index = index
      self._dirty = True
   
   def set_fg_color(self, color):
      self._fg_color = color
      self._dirty = True
   
   def set_bg_color(self, color):
      self._bg_color = color
      self._dirty = True
      
   def create_image(self):
      """
      Generate the image stored in self.image
      tile_palette (TilePalette): the palette generating the image
      returns -> None
      
      """
      self._image = self.palette.get_tile_by_index(self._index, self._fg_color)
      self._dirty = False
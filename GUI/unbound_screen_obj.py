from gui_constants import *
import screen_obj

class UnboundScreenObj(screen_obj.ScreenObj):
   """
   A simple class for holding the basic values for generating an image, and the image itself.
   """
   
   def __init__(self, palette, index = ' ', fg = ColorConstants.WHITE, bg = None):
      """
      Initializer
      """
      super().__init__(palette, index, fg, bg)
      self.loc_tiles = [-1, -1]
      self.offset = [0.0, 0.0]
   
   def blit_to_surface(self, surface):
      """
      Calculates position and blits to passed surface   
      """
      x_loc = int((self.loc_tiles[0] + self.offset[0]) * self.palette.tile_size_px[0])
      y_loc = int((self.loc_tiles[1] + self.offset[1]) * self.palette.tile_size_px[1])
      surface.blit(self.get_image(), (x_loc, y_loc))
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
   
   def blit_to_surface(self, surface, reference=None):
      """
      Calculates position and blits to passed surface   
      surface (Surface): surface to blit this image on to
      reference (UnboundScreenObj) another USO placed at center of surface
      """
      x_pos_tiles = self.loc_tiles[0]
      y_pos_tiles = self.loc_tiles[1]
      if reference is not None:
         pass # TODO
      x_loc = int((x_pos_tiles + self.offset[0]) * self.palette.tile_size_px[0])
      y_loc = int((y_pos_tiles + self.offset[1]) * self.palette.tile_size_px[1])
      surface.blit(self.get_image(), (x_loc, y_loc))
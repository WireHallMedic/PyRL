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
      self._loc_tiles = [-1, -1]
      self._offset = [0.0, 0.0]
   
   def blit_to_surface(self, surface, reference=None):
      """
      Calculates position and blits to passed surface   
      surface (Surface): surface to blit this image on to
      reference (int[]) offset in tiles (based on where camera is tracking)
      """
      x_pos_tiles = self._loc_tiles[0]
      y_pos_tiles = self._loc_tiles[1]
      if reference is not None:
         pass # TODO
      x_loc = int((x_pos_tiles + self._offset[0]) * self.palette.tile_size_px[0])
      y_loc = int((y_pos_tiles + self._offset[1]) * self.palette.tile_size_px[1])
      surface.blit(self.get_image(), (x_loc, y_loc))
   
   def set_loc_tiles(self, x, y):
      """
      Set map location   
      x (int): x position
      y (int): y position
      returns -> None
      """
      self._loc_tiles[0] = x
      self._loc_tiles[1] = y
   
   def get_loc_tiles(self):
      """
      Return map location in tiles  
      returns -> int()
      """
      return (self._loc_tiles[0], self._loc_tiles[1])
   
   def set_offset(self, x, y):
      """
      Set tile offset   
      x (int): x offset
      y (int): y offset
      returns -> None
      """
      self._offset[0] = x
      self._offset[1] = y
   
   def get_loc_tiles(self):
      """
      Return tile offset  
      returns -> float()
      """
      return (self._offset[0], self._offset[1])
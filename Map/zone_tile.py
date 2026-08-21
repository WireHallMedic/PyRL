import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from GUI import screen_obj

class ZoneTile(ScreenObj):
   
   def __init__(self, palette, index = ' ', fg = ColorConstants.WHITE, bg = ColorConstants.BLACK):
      super().__init__(palette, index, fg, bg)
      self.low_passable = True
      self.high_passable = True
      self.transparent = True
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pygame
from tile_palette import TilePalette
from tile_panel import TilePanel
from Engine import utility
import gui_tools
import screen_obj
from gui_constants import *

class BoardPanel(TilePanel):
   """
   Class for displaying the current play area
   """
   
   BOARD_WIDTH = 21
   
   def __init__(self, tile_palette, tiles_wide=BOARD_WIDTH, tiles_tall=BOARD_WIDTH):
      """
      Initializer
      tile_palette (TilePalette): palette used for creating tiles. Retained for future use.
      tiles_wide (int): width in tiles of the grid
      tiles_tall (int): height in tiles of the grid
      returns -> self
      """
      super().__init__(tile_palette, tiles_wide, tiles_tall)
      self.player_character = None
   
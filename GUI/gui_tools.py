import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pygame
from Engine import utility

BORDER_TILE_INDEX_LIST = [
   0,                # no dir
   0,                # N
   0,                #  E
   0 + (12 * 16),    # NE
   0,                #   S
   3 + (11 * 16),    # N S
   10 + (13 * 16),   #  ES
   3 + (12 * 16),    # NES
   0,                #    W
   9 + (13 * 16),    # N  W
   4 + (12 * 16),    #  E W
   1 + (12 * 16),    # NE W
   15 + (11 * 16),   #   SW
   4 + (11 * 16),    # N SW
   2 + (12 * 16),    #  ESW
   5 + (12 * 16)]    # NESW

def get_border_index_array(bool_array):
   """
   Returns an array of the same size, with the sprite location of the tiles that should be borders (as a tuple).
   Tiles that should not be borders are marked with 0
   bool_array (boolean[][]): a two-dimensional array; True if should be a border, else False
   returns -> int[][]
   """
   width = len(bool_array)
   height = len(bool_array[0])
   index_arr = utility.create_2d_array(width, height, 0)
   for x in range(width):
      for y in range(height):
         if bool_array[x][y]:
            index_arr[x][y] = BORDER_TILE_INDEX_LIST[get_neighbor_index(x, y, bool_array)]
   return index_arr

def get_neighbor_index(x, y, bool_array):
   """
   Returns an int [0..15] representing the orthogonally adjacent neighbors; 1 = north, 2 = east, 4 = south, 8 = west
   x (int): x position to check
   y (int): y position to check
   bool_array (boolean[][]): a two-dimensional array; True if should be counted, else False
   returns -> int
   """
   neighbor_index = 0
   if is_in_bounds(x, y - 1, bool_array) and bool_array[x][y-1]:
      neighbor_index += 1
   if is_in_bounds(x + 1, y, bool_array) and bool_array[x+1][y]:
      neighbor_index += 2
   if is_in_bounds(x, y + 1, bool_array) and bool_array[x][y+1]:
      neighbor_index += 4
   if is_in_bounds(x - 1, y, bool_array) and bool_array[x-1][y]:
      neighbor_index += 8
   return neighbor_index
   
def is_in_bounds(x, y, array):
   """
   Returns True if the passed coordinates are within the array, else False
   x (int): x position to check
   y (int): y position to check
   array (object[][]): a two-dimensional array
   returns -> boolean
   """
   return x >= 0 and y >= 0 and x < len(array) and y < len(array[0])

   
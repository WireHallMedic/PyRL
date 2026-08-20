"""
Collection of helper functions
"""

def create_2d_array(width, height, default_val=0):
   """
   Helper method to create a 2d array of size [width][height]
   returns -> Object[][]
   """
   if callable(default_val):
      return [[default_val() for _ in range(height)] for _ in range(width)]
   else:
      return [[default_val for _ in range(height)] for _ in range(width)]
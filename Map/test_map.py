import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from Map.zone_constants import *

def test_no_duplicate_tile_bases():
   val_arr = TileBases
   for i in range(len(val_arr)):
      for j in range(i + 1, len(val_arr)):
         a = val_arr[i]["tile_index"]
         b = val_arr[j]["tile_index"]
         a = a if isinstance(a, int) else ord(a)
         b = b if isinstance(b, int) else ord(b)
         assert a != b
         

if __name__ == "__main__":
   test_no_duplicate_tile_bases()
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from GUI.gui_constants import *

TileBases = [
   dict(name="Pit", high_passable=True, low_passable=True, transparent=True, tile_index=' '),
   dict(name="Clear", high_passable=True, low_passable=True, transparent=True, tile_index=TileConstants.BULLET_TILE),
   dict(name="Low Wall", high_passable=True, low_passable=True, transparent=True, tile_index='='),
   dict(name="Wall", high_passable=True, low_passable=True, transparent=True, tile_index='#'),
   dict(name="Rough", high_passable=True, low_passable=True, transparent=True, tile_index=','),
   dict(name="Bars", high_passable=True, low_passable=True, transparent=True, tile_index=':'),
   dict(name="Shallow Liquid", high_passable=True, low_passable=True, transparent=True, tile_index='-'),
   dict(name="Deep Liquid", high_passable=True, low_passable=True, transparent=True, tile_index='~'),
   dict(name="Closed Door", high_passable=True, low_passable=True, transparent=True, tile_index='|'),
   dict(name="Open Door", high_passable=True, low_passable=True, transparent=True, tile_index='/'),
   dict(name="Terminal", high_passable=True, low_passable=True, transparent=True, tile_index=TileConstants.CAPITAL_OMEGA_TILE),
   dict(name="Unflipped Switch", high_passable=True, low_passable=True, transparent=True, tile_index='!'),
   dict(name="Flipped Switch", high_passable=True, low_passable=True, transparent=True, tile_index=TileConstants.INVERTED_EXCLAMATION_TILE),
   dict(name="Breakable Container", high_passable=True, low_passable=True, transparent=True, tile_index='0'),
   dict(name="Closed Chest", high_passable=True, low_passable=True, transparent=True, tile_index='?'),
   dict(name="Opened Chest", high_passable=True, low_passable=True, transparent=True, tile_index=TileConstants.INVERTED_QUESTION_TILE)
]
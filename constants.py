import util

"""
Path to file containing this snakes appearance configuration
"""
appearance_file = "appearance_config.json"

"""
Constants used to define what is located at a particular
position on the board
"""
FREE_SPACE      = 0
FOOD            = 1
SAFE_SPACE      = 2
HAZARD          = 3

MY_HEAD         = 4
MY_BODY         = 5
MY_TAIL         = 6

ENEMY_HEAD      = 7
ENEMY_BODY      = 8
ENEMY_TAIL      = 9
ENEMY_NEXT_MOVE = 10
ENEMY_MOVE_2    = 11
ENEMY_MOVE_3    = 12
ENEMY_MOVE_4    = 14

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"


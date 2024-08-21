import sys
import os
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.insert(0, parent_directory)
from snakesAndLadderss.models.snake import Snake
from snakesAndLadderss.services.snakes_and_ladder_service import SnakeAndLadderService
# from snakesAndLadderss.models import Ladder, Snake, Player

#snakes

# snakes = []
# snakes.append(Snake(99,10))


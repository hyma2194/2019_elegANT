from .kd_tree_and_dict import KdTreeAndDict
from .nest import Nest
from src.utils import random

# Interface with controller
# GameState calls world interface
class GameState:
    """
            A class used to communicate with the model

            ...

            Attributes
            ----------
            player_list : list
                a list of players id that are currently in the game
            world: list
                a list of all game objects and their positions

            Methods
            -------
            get_objects_in_region(top_left, bottom_right):
                Return positions of objects in specific area

            update()
                Return states and positions of all objects a each time iteration

            create_ants(position, amount)
                Return new ant objects

    """

    def __init__(self, player_list):
        """ Initialize player list and create nests for all the players

        :param player_list: (list) that contains current players IDs

        """
        self.players = player_list
        self.world = KdTreeAndDict()
        all_colors = [player.color for player in player_list]
        positions = []
        for i in range(len(player_list)):
            positions.append(random(2) * 250)
        self.world.create_nests(all_colors, positions)

    def get_objects_in_region(self, top_left, bottom_right):
        """ Get list of positions and all included objects (ants, nests, foods, pheromones, etc) in a specific
            rectangular area

        :param top_left: (list) Coordinates of top left point of the rectangle
        :param bottom_right: (list) Coordinates of bottom right point of the rectangle
        :return:

        """
        self.world.get_rectangle_region(top_left, bottom_right)

    def update(self):
        """Return the states of all the objects and their positions at each time iteration """
        self.world.update()

    def create_ants(self, nest_position, amount):
        """Create new ant objects in the specific nest with the given positions

        :param nest_position: (ndarray) Coordinates of ant position
        :param amount: (int) number of ants that should be created
        :return:

        """
        objects_at_pos = self.world.get_at_position(nest_position)
        for obj in objects_at_pos:
            if type(obj) is Nest:
                nest = obj
        self.world.create_ants(nest, amount)

    def create_nest(self, nest_position, color, size, health):
        self.world.create_nests(nest_position, color, size, health)

    def create_food(self, position_list, size_list):
        self.world.create_food(position_list, size_list)
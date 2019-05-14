import numpy as np

from .game_object import GameObject


class Ant(GameObject):
    """
            A class used to represent an ant object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            color: string
                a string of the ant color
            position: list
                a list of the ant coordinates
            has_food: boolean
                a flag that specifies whether the ant has food or not
            energy: int
                a number that specifies current energy value the ant has

    """

    def __init__(self, color, position):
        """Initialize ant object color and position

        :param color: (str) Color of the ant
        :param position: (list) Coordinates of ant position

        """
        super(Ant, self).__init__(position)
        # TODO: assign id
        self.color = color
        self.has_food = False
        self.energy = 100

    def get_position(self):
        """ Get the coordinates of the object ant position

        :return:

        """
        return self.position

    def unload_food(self):  # TO DO
        """ Flip (has_food) variable to false when the ant reaches the nest and unload the food

        :return:
        """
        # if self.position == nest.position():
        #     self.has_food = False
        #     nest.increase_food(1)
        pass

    def load_food(self):
        """ Flip (has_food) variable to true when the ant finds food

        :return:
        """
        self.has_food = True

    def move(self, possible_positions):
        """ Move the ant to a new position at each time iteration. It moves it randomly in the first milestone.

        :param possible_positions: (list) All the possible neighboring positions the ant can move to
        :return:
        """
        if self.has_food:
            # Go to the nearest nest.
            pass
        # 2. elif it smells, go to smell
        else:  # if no food, it will move randomly
            # this motion is without momentum
            movement = np.random.uniform(low=-1, high=1, size=(1, 2)).astype(np.float32)
            position = self.position + movement
            return position

    def set_trace(self):
        """ Add value for pheromones when the ant finds food.

        :return:
        """
        if self.has_food:
            # Only then it is possible.
            pass

    # TODO: This needs an update function that the world class can call for each ant. -- Unless move is going to
    #  handle food detection, loading, unloading, etc...

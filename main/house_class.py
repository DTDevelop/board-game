"""
House class for board game
"""

class House:
    """
    Class for houses
    """
    def __init__(self, name, color, size = 1):
        """
        create house object
        sizes vary from 1, 2, 3
        """
        self._name = name
        self._color = color
        self._size = size
        if size == 1:
            self._money = 10
        elif size == 2:
            self._money = 40
        elif size == 3:
            self._money = 100

    def __repr__(self):
        """
        String representation
        """
        rep = "House("
        rep += str(self._name) + ", "
        rep += str(self._color) + ", "
        rep += str(self._size) + ", "
        rep += str(self._money) + ")"

        return rep

    def upgrade(self):
        """
        increases house size by 1
        multiplies money value by 2
        maximum limit size 3
        """
        if self._size == 3:
            return
        self._size += 1
        self._money *= 2

    def get_name(self):
        """
        returns name of house
        """
        return self._name

    def get_color(self):
        """
        returns color of house
        """
        return self._color

    def get_size(self):
        """
        returns size of house
        """
        return self._size

    def get_money(self):
        """
        returns money produced
        """
        return self._money

























        #

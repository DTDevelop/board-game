"""
Character class for board game
"""

class Character:
    """
    Class for creating characters
    """
    def __init__(self, name, cash, houses = set([]), items = [], traits = []):
        """
        Create character object based on game mode
        """
        self._name = name
        self._cash = cash
        self._houses = houses
        self._items = items
        self._traits = traits
        self._current_tile = 0 #max range of 0-23

    def __repr__(self):
        """
        String representation
        """
        rep = "Character("
        rep += str(self._name) + ", "
        rep += str(self._cash) + ", "
        rep += str(self._houses) + ", "
        rep += str(self._items) + ", "
        rep += str(self._traits) + ","
        rep += str(self._current_tile) + ")"

        return rep

    def get_name(self):
        """
        get player name
        """
        return self._name
    
    def withdraw_cash(self, amount):
        """
        withdraws given amount
        """
        self._cash -= amount

    def deposit_cash(self, amount):
        """
        deposits given amount into bank account
        """
        self._cash += amount

    def get_cash(self):
        """
        returns total cash
        """
        return self._cash

    def add_house(self, house_coordinates):
        """
        takes ownership of house
        add house coordinate to house set
        represented as tuple
        """
        self._houses.add(house_number)

    def get_houses(self):
        """
        returns set list of house coordinates owned
        """
        return self._houses

    def add_trait(self, trait):
        """
        gain trait
        represented as string, element in list
        """
        self._traits.append(trait)
        
    def get_traits(self):
        """
        return list of traits
        """
        return self._traits
        
    def get_items(self):
        """
        return list of items
        """
        self._items
    
    def get_tile(self):
        """
        returns current tile number
        """
        return self._current_tile
    
    def change_tile(self, num):
        """
        changes tile number
        """
        self._current_tile = num
        




























#

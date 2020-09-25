"""
Character class for board game
"""

class Character:
    """
    Class for creating characters
    """
    def __init__(self, cash, houses = set([]), items = [], traits = []):
        """
        Create character object based on game mode
        """
        self._cash = cash
        self._houses = houses
        self._items = items
        self._traits = traits


    def __repr__(self):
        """
        String representation
        """
        rep = "Character("
        rep += str(self._cash) + ", "
        rep += str(self._houses) + ", "
        rep += str(self._items) + ", "
        rep += str(self._traits) + ")"

        return rep

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

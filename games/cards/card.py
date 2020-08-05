class card:
    def __init__(self,value,suit): # card features: value, suit.
        self.value = value
        self.suit = suit

    def __repr__(self): # card object info
        return f'{self.value}{self.suit}'

    def __gt__(self, other): # fot the cards - self, other: determine which card is "stronger", will be used when i compare two cards during the war game.
        valuelist = [2, 3, 4, 5, 6, 7, 8, 9, 10,"J", "Q", "K", "A"]
        suitlist = ["♦","♠","♥","♣"]

        self_value_strength = 0
        other_value_strength = 0
        self_suit_strength = 0
        other_suit_strength = 0

        for i in range (len(valuelist)):        # i = place in values list.
            if self.value == valuelist[i]:
                self_value_strength = i         # i = level of the card's value "strength".
            if other.value == valuelist[i]:
                other_value_strength = i

        for i in range (len(suitlist)):         # i = place in suit list.
            if self.suit == suitlist[i]:
                self_suit_strength = i          # i = level of the card's suit "strength".
            if other.suit == suitlist[i]:
                other_suit_strength = i

        if self_value_strength > other_value_strength:
            return True
        if self_value_strength == other_value_strength: # if the two cards values are equal -> their suit will determine which is stronger.
            if self_suit_strength > other_suit_strength:
                return True
            else:
                return False
        else:
            return False
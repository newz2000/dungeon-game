from base import Person

class Warrior(Person):
    hp = 100
    strength = 2
    accuracy = 5
    defense = 4
    attacks_by = "swings sword"


class Marksman(Person):
    hp = 100
    strength = 1
    accuracy = 8
    defense = 3
    attacks_by = "shoots an arrow"


class Madman(Person):
    hp = 100
    strength = 3
    accuracy = 3
    defense = 2
    attacks_by = "flails wildly"


class Mage(Person):
    hp = 200
    strength = 1
    accuracy = 6
    defense = 2
    attacks_by = "casts a spell"


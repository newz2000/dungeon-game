from base import Being
from images import *

class Monster(Being):
    last_words = [
        "Now why did I do that?",
        "You have won, O Galilean",
        "I feel ill. Call the doctors.",
        "Tomorrow, I shall no longer be here",
        "Please don't let me fall.",
        "Now, now, my good man, this is no time for making enemies.",
        "I really don't like you.",
        "Oh, oh, that hurt! Foul play!",
        "Fine, if that's how it's gonna be!",
        "I'm telling my mommy!",
        "Oh yeah? Well, my dad can beat up your dad!",
        "Oh, so what you mean is you don't want to be friends?",
        ]
    img = ""

    def __init__(self, name, hp, strength, accuracy, attacks_by, img=""):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.accuracy = accuracy
        self.attacks_by = attacks_by
        if img:
            self.img = img


# Monsters are defined here. The options are:
# name, hp, strength, accuracy. Go ahead and make more monsters by adding to the list
monsters = [
    Monster('rat', 10,  1,  2, 'bites', RAT_IMAGE),
    Monster('bat', 10,  1, 4, 'sucks your blood'),
    Monster('goblin', 20, 3, 6, 'stomps on your toes'),
    Monster('orc', 30,  4,  6, 'stabs with a spear'),
    Monster('troll', 40,  5, 6, 'swings a heavy club'),
    Monster('dragon', 50, 6,  6, 'breathes flames'),
    Monster('blob', 30, 5,  3, 'blobs', BLOB_IMAGE),
    Monster('Two headed Dragon', 55, 6,  4, 'simultaneously breathes fire and ice'),
    Monster('hydra', 70, 6,  4, 'breathes scalding hot steam'),
    Monster('evil stone pegasus', 42, 4,  3, 'kicks with heavy stone hooves'),
    Monster('black spot ', 20, 1,  10, 'seduces you with it\'s blackness'),
    Monster('evil sorcerer', 80, 5,  4, 'casts an enchanting spell'),
    Monster('Baby Basilisk', 25, 2,  7, 'wraps it\'s slender body around you'),
    Monster('Basilisk', 40, 3,  7, 'bites at you'),
    ]

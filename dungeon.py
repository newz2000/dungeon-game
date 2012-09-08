import random
import copy
from actions import *
from monsters import *
from heroes import *
from story import show_story

MONSTER_DEAD = "He's dead, Jim."
PLAYERS_DEAD = "Everyone died and the monsters lived happily ever after. The end."

level = 1
monster = False

HELP = """ The remaining section is instructions on how to play the game

# To start the game do this:
# Figure out the level of the room you're in (a number between 1 and 6).
# Very possibly the first room you visit will be a 6. Using that as an 
# example, type this:
room(6)

# If there is a monster you'll see a message telling you to fight.
# To fight type this:
player_attack()

# After you attack, if it's still alive then it's the monster's turn to 
# fight, type this:
monster_attack()

# repeat the steps above until either the monster dies or the players die
# When the monster dies then you go to the next room, for example, if your 
# 2nd room is a 5 then:
room(5)

# Need to know how well your players are doing? Then check the status:
status()

Have fun! """

# Here you set up the players:
# Choices:
#   Warrior
#   Marksman
#   Madman
#   Mage
# If you want to make a new kind of person then copy and paste the Warrior
# or one of the other types above and change the settings how you like.

players = {
    'Player1': Marksman('Player1'),
    'Player2': Madman('Player2'),
    'Player3' : Warrior('Player3'),
    }

if __name__ == "__main__":
    print "\nTo begin, type: show_story() and hit enter\n"


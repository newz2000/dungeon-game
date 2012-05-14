import random
import copy

MONSTER_DEAD = "He's dead, Jim."
PLAYERS_DEAD = "Everyone died and the monsters lived happily ever after. The end."


class Being(object):
    defense = 0
    name = 'being'
    hp = 0
    strength = 1
    accuracy = 1
    last_words = ["Goodbye cruel world.",]
    attacks_by = 'looks real mean'
    def __str__(self):
        return '%s has %s hp'  % (self.name, self.hp)
    def hit(self, force):
        if force <= self.defense:
            return "Blocked"
        self.hp -= force - self.defense
        if self.hp <= 0:
            print "%s died" % self.name
            return self.die()
        print "%s remaining" % self.hp
        return True
    def defend(self, force):
        if self.defense >= force:
            print "No damage for %s" % self.name
            return True
        else:
            hp = force - self.defense
            self.hp -= hp
            if self.hp > 0:
                print "%s was hit, losing %s hp - %s hp remaining" % (self.name, hp, self.hp)
                return True
            else:
                print "%s was hit, losing %s hp and died" % (self.name, hp)
                return False
    def attack(self, characters):
        isMultiple = True
        try:
            iterator = iter(characters)
        except TypeError:
            isMultiple = False
        if isMultiple:
            divider = len(characters)
        else:
            divider = 1
            characters = {1: characters}
        force = self.strength * random.randint(1,12)
        hit = random.randint(1,12) - self.accuracy
        if hit <= 0:
            force = force / divider
            for character in characters:
                status = characters[character].defend(force)
                if not status:
                    return False
            return status
        else:
            print "Missed"
            return True
    def die(self):
        print "\t%s: %s" %\
              (self.name, self.last_words[
                          random.randint(0, len(self.last_words)-1) ]
                  )
        return False


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
    def __init__(self, name, hp, strength, accuracy, attacks_by):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.accuracy = accuracy
        self.attacks_by = attacks_by


class Person(Being):
    def __init__(self, name):
        self.name = name


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


def get_a_monster(chance):
    if random.randint(1, 6) >= chance:
        return copy.copy(monsters[ random.randint(0, len(monsters) - 1)])
    else:
        return False


def treasure(killed_monster=False):
    treasure_odds = 10 - level
    if not killed_monster:
        treasure_odds /= 2
    y = random.randint(1,10)
    if treasure_odds >= y:
        # we get treasure!
        print
        x = treasure_odds / 2
        if x == 0:
            print "You get a drop of potion! 10 hp for everyone!"
            for player in players:
                players[player].hp += 10
        if x == 1:
            print "You get a small potion! 20 hp for everyone!"
            for player in players:
                players[player].hp += 20
        elif x == 2:
            print "You get a large potion! 40 hp for everyone!"
            for player in players:
                players[player].hp += 40
        elif x == 3:
            print "Ooh, armor! Shiny! +1 defense for everyone!"
            for player in players:
                players[player].defense += 1
        elif x >= 4:
            print "Something very special!"
            if y % 2 == 1:
                print "Caffeine to boost your focus! +1 accuracy for everyone!"
                for player in players:
                    players[player].accuracy += 1
            else:
                print "A ring of power! +1 strength for everyone!"
                for player in players:
                    players[player].strength += 1
        print


def player_attack():
    global monster
    print
    if len(players) <= 0:
        print PLAYERS_DEAD
        return
    try:
        if not monster:
            return
    except NameError:
        print MONSTER_DEAD
    play_order = range(0, len(players))
    random.shuffle(play_order)
    keys = players.keys()
    for play in play_order:
        if players[keys[play]].hp <= 0:
            print "%s is dead. Dead people don't attack." % keys[play]
            players.pop(keys[play])
            continue
        print "%s %s at %s" % \
              (keys[play], players[keys[play]].attacks_by, monster.name)
        results = players[keys[play]].attack(monster)
        if not results:
            monster.die()
            del(monster)
            treasure(True)
            print
            status(False)
            break
        print

def monster_attack():
    try:
        print "\n%s %s" % (monster.name, monster.attacks_by)
        monster.attack(players)
        print
    except NameError:
        print MONSTER_DEAD


def room(room_level):
    global level
    global monster
    print
    level = room_level
    monster = get_a_monster(room_level)
    if monster:
        status(False)
        print "There's a monster here!\nFight!"
    else:
        print "This room is clear"
        treasure()
        return
    if random.randint(1, 20) > 19:
        print "Oooh, that mean ol' %s was waiting for you!" % monster.name
        monster_attack()

        
def status(extended=True):
    if len(players) <= 0:
        print PLAYERS_DEAD
    for player in players:
        print players[player]
        if extended:
            print "\tStrength: %s\n\tAccuracy: %s\n\tDefense: %s\n" %\
                  (players[player].strength, players[player].accuracy, players[player].defense)
    try:
        if monster:
            print monster
            print
    except NameError:
        print
        return


level = 1
monster = False

########################################################
########################################################
# Go ahead and play with stuff below
# Lines that begin with # (like this one) are completely
# ignored. So are blank lines. Other lines have to
# be right or you get an error


# Monsters are defined here. The options are:
# name, hp, strength, accuracy. Go ahead and make more monsters by adding to the list
monsters = [
    Monster('rat', 10,  1,  2, 'bites'),
    Monster('bat', 10,  1, 4, 'sucks your blood'),
    Monster('goblin', 20, 3, 6, 'stomps on your toes'),
    Monster('orc', 30,  4,  6, 'stabs with a spear'),
    Monster('troll', 40,  5, 6, 'swings a heavy club'),
    Monster('dragon', 50, 6,  6, 'breathes flames'),
    Monster('blob', 30, 5,  3, 'blobs'),
    Monster('Two headed Dragon', 55, 6,  4, 'simultaneously breathes fire and ice'),
    Monster('hydra', 70, 6,  4, 'breathes scalding hot steam'),
    Monster('evil stone pegasus', 42, 4,  3, 'kicks with heavy stone hooves'),
    Monster('black spot ', 20, 1,  10, 'seduces you with it\'s blackness'),
    Monster('evil sorcerer', 80, 5,  4, 'casts an enchanting spell'),
    Monster('Baby Basilisk', 25, 2,  7, 'wraps it\'s slender body around you'),
    Monster('Basilisk', 40, 3,  7, 'bites at you'),
    ]

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

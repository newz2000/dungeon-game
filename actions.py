import random
import copy
from monsters import *
from dungeon import players

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

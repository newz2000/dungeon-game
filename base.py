import random
import copy


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


class Person(Being):
    def __init__(self, name):
        self.name = name


# Matt's Dungeon Game

My son and I created this game as an exercise to help him learn programming. We started out with a piece of paper and some dice. We then began to replace the parts of the game that used the dice with a bit of Python code. Eventually we had alost the entire game in python, with the exception of the map.

## To play:

1. Install Python 2.7
1. Download [dungeon.py](https://raw.github.com/newz2000/dungeon-game/master/dungeon.py)
1. You probably put dungeon.py file in your Downloads folder, so go there by typing `cd Downloads` 
1. Open the python console and load the game, you can do this by:
  1. In Linux or Mac OS open a terminal and type `python -i dungeon.py`
  1. In Windows, open Power Shell and type `\Python27\python.exe -i dungeon.py`
1. The game is ready to play. To see some simple instructions, type `print(HELP)`

## The premise:

Start with a grid (a printable grid is included). You draw a maze-like path from a starting-point to an end-point. See the example image below. Each room has a number, which is calculated by taking the number 7 and subtracting the number of adjacent (not diagonal) rooms. So for example, your first room may be a 6 if it touches only one room. The lower the number the harder the room will be, also the more likely you are to get a cool treasure!

If you have a large open chamber you can choose to make the number smaller if you like. See the purple numbers in the image below. 1 is the hardest room and is most likely to give you the best treasure.

After you are done in a room, either because it was empty or you defeated the enemy therein you choose which way to go next. In many cases the only way to go is forward but you may come to a place where you can choose to turn left or right. Keep going, until you reach the exit safely (or die trying).

![](https://github.com/newz2000/dungeon-game/raw/master/dungeon-game.png)

In that map I didn't fill out all the squares, just a few to show how its done. Here's a <a href="https://github.com/newz2000/dungeon-game/raw/master/map.png">map that is complete</a> that you can use as an example.

## The goal:

The goal of the game is to learn programming! You start out by controlling a team of characters through a dungeon inhabited by monsters with simple programming steps.

Since your first room probably has a six then you'd start like this:

`room(6)`

The first thing you're doing is learning the syntax of programming. If you type something wrong then you get an error. If you type it right, you may get a prize or a monster!

This is what you see if the room is empty:

    >>> room(6)

    This room is clear

You might see this if there is a monster in the room:

    >>> room(6)

    Player2 has 100 hp
    Player3 has 100 hp
    Player1 has 100 hp
    Two headed Dragon has 55 hp

    There's a monster here!
    Fight!


If you get a monster then you must attack it. No cowardice! You do this by typing:

`player_attack()`

You'll see something like this:

    >>> player_attack()

    Player2 flails wildly at Two headed Dragon
    Missed

    Player1 shoots an arrow at Two headed Dragon
    Two headed Dragon was hit, losing 8 hp - 47 hp remaining

    Player3 swings sword at Two headed Dragon
    Missed

Your players are initially weak so they may miss or they may not strike hard enough to deal a lethal blow. So then you must give the monster a turn to retaliate, like this:

`monster_attack()`

The monster may miss you or it may strike you. You may see something like this:

    >>> monster_attack()

    Two headed Dragon simultaneously breathes fire and ice
    Player2 was hit, losing 16 hp - 84 hp remaining
    Player3 was hit, losing 14 hp - 86 hp remaining
    Player1 was hit, losing 15 hp - 85 hp remaining

Then you take turns `player_attack()` and `monster_attack()` until the monster dies. You may get a treasure!

You'll see something like this:

    >>> player_attack()

    Player3 swings sword at Two headed Dragon
    Two headed Dragon was hit, losing 4 hp and died
    Two headed Dragon: Oh yeah? Well, my dad can beat up your dad!

    You get a large potion! 40 hp for everyone!


    Player2 has 124 hp
    Player3 has 126 hp
    Player1 has 125 hp


Then you go to the next room. It might be a 5, so you'd do this:

`room(5)`

## Customizing the game

Simple so far, right? Well, to make the game more fun you do some additional programming. Start by giving your team member's names. If you look at the programming code you copied you will see this:

    players = {
        'Player1': Marksman('Player1'),
        'Player2': Madman('Player2'),
        'Player3': Warrior('Player3'),
    }

You can replace Player1 where it appears with your own name. Note that it appears twice! Also be careful to keep the quotes in place. There are three players initially but you can add more. Just copy one of the existing lines and paste it after player3 line. Make as many as you like!

You'll also see that there are different types of players. Initially the choices are `Warrior`, `Marksman`, `Madman` and `Mage`. Each has benefits and disadvantages. You can change your players hero class to whatever you like.

Then save your changes and copy and paste the game again. If you make many changes you may want to exit python and re-open it to start fresh. Now you are starting to learn some more Python programming, specfically Dictionaries and Class instances.

You can also change the list of monsters. Monsters are set in a list. You can make your own simply by adding to the list. Just follow the pattern: The word in quotes is the monster's name, the first number is its hit points (larger numbers are harder to kill). After that is strength, which means how hard they hit you. A higher number means more damage. The next number is it's accuracy, a value of 1-12 where 1 means they're not likely to hit you and 12 means they never miss. The last value is a few words in quotes. This is how they attack.

Once you get good you can make your own types of heros by adding new Classes that inherit from the Person() class. Start with one of the examples and copy and paste it, changing the values of the class Name (i.e. Warrior) and their charactersitcs. The characterstics are just like monsters except they have one new one: defense. If an enemy would have done 10 damage to you but your defense is 4 then the damage is reduced by 4, meaning it only takes 6 hit points. Now you've learned about object oriented programming including classes and inheritance!

Each time you make a change you have to re-paste the whole program. I'd suggest exiting python and starting it up again.

Good luck, I hope you have fun.

## TODO:

The game is not perfect, nor is it complete. Here are a few things we plan to fix:

 * Change the treasure algorithm, some treasures are impossible to get
 * Change the way items affect players. Currently it's possible to increase accuracy to 12 which means you never miss
 * Improve the monster-finding algorithm so that lower numbered rooms get harder monsters and higher numbered rooms get easier monsters
 * Create an easier-to-share Javascript version. This is harder than it sounds because the premise of this game is to introduce Object Oriented Programming which is very weird in JS.

## Thanks

Thanks to John Lenton and Łukasz Czyżykowski who told me about the -i option for python.

## License

This is free, open source software covered by the Apache 2.0 license. It is Copyright by me, Matthew Nuzum. I'd love to see your improvements and changes, though do be careful about sharing children's personal information. (for example if you add your name to the list of players)

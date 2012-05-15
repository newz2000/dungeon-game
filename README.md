# Matt's Dungeon Game

Me and my son created this game as an exercise to help him learn programming. We started out with a peace of paper and some dice. We then began to replace the parts fo the game that used the dice with a bit of Python code. Eventually we had alost the entire game in python, with the exception of the map.

## To play:

1. Install Python 2.7
1. Open the python console, you can do this by:
  1. In Linux or Mac OS open a terminal and type `python`
  1. In Windows, open Power Shell and type `\Python27\python.exe`
1. Copy the contents of the entire dungeon.py file and then paste them into the python console. Note: In Windows, you simply right click in powershell to paste.
1. The game is ready to play. To see some simple instructions, type `print(HELP)`

## The premise:

Imagine a grid (an example grid is included). You've drawn a maze-like path from a starting-point to an end-point. Each room has a number, which is calculated by taking the number 7 and subtracting the number of adjacent (not diagonal) rooms. So for example, your first room may be a 6 if it touches only one room. The lower the number the harder the room will be, also the more likely you are to get a cool treasure!

If you have a large open chamber you can choose to make the number smaller if you like.

!(dungeon-game.png)

## The goal:

The goal of the game is to learn programming! You start out by controlling a team of characters through a dungeon inhabited by monsters with simple programming steps.

Since your first room probably has a six then you'd start like this:

`room(6)`

You start by learning the syntax of programming. If you type something wrong then you get an error. If you type it right, you may get a prize or a monster!

If you get a monster then you must attack it. No cowardice! You do this by typing:

`player_attack()`

Your players are initially weak so they may miss or they may not strike hard enough to deal a lethal blow. So then you must give the monster a turn to retaliate, like this:

`monster_attack()`

Then you take turns `player_attack()` and `monster_attack()` until the monster dies. You may get a treasure!

Then you go to the next room. It might be a 5, so you'd do this:

`room(5)`

Simple, right? Well, to make the game more fun you do some additional programming. Start by giving your team member's names. If you look at the programming code you copied you will see this:

    players = {
        'Player1': Marksman('Player1'),
        'Player2': Madman('Player2'),
        'Player3' : Warrior('Player3'),
    }

You can replace Player1 where it appears with your own name. Note that it appears twice! Also be careful to keep the quotes in place. 

You'll also see that there are different types of players. Initially the choices are `Warrior`, `Marksman`, `Madman` and `Mage`. Each has benefits and disadvantages. 

Then save your changes and copy and paste the game again. Now you are starting to learn some more Python programming, specfically Dictionaries and Class instances.

You can also change the list of monsters. Monsters are set in a list. You can make your own simply by adding to the list.

Once you get good you can make your own types of heros by adding new Classes the inherit from the Person() class.

Each time you make a change you have to re-paste the whole program. I'd suggest exiting python and starting it up again.

Good luck, I hope you have fun.

## License

This is free, open source software covered by the Apache 2.0 license. It is Copyright by me, Matthew Nuzum. I'd love to see your improvements and changes, though do be careful about sharing children's personal information. (for example if you add your name to the list of players)

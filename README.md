# Steel Titans
#### Video Demo:  <URL HERE>
#### Description:
I made this game using python and pygame.
The primary objective of the game is to navigate the maze-like arena and survive. 
The main focus is to entertain the users and keep them away from boredom. This game can be played in multiplayer mode on the same keyboard (2-player game). 
It is a PvP game. The user has to eliminate the other user from the game by shooting his/her tank. In my game the tank does not get destroyed by its own bullet,
like in other tank games where a tank is destroyed by its own bullet. This feature helps the game by making the game long last.
The reason why I chose a maze as a battlefield is to make the bullets collide off the walls at different angles this makes the game very interesting. 
It is very interesting to figure out that at which angle do you have to shoot your bullet so it bounces off the walls perfectly and destroyes your opponent's tank.
The game uses the following mechanics:
- Player 1:
  - WASD to move around
  - 'Q' button to shoot
- Player 2:
  - Arrow keys to move around
  - 'Right Shift' button to shoot
And 'P' for pause for both players.


### Computational Methods:

First of all, the maze can be created using a Python library called “mazelib”.
I will develop this game in Python using Pygame.
The keyboard ensures efficient player movements.
The event loop in Pygame captures real-time keyboard inputs, resulting in smooth and effective player movement.
I can utilise coordinates or vectors for a physics simulation, which includes a bullet bouncing off a wall at a specific angle.
Using decomposition, I can break the problem down into smaller problems so that I can focus on certain things separately.
For example, I can work on the tanks, walls, bullets, etc.
Separately.

Focusing on the tanks.
I can present the tank as an object with the main properties that it needs, like position, angle and speed.
I can ignore any other irrelevant information, like the weight of the tank, the physics of its engine or the rotating turret on top.
Similarly, the bullet can be modelled as a particle which has a position, direction and speed.
This is an abstraction, and this helps because this simplification means that the problem can be modelled and solved efficiently in the code.
I am changing the graphics for the tank as the player moves it with the designated keys.
The bullets, as well as when the bullet is shot from the tank, I'm updating the position of the bullet.


### Who will be interested?:

Most people find most maze games kind of repetitive, in which you just keep on escaping the maze with increasing difficulty.
This is different; instead of escaping the maze, the user needs to survive the maze, and there will be tanks.
This game is intended for a broad age range, which includes younger children.
The controls will be simple: arrow keys, WASD and some action keys.
The graphics will be clear, ensuring the game does not appear frustrating or dull.
Mostly for people who do not enjoy playing games alone and want someone to play with their friends or family.


### Software and hardware requirements:
### Hardware requirements:

* Input devices:
    * Keyboard
    * Mouse
* Output devices:
    * Monitor
    * Speaker

* Storage
    * Minimum 20MB storage

20 MB storage because all the contents of my game all together add up to 10.4MB, so 20MB is the minimum requirement for the game to run properly.

* Processor
    * Minimum Intel Core i3.

It will require a minimum of Intel Core i3 because my game can run on this processor, as this is the most basic one suitable for my game and is mostly widely available.
The graphics of my game also don't require a very high-end processor like Core i5, i7 and i9.
The graphics are compatible with i3.

### Software requirements:

* Operating system:
    * Windows 7+ (64-bit) because Pygame libraries and Python installations are required for the project, which are stable on modern 64-bit systems.
    * macOS 10.13+

* Library used:
    * Pygame


### The Limitations:

There are quite a few limitations for this project.

#### Rendering:

Some older systems may struggle with rendering, as the Intel Core i3 came out in 2010 onwards, while the systems before that are quite outdated, 
which is why they will have problems with rendering.
To improve this, the user can try to upgrade their PC so that the rendering works fine.

#### Accuracy of collision:

I will be using masks to implement the collision system throughout, but achieving top-notch,
pixel-perfect accuracy will probably slow down performance if there isn't enough storage, as it can be heavy.
Which is why I will use the optimised accuracy of collision.
Masks help to some extent to provide pixel-perfect collision, but they're not the best.

#### Performance:

The program may lag due to too many entities on screen.
While Pygame is good for 2D, it runs on a single CPU core.
To increase performance in this, I have decided to limit the bullets to five at a time, meaning when a tank shoots five bullets, 
it has to wait until one of the bullets disappears from the screen.
This will prevent the program from lagging, as there will be fewer entities covering the screen.
I have also set the fps to 60 so that it runs smoothly.

#### Multiplayer:

As two players will play this game, both players will use the same keyboard, which might cause a conflict between the inputs.
The inputs required will be at a decent distance on the keyboard.
To decrease this conflict, I have made the keys further apart from each other.

#### Graphics:

I’m using PyGame, which means it will not consist of very top-class graphics, but they will be reasonable.
It will be a 2D game, not a 3D game.
3D games have much better graphics than 2D games.


### Already existing solutions:

#### Tank trouble:

This is a game that allows up to 3 players.
In Tank Trouble, the main objective is to survive and destroy the other tank while navigating a maze-like arena.
It has no score limit (endless scoring system), so there is no official winner.
Nonetheless, a positive aspect of this game is that it supports up to 3 players.
My game is mostly focused on this one.

#### Bomberman:

This is a very famous game related to my project.
Here, the main goal of this game is to be the last one standing.
However, instead of tanks, some characters place bombs around the arena.
The bombs in this game don't act like bullets and do not jump off the wall, but they are a type of landmine which goes off when a player approaches.
Mostly, the existing solutions have an endless scoring system, which can feel kind of boring over time.
That’s why my project will have a Limited scoring system, which will make the game more competitive and fun.
Players will compete against each other to reach a score limit.
This means that there will be a final winner every time, not like the endless system in which one player leads first, and then the other comes on top, which makes it boring and repetitive.

#### Comparison:

One other important thing is that my game controls are ergonomic, meaning that there will be no conflict between the two players playing the game.
However, in Tank Trouble, as it supports up to 3 players, the controls for the 3rd player is a mouse.
The player uses the mouse to move around and the left mouse button to shoot bullets.
In my opinion, this gives an unfair advantage to the players using the keyboard keys, as using the keyboard keys is more ergonomic and efficient.
So in my game, there are only 2 players, and both of them can use the keys, which keeps it fair.












# PythonIntro - Project 1 Simple Game Creation
PROJECT 1: Racket Ball Pong - CPSC 4160/6160 (Game Engine Construction) <br />
Developed by: James Reich and Joseph Suter <br />

Game: Racket-Ball Pong <br />
-------------------------------------
Version: Pygame python <br />
------------------------------------
How to Install and Run: <br />
!! Please have python 3 and pygame pre-installed !!
1.) Download the files in the github <br />
2.) Open Terminal and navigate to where you've saved the files <br />
3.) Use Terminal command: python3 pygameIntro.py <br />
-------------------------------------
Rules / How to Play : <br />
1.) Use the (left, right) arrow keys to move the player paddle <br />
2.) Don't let the pong hit the ground! <br />
3.) Try to get the highest score possible. <br />
-------------------------------------
Game Image: <br />
![Screenshot 2023-02-27 at 1 49 27 AM](https://user-images.githubusercontent.com/112408320/221494261-dd155a67-c0c7-4530-8f2a-d07277a2583c.png) <br />
-------------------------------------

Motivation: We wanted to create a game anyone could play to pass the time and have some quick casual fun. Settling to cerate a game based on the high-score / self-competitive modules. We created a hybrid combination of pong and racket ball. <br />
-------------------------------------
Reasoning: We chose to implement a feature that causes the game pong to bounce in a random direction within a 70 degree angle every time it hits the player platform, in order to make the game slightly less predictable. There is also a feature that increases the speed of both the game pong and player platform every time the player reaches a score that is a factor of 10, which makes the game more challenging at higher scores. The score increases every time the game pong hits the player platform, and the score is displayed in-game so the player knows what their score is. The high score shows the player what their best score is from the games they played.<br />
------------------------------------
 Game Scheme Image: <br />
 
 ![GameImage drawio](https://user-images.githubusercontent.com/112408320/221486873-fa5a41ee-6658-40f4-8583-b28aeb628eff.png) <br />
------------------------------------
Future Work: To improve the game we could add the following elements: <br />
* A start menu
* Pause menu
* Different game modes (i.e. break-out)
* Prompt which would ask if user would like to play again or quit
Generalization: endless solo racket ball 
<br />


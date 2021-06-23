# Pong-Game
My assignment submission for NIT 6120 Pong Game Application built using Kivy.

Built using the reference: https://kivy.org/doc/stable/tutorials/pong.html

Classes and Methods

Item	- Type -	Description
PongPaddle	- Class -	Paddle class that stores the name and score of the player
bounce_ball	- Method -	Defines how the ball bounces off the paddle based on where it strikes
reset_position	- Method -	Resets the position of both the paddles to its original position when the player opts to start the game again.
Result	- Class -	Contains variables to store the winner number and textual information of the game result
PongBall	- Class -	Class to create a widget for ball
move	- Method -	Method to make the ball move
PongGame	- Class -	Creates Widget for the root element of the UI.
play_again	- Method -	Facilitates the play again feature. Resets variables before start of play.
set_player_info	- Method -	Set the information of the player before start of play. If both players name is entered, serve the ball
serve_ball	- Method -	Resets the position of the ball to center and sets velocity to it. Used after either player scores a point.
stop_ball	- Method -	Method to stop the ball when a conclusion is attained.
update	- Method -	Updates the score.
on_touch_move	- Method -	Method to move the ball when it touches the gradle.
PongApp	- Class -	Base Class of Kivy App
build	- Method -	Initializes and returns Root Widget

Changes in the pong.kv file
1.	Design Changes:
a.	I have changed the colors of the paddle, ball, text, etc at different place as follows:
i.	rgba: utils.rgba('050E5C')
ii.	To use this I had to import utils from kivy.utils
2.	Adding button:
a.	I have added a couple of buttons like ‘Start Game’ and ‘Play Again’.
3.	Adding TextInput Fields:
a.	I have added a couple of TextInput boxes for getting the player names.
4.	Hiding and disabling the unwanted components:
a.	Once I no longer require the components, I am disabling them by setting the opacity to be 0 and disabling them.
 

Further improvisations made by me
1.	Changed the color of the gradle and the ball
2.	Ask the user to enter the name of the players before starting
3.	Display the name of the players besides their score
4.	Give a logical end to the game as follows:
a.	Player scoring 11 first wins the game if the difference when the player scores 11 is 2 or more.
b.	Otherwise after scoring 10, the player will have to earn two more points than his opponent if both have reached 10 points by then.
c.	This rule is similar to that of table tennis.
5.	Play Again feature.

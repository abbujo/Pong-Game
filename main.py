from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

# Game Rules - Updated Version
# Each Player must be given a Name. The color code for players is Green and Red. 
# Player1 color code is Green. Player2 color code is Red.
# The game will not proceed without entering the name of players.
# The player that scores 11 points first will win the game.
# If both the players score 10 points each, a player would need to score 2 more than the other to win the game from there onwards
# After the result a prompt will appear displaying the result of the game
# Along with the prompt will be a play again button.
# Clicking on play again button will restart the game with same players.
# Paddle class that stores the name and score of the player
class PongPaddle(Widget):
    score = NumericProperty(0)
    name = StringProperty("")

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

    def reset_position(self):
        self.pos = self.x, self.width+175

# Result class to store the winner number and textual information of the game result
class Result(Widget):
    info = StringProperty(None)
    winner = NumericProperty(0)


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    result = ObjectProperty(None)

    # method that facilitates the play again feature. Resets variables before start of play.
    def play_again(self):
        self.player1.score = 0
        self.player2.score = 0
        self.result.info = ""
        self.result.winner = 0
        self.player1.reset_position()
        self.player2.reset_position()
        self.serve_ball()

    # method to set the information of the player before start of play. If both players name is entered, serve the ball
    def set_player_info(self):
        self.player1.name = self.ids.name1.text
        self.player2.name = self.ids.name2.text
        if self.player1.name != "" and self.player2.name != "":
            self.serve_ball()

    # method to start serving the ball. Centers the ball and sets the velocity
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    # method to stop the ball. Centers the ball and sets the velocity to zero. Used after the game concludes in a result
    def stop_ball(self, vel=(0, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    # method to provide updates to the game play
    def update(self, dt):
        self.ball.move()
        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            # According to the rule of game if player 2 scores 11 (more than 10) while player 1's score is less than 10. Player 2 wins the game
            if self.player2.score > 10 and self.player1.score < 10:
                self.result.info = self.player2.name + " won the game"
                self.result.winner = 2
                self.stop_ball()
            # According to the rule of game if player 2 and 1 both score more than or equals to 10 and the difference of player2's score and player1's score is 2, Player 2 wins the game
            elif self.player2.score >= 10 and self.player1.score >= 10 and self.player2.score - self.player1.score >= 2:
                self.result.info = self.player2.name + " won the game"
                self.result.winner = 2
                self.stop_ball()
            # According to the rule of game if player 2 and 1 both score more than or equals to 10 and the difference of the score is less than 2, continue serving the ball.
            elif self.player2.score >= 10 and self.player1.score >= 10 and self.player2.score - self.player1.score < 2:
                self.serve_ball(vel=(4, 0))
            # Otherwise serve the ball.
            else:
                self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            # According to the rule of game if player 1 scores 11 (more than 10) while player 2's score is less than 10. Player 1 wins the game            if self.player1.score > 10 and self.player2.score < 10:
            if self.player1.score > 10 and self.player2.score < 10:
                self.result.info = self.player1.name + " won the game"
                self.result.winner = 1
                self.stop_ball()
            # According to the rule of game if player 2 and 1 both score more than or equals to 10 and the difference of player1's score and player2's score is 2, Player 1 wins the game
            elif self.player2.score >= 10 and self.player1.score >= 10 and self.player1.score - self.player2.score >= 2:
                self.result.info = self.player1.name + " won the game"
                self.result.winner = 1
                self.stop_ball()
            # According to the rule of game if player 2 and 1 both score more than or equals to 10 and the difference of the score is less than 2, continue serving the ball.
            elif self.player2.score >= 10 and self.player1.score >= 10 and self.player1.score - self.player2.score < 2:
                self.serve_ball(vel=(-4, 0))
            # Otherwise serve the ball.
            else:
                self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        # Starting point of the game
        game.set_player_info()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
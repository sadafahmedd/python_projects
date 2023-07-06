from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
       if self.score > self.high_score:
           self.high_score = self.score
           with open("data.txt", mode="w") as data:
               data.write(f"{self.high_score}")

       self.score = 0
       self.update_scoreboard()


    def increase(self):
        self.score += 1
        self.update_scoreboard()





    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER. ", align="center", font=("Courier", 24, "normal"))


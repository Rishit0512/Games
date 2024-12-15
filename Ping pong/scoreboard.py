from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):  
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    
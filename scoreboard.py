from turtle import Turtle
ALIGNMENT= "center"
FONT=("Courier,24,normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    with open ("snake_game\score.txt") as file:
      self.new_score=int(file.read())
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.hideturtle()
    self.update()
    
  def update(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.new_score}",align=ALIGNMENT,font=FONT)
    
  def reset(self):
    if self.score>self.new_score:
      self.new_score=self.score
      with open("snake_game\score.txt","w") as file:
        file.write(f"{self.new_score}")
    self.score=0
    self.update()   

  def inc_score(self):
    self.score+=1
    self.update()

    
    
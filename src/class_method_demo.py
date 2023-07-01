class Player:
  def __init__(self, color, points):
    self.color = color
    self.points = points

  def tellscore(self):
      print("I am",self.color ," we have " ,self.points , "points!")
  def goal(self):
      self.points = self.points+1
      return self.points
p1 = Player("Blue", 0)
p1.goal()
p1.tellscore()


class Player:
  def __init__(self, color, points):
    self.color = color
    self.points = points

p1 = Player("Blue", 300)

print("The", p1.color , "contender has", p1.points, "points!")

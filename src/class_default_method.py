class Player:
    '''stores data on team colors and points.'''
    points = 0


    def __init__(self):
        self.color = input("What color do I get?: ")
    def tellscore(self):
         print("I am", self.color ,",  we have " ,self.points , "points!")
    def goal(self):
        self.points = self.points+1
        return self.points
p1 = Player()
p2 = Player()

p1.goal()
p1.goal()
p1.tellscore()

p2.goal()
p2.tellscore()



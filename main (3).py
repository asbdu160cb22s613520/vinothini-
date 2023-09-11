class player:
 def paly(self):
  print("The player is playing cricket.")
class Batsman(player):
  def play(self):
    print("The batsman is batting")
class Bowler(player):
  def play(self):
    print("The bowler is bowling")
#creating objects and calling the play()method
if __name__=="__main__":
 batsman=Batsman()
 bowler=Bowler()
batsman.play()
bowler.play()
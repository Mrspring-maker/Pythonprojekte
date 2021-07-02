class backpack:
    def __init__(self):
        self.players= [
           {
              "player" : "player1",
              "name": "Hans"
           },
           {
              "player" : "player1",
              "name": "Franz"
           }
]
    def print(self):
        print (self.players)

class Test:
     b = backpack()
     b.print()

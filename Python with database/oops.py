class PartyAnimal:
    x = 0
    name = ''
    points = 0
    def __init__(self,z):
        self.name = z
        print(self.name,'constructor created')
    def party(self):
        self.x = self.x +1
        print(self.name,"party count", self.x)
class FootballFan(PartyAnimal):
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name,"points",self.points)
        
s = PartyAnimal("sally")
s.party()
j = FootballFan("ria")
j.party()
s.party()
j.touchdown()

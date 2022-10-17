class Band:
    instances = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        solos = []
        for player in self.members:
            solos.append(player.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name, type, instrument):
        self.name = name
        self.type = type
        self.instrument = instrument
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.type} instance. Name = {self.name}"
    
    def get_instrument(self):
        return f'{self.instrument}'
    

class Guitarist(Musician):
    def __init__(self, name):
      super().__init__(name, "Guitarist", "guitar")
    

    def play_solo(self):  
        return "face melting guitar solo"
    

class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name, "Bassist", "bass")
    

    def play_solo(self):  
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "Drummer", "drums")
    
    
    def play_solo(self): 
        return "rattle boom crash"

from abc import ABC, abstractmethod




class Musician(ABC):

    def __init__(self,name):
        self.name=name
    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod
    def __repr__ (self):

     def get_instrument (self):
        pass
    
        pass
    def play_solo(self):
        pass
   


class Guitarist(Musician):
  
    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    def __repr__ (self):
        return (f"Guitarist instance. Name = {self.name}")
    def get_instrument(self):
        return "guitar" 
    def __init__(self,name):
        self.name=name
    def play_solo(self): 
     return 'face melting guitar solo' 



class Drummer(Musician):

    def __str__(self):
                return (f"My name is {self.name} and I play drums")
    def __repr__ (self):
        return (f"Drummer instance. Name = {self.name}")
    def get_instrument(self):
        return "drums"
    def __init__(self,name):
        self.name=name
    def play_solo(self): 
     return 'rattle boom crash'



class Bassist(Musician):
   

    def __init__(self,name):
        self.name=name
    def __str__(self):
                return (f"My name is {self.name} and I play bass")
    def __repr__ (self):
        return (f"Bassist instance. Name = {self.name}")
    def get_instrument(self):
        return "bass"
    def play_solo(self): 
     return 'bom bom buh bom'


class Band(Musician):
   

    instances=[]       
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)

        
    def play_solos(self):
         return [instance.play_solo() for instance in self.members]

    @classmethod  
    def to_list(cls):
     return cls.instances

     
    def __str__(self):
        pass
    def __repr__ (self):
        pass




import random
class Jatekos:
    def __init__(self,nev:str="Jatekos",emo:str="", poz:int=0):
        self.nev=nev
        self.eletero=3+random.randint(1,6)
        self.emo=emo
        self.poz=poz
    
    def get_eletero(self):
            return self.eletero
    
    def get_emo(self):
            return self.emo
    
    def get_poz(self):
            return self.pot
    
    def set_poz(self):
          self.poz=random.randint(0,2)
                 
    def set_eletero(self):
        pont=random.randint(0,1)
        self.eletero-=pont

    def __str__(self):
        return f"Név: {self.nev}, Életerő: {self.eletero}, Emo: {self.emo}, Pozíció: {self.poz}"

          
    


    
    
    
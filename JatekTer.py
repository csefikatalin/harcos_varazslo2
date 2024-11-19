from Jatekos import Jatekos

class Jatekter:
    def __init__(self) -> None:
        self.kor=1
        self.harcos=Jatekos("Boromir","🤷‍♂️",0)
        self.varazslo=Jatekos("Szarumán","🧙‍♂️",2)
        self.list=[]
        self.listabeallit()
        self.kiir()

    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
        print(f"* {self.list[0]:<3} {self.list[1]:^3} {self.list[2]:>3} *   | A {self.harcos.nev} életereje: {self.harcos.eletero} |  | A {self.varazslo.nev} életereje: {self.varazslo.eletero} |")
        print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
        print("")

    def harc(self):
        self.harcos.set_eletero()
        self.varazslo.set_eletero()

    def listabeallit(self):
        self.list=[]
        for i in range(0,3):
            self.list.append("_")
        hp=self.harcos.poz
        vp=self.varazslo.poz
        if (hp==vp):
            self.list[hp]="⚔"
            self.harc()
        else:
            self.list[self.harcos.poz]=self.harcos.emo
            self.list[self.varazslo.poz]=self.varazslo.emo


    def jatek(self):        
        while (self.harcos.eletero>0 and self.varazslo.eletero>0):    
            """  itt jönnek a lépések. Minden körben minden játékos véletlenszerűen lép valamelyik mezőre """
            self.kor+=1
            self.harcos.set_poz()
            self.varazslo.set_poz()
            self.listabeallit()    
            self.kiir()
            input()

        if self.harcos.eletero>self.varazslo.eletero:
            print(f"{self.harcos.nev} {self.harcos.emo} nyert! {self.varazslo.nev} {self.varazslo.emo} elbukott!")
        
        else:
            print(f"{self.varazslo.nev} {self.varazslo.emo} nyert! {self.harcos.nev} {self.harcos.emo}  elbukott!")



        

from Jatekos import Jatekos

"""  adott egy 3 elemű játéktér.  """
"""Kezdetben a Játékosok a két végpontban vannak, majd kockával dobunk mindegyiknek és léttetjük őket. 
Ha azonos mezőre léptek, akkro sebzik egymást véletlenszerűen. 

"""
# 

def kiir(list,harcos,varazslo, kor):
    print(f"{kor}. kör")
    print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
    print(f"* {list[0]:<3} {list[1]:^3} {list[2]:>3} *   | A {harcos.nev} életereje: {harcos.eletero} |  | A {varazslo.nev} életereje: {varazslo.eletero} |")
    print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
    print("")

def harc(harcos,varazslo):
    harcos.set_eletero()
    varazslo.set_eletero()

def listabeallit(harcos,varazslo):
    lista=[]
    for i in range(0,3):
        lista.append("_")
    hp=harcos.poz
    vp=varazslo.poz
    if (hp==vp):
        lista[hp]="⚔"
        harc(harcos,varazslo)
    else:
        lista[harcos.poz]=harcos.emo
        lista[varazslo.poz]=varazslo.emo

    return lista


kor=1
harcos=Jatekos("Boromir","🤷‍♂️",0)
varazslo=Jatekos("Szarumán","🧙‍♂️",2)
list=listabeallit(harcos,varazslo)
kiir(list,harcos, varazslo,kor)

while (harcos.eletero>0 and varazslo.eletero>0):    
    """  itt jönnek a lépések. Minden körben minden játékos véletlenszerűen lép valamelyik mezőre """
    kor+=1
    harcos.set_poz()
    varazslo.set_poz()
    list=listabeallit(harcos,varazslo)    
    kiir(list,harcos, varazslo,kor)
    input()

if harcos.eletero>varazslo.eletero:
    print(f"A {harcos.nev} {harcos.emo} nyert! A {varazslo.nev} {varazslo.emo} elbukott!")
  
else:
      print(f"A {varazslo.nev} {varazslo.emo} nyert! A {harcos.nev} {harcos.emo}  elbukott!")


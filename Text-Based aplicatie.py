#Text Based aplicatie van Thies van der Zon
#Doel: Maak een verhaal met 4 VERSCHILLENDE soorten einde

print("Hoi, in dit spel ga je beleven hoe het is om uit een land te vluchten")
print("Je wordt wakker, het is wazig, er zit een gat in je muur waarschijnlijk door een bom, Je denkt snel en rent naar buiten")
print("Je ziet wat voor zootje het buiten is waar ga je naartoe LINKS of RECHTS?")

def beginverhaal():
    
    print("LINKS = A RECHTS = B")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        #verhaalstuk14()
    elif antwoord == 'B':
        print("--------")
#verhaalstuk13()
    else:
        print(antwoord, "= INVALID")
beginverhaal()

def verhaalstuk1():
    print("")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        verhaalstuk4()
    elif antwoord == 'B':
        print("Dit is verhaalstuk1")
        verhaalstuk4()
    else:
        print(antwoord, "INVALID")

def verhaalstuk2():
    print("Je begint te rijden")
    antwoord = input()
    if antwoord == 'A':
        print("Dit is verhaalstuk 2")
        verhaalstuk18()
    elif antwoord == 'B':
        print("Dit is verhaalstuk2")
        verhaalstuk21()
    elif antwoord == 'C':
        print("Dit is verhaalstuk2")
        verhaalstuk1()
    else:
        print(antwoord, "INVALID")


def verhaalstuk3():
    print("Dit is verhaalstuk3")
    antwoord = input()
    if antwoord == 'A':
        print("Dit is verhaalstuk3")
        verhaalstuk11()
    elif antwoord == 'B':
        print("Dit is verhaalstuk3")
        verhaalstuk17()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk4():
    print("Dit is verhaalstuk4")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk10()
    elif antwoord == 'B':
        print("")
        verhaalstuk8()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk5():
    print("Dit is verhaalstuk5")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVLID")
        
def verhaalstuk6():
    print("Dit is verhaalstuk6") 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk7():
    print("Dit is verhaalstuk7")
    antwoord = input()
    if antwoord == 'A':
        print("")
        einde2()
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk8():
    print("Dit is verhaalstuk8")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk9():
    print("Dit is verhaalstuk9")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk20()
    elif antwoord == 'B':
        print("")
        verhaalstuk16()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk10():
    print("Dit is verhaalstuk10")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk9()
    elif antwoord == 'B':
        print("")
        verhaalstuk15()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk11():
    print("Dit is verhaalstuk11") 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk12():
    print("Dit is verhaalstuk12")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk12()
    elif antwoord == 'B':
        print("")
        verhaalstuk3()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk13():
    print("verhaalstuk13")
    antwoord = input()
    if antwoord == 'A':
        print("Test")
        verhaalstuk5()
    elif antwoord == 'B':
        print("hoe")
        verhaalstuk19()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk14():
    print("Je gaat naar links, en begint te rennen naar de auto je stapt in  en gaat rijden waar ga je naartoe? \nNOORD = A, ZUID = B ")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        verhaalstuk2()
    elif antwoord == 'B':
        print("-")
        verhaalstuk13()
    else:
        print(antwoord, "INVALID")
verhaalstuk14()

#def einde1
    
#def einde2

#def einde3

#def einde4



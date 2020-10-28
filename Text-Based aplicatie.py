#Text Based aplicatie van Thies van der Zon
#Doel: Maak een verhaal over een vluchteling met 4 VERSCHILLENDE soorten einde

print("Hoi, in dit spel ga je beleven hoe het is om uit een land te vluchten")
print("Je wordt wakker in een puinhoop, het is wazig, er zit een gat in je muur waarschijnlijk door een bom,\nHet is al de zoveelste keer dat er wordt gevochten, je maakt een besluit om weg te gaan van oorlog en gaat vluchten.")
print("Je ziet wat voor zootje het buiten is waar ga je naartoe LINKS of RECHTS?")


def einde1():
    print("einde doodlopend")  
def einde2():
    print("einde normaal")
def einde3():
    print("einde kwaad")
def einde4():
    print("einde goed")
    
#def gameRunning():

#while gameRunning == True:
    #beginverhaal()   

def beginverhaal():

    print("LINKS = A RECHTS = B")
    antwoord = input(":")
    if antwoord == 'A':
        print("-")
        #verhaalstuk14()
    elif antwoord == 'B':
        print("--------")
        #verhaalstuk13()
    else:
        print(antwoord, "= INVALID")


def verhaalstuk1():
    print("Je rijdt naar rechts maar je hebt geen benzine meer, dus moet weer verder gaan lopen. Na een tijdje lopen ben je moe en besluit een pauze te nemen.\nJeziet dat je nog weinig water hebt Wat doe je? BESPAREN = A, OPDRINKEN = B ")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        verhaalstuk4()
    elif antwoord == 'B':
        print("-")
        verhaalstuk4()
    else:
        print(antwoord, "INVALID")

def verhaalstuk2():
    print("Je stapt in en komt uiteindelijk op een kruising aan. Waar ga je naartoe?\n LINKS = A \n RECHTDOOR = B \n RECHTS = C")
    antwoord = input()
    if antwoord == 'A':
        print("----")
        verhaalstuk18()
    elif antwoord == 'B':
        print("----")
        verhaalstuk21()
    elif antwoord == 'C':
        print("----")
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
    print("-")
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
    print("Je gaat zoeken naar je vrienden,je vindt uiteindelijk een goede vriend van je en gaat samen met hem vluchten.\nSamen eindigen jullie in een vluchtenlingenkamp hopend op een beter leven")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

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
    print("Je gaat mee met een het groepje vluchtelingen, na een lange reis zijn jullie ontsnapt uit het oorlogsgebied en op naar een beter leven")
    antwoord = input()
    if antwoord == 'A':
        print("")
        einde2()
    elif antwoord == 'B':
        print("")
        einde2()
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
    print("Je vindt het te riskant en besluit om niet mee te gaan en gaat zelf door. ")
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
    print("Je gaat naar rechts, en gaat bedenken of je ergens bij vrienden naartoe kan of is het toch slimmer om alleen te blijven en risico's te vermijden. Wat doe je? ANDEREN ZOEKEN = A, ALLEEN VERDER = B")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk5()
    elif antwoord == 'B':
        print("")
        verhaalstuk19()
    else:
        print(antwoord, "INVALID")
        
verhaalstuk13()

def verhaalstuk14():
    print("Je gaat naar links, en ziet je auto staan. Wat doe je? INSTAPPEN = A, VERDER OP VOET = B ")
    antwoord = input()
    if antwoord == 'A':
        print("----")
        verhaalstuk2()
    elif antwoord == 'B':
        print("----")
        verhaalstuk13()
    else:
        print(antwoord, "INVALID")

verhaalstuk14()


def verhaalstuk15():
 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk16():
 
    antwoord = input()
    if antwoord == 'A':
        print("")
        #einde3()
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk17():
 
    antwoord = input()
    if antwoord == 'A':
        print("")
        #einde1()
    elif antwoord == 'B':
        print("")
        #einde1() 
    else:
        print(antwoord, "INVALID")

def verhaalstuk18():
 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk19():
    print("Je hebt gekozen om alleen verder te gaan, Je gaat richting het Zuiden waar je hoopt dat het velig is.\nJe komt een groepje andere vluchtelingen tegen, hun plan is om over de grens proberen te komen en ze vragen je mee Wat doe je? NIET MEEGAAN = A, MEEGAAN =B")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        verhaalstuk12()
    elif antwoord == 'B':
        print("-")
        verhaalstuk7()
    else:
        print(antwoord, "INVALID")

def verhaalstuk20():
 
    antwoord = input()
    if antwoord == 'A':
        print("")
        einde4()
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk21():
 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")



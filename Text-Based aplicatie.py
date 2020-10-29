#Text Based aplicatie van Thies van der Zon
#Doel: Maak een verhaal over een vluchteling met 4 VERSCHILLENDE soorten einde
import os, time

def einde1():
    print("einde doodlopend")  
def einde2():
    print("einde normaal")
def einde3():
    print("einde kwaad")
def einde4():
    print("einde goed")
    
print("Hoi, in dit spel ga je beleven hoe het is om uit een land te vluchten")
print("Hoe werkt het?, het is erg simpel het is een meerkeuze verhaal") 

def Enterknop():
    time.sleep(1)
    print("\n\n\nOm door te gaan klick op 'ENTER'!")

    answer0 = input()

    if answer0 == "":
        print("")

    os.system("cls")
    

def beginverhaal():
    os.system("cls")
    print("Je wordt wakker in een puinhoop, het is wazig, er zit een gat in je muur waarschijnlijk door een bom,\nHet is al de zoveelste keer dat er wordt gevochten, je maakt een besluit om weg te gaan van oorlog en gaat vluchten.")
    print("Je ziet wat voor zootje het buiten is waar ga je naartoe LINKS of RECHTS?")
    print("LINKS = A RECHTS = B")
    antwoord = input(":")
    if antwoord == 'A':
        print("-")
        verhaalstuk14()
    elif antwoord == 'B':
        print("--------")
        verhaalstuk13()
    else:
        print(antwoord, "= INVALID")


def verhaalstuk1():
    os.system("cls")
    print("Je rijdt naar rechts maar je hebt geen benzine meer, dus moet weer verder gaan lopen. Na een tijdje lopen ben je moe en besluit een pauze te nemen.\n")
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
    os.system("cls")
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
    os.system("cls")
    print("Je besluit land inwaarst te gaan, laag op ratsoenen moet je een keuze maken door gaan en hopen op het beste of overnachten en in de ochtend door gaan DOORGAAN = A , OVERNACHTEN = B")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk11()
    elif antwoord == 'B':
        print("")
        verhaalstuk17()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk4():
    os.system("cls")
    print("Je komt een 2 groepen mensen tegen, Je bedenkt dat het misschien wel handig is dat je met hen meet gaat\nGroep 1 gaat met de auto \nGROEP 1 = A, GROEP 2 = B")
    antwoord = input()
    if antwoord == 'A':
        print("-")
        verhaalstuk10()
    elif antwoord == 'B':
        print("-")
        verhaalstuk8()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk5():
    os.system("cls")
    print("Je gaat zoeken naar je vrienden,je vindt uiteindelijk een goede vriend van je en gaat samen met hem vluchten.\nSamen eindigen jullie in een vluchtenlingenkamp hopend op een beter leven")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk6():
    #os.system("cls")
    print("Je hebt besloten om de richting van de kust te gaan, Je herrinert je dat er een stad is richting de kust, Wil je er naartoe? JA = A NEE = B  ") 
    antwoord = input()
    if antwoord == 'A':
        print("helaas de stad is compleet verwoest dan maar weer weer op naar de kust") 
        verhaalstuk4()  
    elif antwoord == 'B':
        verhaalstuk4()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk7():
    os.system("cls")
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
    os.system("cls")
    print("Je gaat met groep 2 mee naar het blijkt dat. Je vraagt waar ze precies naar toe gaan, ze vertellen je over een bootsmokkel plek waar je het land uit kan gaan")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk9():
    os.system("cls")
    print("Je komt aan bij de haven en voelt je geweldig, maar het is nog niet af.\nJe moet een groot bedrag betalen en hebt net aan genoeg maar je wilt niet al je geld kwijt. gelukkig is er ook een goedkopere optie voor een andere boot Wat doe je?\nDURE BOOT = A , GOEDKOPERE BOOT = B")
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
    os.system("cls")
    print("Je hebt gekozen voor groep 1 uit, je vraagt waar je naartoe gaat, Ze zeggen dat je naar de haven gaat en met een boot naar een ander land gaat.\nJe kan ook kiezen om niet naar de haven te gaan en weer lopend verder\nHAVEN = A, UITSTAPPEN = B")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk9()
    elif antwoord == 'B':
        print("")
        verhaalstuk15()
    else:
        print(antwoord, "INVALID")
#Einde1        
def verhaalstuk11():
    os.system("cls")
    print("Je zet door een hoopt voor het best, maar helaas haal je het niet en vriest dood") 
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk12():
    os.system("cls")
    print("Je vindt het te riskant en besluit om niet mee te gaan en gaat zelf door. Je gaat een besluit maken, richting de kust te gaan of landinwaarts trekken\nKUST = A , LAND INWAARST = B")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk6()
    elif antwoord == 'B':
        print("")
        verhaalstuk3()
    else:
        print(antwoord, "INVALID")
        
def verhaalstuk13():
    os.system("cls")
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
        


def verhaalstuk14():
    os.system("cls")
    print("Je gaat naar links, en ziet je auto staan. Wat doe je? INSTAPPEN = A, VERDER OP VOET = B")
    antwoord = input()
    if antwoord == 'A':
        print("----")
        verhaalstuk2()
    elif antwoord == 'B':
        print("----")
        verhaalstuk13()
    else:
        print(antwoord, "INVALID")


def verhaalstuk15():
    os.system("cls")
    antwoord = input()
    if antwoord == 'A':
        print("")   
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk16():
    os.system("cls")
    einde3()
  

#einde1()
def verhaalstuk17():
    os.system("cls")
    print("Je gaat overnachten en gaat door in de ochtend, je maakt een lange dat je net aan overleeft komt aan in een vluchtenlingkamp")
    antwoord = input()
    if antwoord == 'A':
        print("")
        
    elif antwoord == 'B':
        print("")
         
    else:
        print(antwoord, "INVALID")

def verhaalstuk18():
    os.system("cls")
    print("Je bent naar links gegaan en na een lange reis kom je bij een smokkelbedrijf langs, de smokkelaars verdelen de mensen in groepen, je probeert één van de smokkelaars op te kopen Welke groep wil je in?\nGROEP 1 = A, GROEP 2 = B")
    antwoord = input()
    if antwoord == 'A':
        print("")
        verhaalstuk10()
    elif antwoord == 'B':
        print("")
        verhaalstuk8()
    else:
        print(antwoord, "INVALID")

def verhaalstuk19():
    os.system("cls")
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
    os.system("cls")
    antwoord = input()
    if antwoord == 'A':
        print("")
        einde4()
    elif antwoord == 'B':
        print("")
    else:
        print(antwoord, "INVALID")

def verhaalstuk21():
    os.system("cls")
    print("Je gaat rechtdoor en na een lange reis eindig je veiling in een vluchtelingenkamp en hier ga je dood aan voedselvergifteging")
    einde1()
    Enterknop()

gameRunning = True
while gameRunning == True:
    beginverhaal()
    print("Wil je nog een keer spelen? JA of NEE")
    antwoord = input()
    if antwoord == 'JA':
        continue
    elif antwoord == 'NEE':
        break
    



print ("Hello You!, ik ben Thies")
print("Wie ben jij?")

naam = input("Wat is jouw naam?:")
print("Hallo: " + naam)

print("----------------------------------------")

print("Ik ben Thies")

print("----------------------------------------")

print ("Ik ben een nieuwkomer op deze school,en ik heb hier een klein quizje om mij te leren kennen")


print("----------------------------------------")

print ("Vraag 1: Waar woon ik?")

print("A: Tuitjehorn")
print("B: Warmenhuizen")
print("C: Alkmaar")

antwoord = input()

if antwoord == "A":
    print("Nee, dit is fout")
    print ("Het goede antwoord is B: Warmenhuizen")

if antwoord == "B":
    print ("Dit is goed, ik woon in Warmenhuizen")
    print ("Op naar de volgende vraag")

if antwoord == "C":
    print("Nee, dit is fout")
    print ("Het goede antwoord is B: Warmenhuizen")


print("----------------------------------------")


print ("Vraag 2: Hoe oud ben ik?")

print("A: 15")
print("B: 16")
print("C: 17")

antwoord = input()

if antwoord == "A":
    print("Dit is goed, ik ben 15 jaar oud.")
    
if antwoord == "B":
    print ("Dit is fout, Het goede antwoord is A: 15")

if antwoord == "C":
    print ("Dit is fout, Het goede antwoord is A: 15")


print("----------------------------------------")



print("Vraag 3: Wat is mijn favoriete serie")

print("A: Hoops")
print("B: Lucifer")
print("C: Friends")

antwoord = input()

if antwoord == "A":
    print ("Dit is fout, Het goede antwoord is C: Friends")
  
if antwoord == "B":
    print ("Dit is fout, Het goede antwoord is C: Friends")

if antwoord == "C":
    print ("Dit goed, mijn favoriete serie is Friends")


print("----------------------------------------")


print(" ")


print("----------------------------------------")

print("Waar wil je het nu over hebben?  ")


print("----------------------------------------")


print("Je wordt wakker met een kater, JONKO of GLAS WATER")
keuze = input()
if keuze == 'JONKO':
    print("Goeie keuze dikke toeter wordt geconsumeerd...")

elif keuze == 'GLAS WATER':
    print("Prima, je bent weer gehydrateerd tijd voor een jonko!")

else:
    print (keuze, "INVALID")

print("________________________________________________________________")

print("Je moet naar school, hoe ga je heen? BUS of PITBIKE")
keuze = input()

if keuze == 'BUS':
    print("Helaas! bus gemist, Dan maar met de pitbike")

elif keuze == 'PITBIKE':
    print("Dikke wheelies trekken op de pitbike best gaan.")

else:
    print (keuze, "INVALID")

print("________________________________________________________________")

print("Je komt op school net optijd in de les, Je hebt alleen helemaal geen zin in school, SLAPEN of UIT DE LES GAAN")
keuze = input()

if keuze == 'SLAPEN':
    print("Je gaat liggen op je tafel en valt in slaap, alleen wordt je al 5 min later wakker met een docent die voor je neus staat te schreeuwen, dus je wordt uit de les gestuurd")


elif keuze == 'UIT DE LES GAAN':
    print("Je bent er alweer klaar mee en besluit weg te gaan, de docent vraagt wat je gaat doen dus je bedenkt een simpel smoesje")

else:
    print (keuze, "INVALID")

print("________________________________________________________________")
    
print("Je bent weer buiten, pakt de pitbike, doet een burnout op het plein crost vol weg. Onderweg naar huis kom je een donerzaak en hebt wel honger, DONER of NAAR HUIS")
keuze = input()

if keuze == 'DONER':
    print("Je neemt een lekker broodje doner met saus, als je klaar bent ga je weer lekker door naar huis")

elif keuze == 'NAAR HUIS':
    print("Je hebt niet zo'n zin in doner gaat rijd door")

else:
    print (keuze, "INVALID")

print("________________________________________________________________")

print("Je bent weer thuis gaat lekker op de bank zitten en zet de tv aan, BIER of JONKO")
keuze = input()

if keuze == 'BIER':
    print("Je tikt een koud pilsie open en geniet van je vrije dag")

elif keuze == 'JONKO':
    print("Je draait een dikke toeter een gaat lekker smoken op de bank")

else:
    print (keuze, "INVALID")






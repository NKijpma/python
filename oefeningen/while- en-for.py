'''10 Opdrachtjes met loops en input 

    Vraag een getal en print alle getallen van 0 tot dat getal met een while loop. gedaan

    Vraag een getal en print alle getallen van 0 tot dat getal met een for loop. gedaan

    Vraag een getal en print "Hoi!" dat aantal keer met een while loop.  gedaan

    Vraag een woord en print elk teken van het woord apart met een for loop. gedaan

    Vraag een geheim woord met een while loop, blijf vragen tot het juiste woord is ingevoerd. gedaan

    Vraag een getal en print de even getallen tot dat getal met een for loop. gedaan

    Vraag de naam van 3 vrienden met een for loop en print ze allemaal achter elkaar. gedaan

    Vraag een zin en print elk woord apart (hint: gebruik .split()) met een for loop. gedaan

    Vraag een getal en print een aftelling tot 0 met een while loop. gedaan

    Vraag de gebruiker om 5 getallen in te voeren en bereken en print de som met een for loop. gedaan

  '''

mijn_getal = int(input("geef een getal op:"))
mijn_stapje = 0
while mijn_stapje <=  mijn_getal: #als mijn_getal gelijk is aan mijn_stapje stopt het
    print(mijn_stapje)
    mijn_stapje+=1


mijn_getal_2 = int(input("geef een getal op! :"))
mijn_stapje_2 = 0
for mijn_stapje_2 in range (mijn_getal_2 + 1): #range gaat omhoog tot en met mijn_getal_2 + 1
 print(mijn_stapje_2)
 mijn_stapje_2+=1
        
mijn_hoi= int(input("geef een getal op!? :"))
mijn_stapje_3 = 0
while mijn_stapje_3 < mijn_hoi: 
 print("holla!")
 mijn_stapje_3+=1

woord= (input("geef een woord op: "))
for letter in woord: print(letter) # voor elke letter in woord print letter

raden = input("raad het woord: ")
while raden != "floorp": #!=betekent is niet gelijk aan(onthouden) , floorp is een browser 
    raden = input("fout! raad nog een keer: ")
    if raden == "floorp": #==betekent is gelijk aan (onthouden) 
     print("goed geraden!")

mijn_getal_4 = int(input("geef een getal! :"))
for mijn_stapje_4 in range (0, mijn_getal_4 + 1): 
    if mijn_stapje_4 % 2 == 0: #% is modulo laat alleen de rest zien nu laat het alleen om de 2 zien (even)
        print(mijn_stapje_4)

vrienden = input("noem een vriend op: ")
vrienden_2 = input("noem nog een vriend op: ")
vrienden_3 = input("noem nog een laatste vriend op: ")
print("je vrienden zijn dus: " + vrienden + ", " + vrienden_2+ ", " + vrienden_3 + "?")

zin = input("geef een zin op: ")
for woord in zin.split(): #zet elke spatie onder elkaar(string naar lijst)
    print(woord)

mijn_getal_5 = int(input("geef een getal op: "))
mijn_stapje_5 = 0
while mijn_getal_5 >= mijn_stapje_5: 
    print(mijn_getal_5)
    mijn_getal_5-= 1


one = int(input("geef een getal op: "))
two = int(input("geef nog een getal op: ")) 
thre = int(input("geef nog een getal op: "))
fou = int(input("geef nog een getal op: "))
fiv = int(input("geef nog een getal op: "))
vijf_getallen = [one + two + thre + fou + fiv]
for getal in vijf_getallen:
    print(vijf_getallen)
    #denk niet dat het zo moest maar hij doet het!

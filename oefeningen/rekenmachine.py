# berekeningen.py
'''Opdracht: Bouw een rekenmachine
Opdrachtomschrijving
Maak een programma dat eenvoudige rekensommen kan uitvoeren. Het programma vraagt aan de gebruiker welke bewerking hij wil uitvoeren (optellen, aftrekken, vermenigvuldigen of delen) en welke twee getallen daarbij horen. Vervolgens voert het programma de berekening uit en toont het resultaat.

Wat je moet gebruiken:
Functies: schrijf voor elke bewerking (optellen, aftrekken, vermenigvuldigen, delen) een aparte functie.

If-statements: gebruik if, elif en else om te bepalen welke bewerking de gebruiker heeft gekozen.

Booleaanse expressies: controleer of de invoer geldig is (bijvoorbeeld of de gebruiker een geldig getal invoert).

Modules: zet je functies in een aparte module, bijvoorbeeld berekeningen.py, en importeer ze in je hoofdprogramma.

User input: gebruik input() om de gebruiker om gegevens te vragen.

Return: zorg dat je functies het resultaat teruggeven.

Error handling: controleer op ongeldige invoer (zoals delen door nul).

Uitgebreide opdrachtstappen
Maak een module berekeningen.py met vier functies:

optellen(a, b) — geeft a + b terug.

aftrekken(a, b) — geeft a - b terug.

vermenigvuldigen(a, b) — geeft a * b terug.

delen(a, b) — geeft a / b terug, maar controleer eerst of b niet nul is!

Maak een hoofdprogramma rekenmachine.py dat:

De gebruiker vraagt welke bewerking hij wil uitvoeren (bijvoorbeeld: typ "optellen", "aftrekken", "vermenigvuldigen" of "delen").

De gebruiker vraagt om twee getallen.

Controleert of de invoer geldig is (gebruik eventueel try-except of een booleaanse check).

Roept de juiste functie uit berekeningen.py aan.

Print het resultaat.

Vraagt of de gebruiker nog een berekening wil doen (ja/nee).

Als de gebruiker nee zegt, stopt het programma.

Zorg voor duidelijke en nette output.

Voorbeeld van input:

Welke bewerking wil je uitvoeren? (optellen, aftrekken, vermenigvuldigen, delen): optellen
Voer het eerste getal in: 4
Voer het tweede getal in: 7
Resultaat: 11
Wil je nog een berekening doen? (ja/nee): ja

Welke bewerking wil je uitvoeren? (optellen, aftrekken, vermenigvuldigen, delen): delen
Voer het eerste getal in: 10
Voer het tweede getal in: 0
Fout: delen door nul is niet toegestaan.
Wil je nog een berekening doen? (ja/nee): nee
Programma gestopt. Tot ziens!
'''
def main():
    while True:
        multi = input("wat soort bewerking wil je uitvoeren? (optellen, aftrekken, keer, delen): ")
        a = int(input("voer het eerste getal in: "))
        b = int(input("voer het tweede getal in: "))
        
        if multi not in ["optellen", "aftrekken", "keer", "delen"]:  # als het ingevuld woord niet 1 van deze is print ongeldig
            print("Ongeldige bewerking. Kies uit: optellen, aftrekken, keer, delen.")

        if multi == "optellen": #als multi gelijk is aan optellen print a + b
            print(a + b)   # voegt input a en b samen 
        if multi == "aftrekken":
            print(a - b)
        if multi == "keer":
            print(a * b)
        if multi == "delen":
            if b != 0:  # als b niet gelijk is aan 0, print antwoord, anders print error
                print(a / b)
            else:
                print("Fout: delen door 0 is niet toegestaan.")  

        ja_nee = input("Wil je nog een berekening doen? (ja/nee): ")
        if ja_nee == "nee":
            print("Tot ziens!")
            break #exit de loop

main()

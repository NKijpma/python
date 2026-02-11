'''
Maak een programma dat een wishlist maakt voor steam. 
Een wishlist is een lijst van spellen die je graag wilt hebben. 
De gebruiker krijgt als het start de volgende opties te zien: 
1) Spellen bekijken 
2) Spel toevoegen 
3) Totaalprijs berekenen 
4) Afsluiten 
Wanneer je dus een “1” invoert, krijg je de spellen te zien, 
Elk spel op een regel met naam en prijs 
Wanneer je “2” invoert mag je info invullen voor een spel, 
Het programma vraagt dan eerst naar een naam van een spel en de prijs 
Wanneer je “3” invoert krijg je de totaalprijs van alle spellen bij elkaar te zien 
Wanneer je “4” invoert sluit het programma af 
Wanneer je iets anders invoer zegt het programma “ongeldige invoer” 

Tip! Gebruik Match: 
https://www.w3schools.com/python/python_match.asp 

Ondersteuning: 
Maak een object voor de class Game. 
Een game heeft: 
een naam 
 een prijs. 
Een Game kan: 
Uitgeprint worden (dus naam en prijs) 
Maak een object voor de class Wishlist 
Een whislist heeft  
een verzameling van het type Game met de naam games. 
Een whislist kan: 
Een spel toevoegen 
Uitprinten welke spellen er in de wishlist zitten en hun prijs 
Uitrekenen hoe duur de wishlist is 
# '''
# class wishist:
#     def __init__(self,game,add,tot_prijs,close):
#         self.game=game
#         self.add=add
#         self.tot_prijs=tot_prijs
#         self.close=close
# game_list= ("1.metro gravity","2.")
# my_list=[]
# def wish_fist():

#     while True:
#         keuze= print (int)(input("wat will je doen: (1.mij games ,2.add game ,3.totaal prijs, 4.stop): "))
#         if keuze not in ["mij games", "add game", "totaal prijs", "stop",1,2,3,4]:  # als het ingevuld woord niet 1 van deze is print ongeldig
#             print("Ongeldige bewerking. Kies uit: mij games, add game, totaal prijs, stop.")
#         my_list.append(keuze)
#         # if keuze=="mij games":
# #         #             return 

# class steam:
#    def __init__(self,games,add,totaal,close):
#                 self.games=games 
#                 self.add=add 
#                 self.totaal=totaal
#                 self.close=close
#    def __str__(self):
#         return(f"Game: {self.games}"),((f"Toevoegen: {self.add}")),(f"Totaalprijs: {self.totaal}"),(f"Afsluiten: {self.close}")


class Game:
      def __init__(self,naam,prijs):
        self.naam= naam
        self.prijs= prijs
      def __str__(self):
        return(f"game naam:{self.naam}€:{self.prijs}")
      
class Wishlist:
    def __init__(self):
        self.games = []

    def add_game(self,game):
        self.games.append(game)

    def print_wishlist(self):
        for game in self.games:
            print(game)

    def total_price(self):
        return sum(game.prijs for game in self.games)#summary/totaal
  
my_wishlist = Wishlist()
my_wishlist.add_game(Game("metro gravity",12.79))
my_wishlist.add_game(Game("Made in Abyss: Binary Star Falling into Darkness",59.99))
my_wishlist.add_game(Game("Blasphemous 2",29.99))

while True:
    keuze = input(
    "Kies een optie:\n" #/n is /niewe regel
    "1. My wishlist\n"
    "2. Add\n"
    "3. Totaal prijs\n"
    "4. Stop\n"
)   
    match keuze:
        case "1":
            my_wishlist.print_wishlist()
        case "2":
            naam = input("Naam van het spel: ")
            prijs = float(input("Prijs van het spel: "))
            game = Game(naam, prijs)
            my_wishlist.add_game(game)
        case "3":
            totaal = my_wishlist.total_price()
            print(f"Totaalprijs: €{totaal:.2f}")
        case "4":
            break
        case _:
          print("Ongeldige invoer")

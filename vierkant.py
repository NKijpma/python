#vierkant
''' Opdracht 2: 
Maak een programma dat de gebruiker vraagt voor een getal, een binnen symbool en een buiten symbool. 
Maak het programma dat aan de hand van die waardes een vierkant met een rand tekent. 
Tip: gebruik input() en int()!
Voorbeeld van output: 

Hoe groot moet het vierkant zijn?
5
Welk symbool heeft de rand?
X 
Welk symbool heeft de inhoud?
# 
Output: 
XXXXX
X###X
X###X
X###X
X###X
XXXXX 
'''
grootte = int(input("Geef de grootte van het vierkant: "))
binnen = input("Geef het symbool voor binnen: ")
buiten = input("Geef het symbool voor buiten: ")

for skibidi in range(grootte): #skibidi is een vorm van variabel , boom ook (slaat de range van grootte op)
    for boom in range(grootte): #range is van 0 tot grootte-1
        if skibidi == 0 or skibidi == grootte-1 or boom == 0 or boom == grootte-1:  #== betekent is gelijk aan en = is wordt
            print(buiten, end="") #"" is een spatie 
        else:                                          
            print(binnen, end="")
    print()  

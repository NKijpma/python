#12345 for en while loops
'''Maak doormiddel van for-loops de volgende figuren: 
***** 
***** 
***** 
***** 
***** 

* 
**  
***  
****  

***** 
***** 
****  
*** 
**  
* 

12345
12345
12345
12345
12345 

1 
12 
123 
1234 
12345 

….1 
…12 
..123 
.1234 
12345 
Opdracht 1.2: 
Maak de zelfde opdrachten in opdracht 1 met while loops '''
for i in range(5):    # i is een vorm van variabel
    print("*****") # print een rij van 5 sterren 

print() #print een lege regel

for i in range(1, 6): # 1 tm 5
    print("*" * i)   # 1* 2** 3*** 4**** 5*****

print()

for i in range(5, 0, -1):
    print("*" * i)

print()
#zelfde maar cijfers
for i in range(5):
    print("12345")

print()

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1))) #join plakt alles aan elkaar (zonder spaties)

print()

for i in range(1, 6):
    print("." * (5 - i) + "".join(str(j) for j in range(1, i+1)))


i = 0    # i wordt 0
while i < 5: # als i minder is dan 5 print ***** dus dat kan hij maar 5 keer doen want 0 + 1*5 = 5
    print("*****")
    i += 1   #i + 1 tot dat i 5 is

print()

i = 1
while i <= 5: #while i is kleiner dan of gelijk aan 5 print *
    print("*" * i) 
    i += 1 #+= betekent i = i + 1

print()

i = 5
while i > 0:
    print("*" * i)
    i -= 1

print()

i = 0
while i < 5:
    print("12345")
    i += 1

print()

i = 1
while i <= 5:
    print("".join(str(j) for j in range(1, i+1))) #range bepaalt de lengte van hoe ver hij gaat, "" is niks (spaties)
    i += 1

print()

i = 1
while i <= 5:
    print("." * (5 - i) + "".join(str(j) for j in range(1, i+1))) #join plakt alles aan elkaar (zonder spaties)
    i += 1

import random

#initialization
turns=1
cards=[]
face_cards=["Jack" ,"Queen" , "King" , "Ace"]
y=0
suit=["_hearts", "_spades", "_diamonds", "_clubs"]

#adds the numbers 2-10 to the deck
for i in range(9):
	cards.append(i+2)
	
#adds face cards to the deck
cards.extend(face_cards[:])

#maps each of the four suits onto each card in the deck
while y<4:
	cards.extend(list(map(lambda x: str(x)+ suit[y] , cards[:13])))
	y+=1
	
#removes cards without a suit from the deck
cards[:13]=[]

#creates a constant deck "cardso" where every 13 cards are in order from least to greatest
cardso= tuple(cards)

#shuffles the deck and deals the cards into 2 hands
random.shuffle(cards)
hand1=cards[:26]
hand2=cards[-26:]
random

def war(type):
	print("WAR!")
	print(hand1[type] + " and " + hand2[type] + " were played")

	warCard1=cardso.index(hand1[type + 2])
	warCard2=cardso.index(hand2[type + 2])
	while warCard1>12:
		warCard1-=13
	while warCard2>12:
		warCard2-=13

	if warCard1>warCard2:
		x=1
		savings = []
		winnings = []
		while (type-x)>=-1:
			savings.append(hand1[x])
			winnings.append(hand2[x])
			x+=2
		print("player 1's " + hand1[type + 2] + " beat player 2's " + hand2[type + 2])		
		print("player 1 saved " + str(savings) + " and player 2 lost " + str(winnings))
		hand1.extend(hand1[:(type + 2)])
		hand1.extend(hand2[:(type + 2)])
		del hand1[:(type + 2)]
		del hand2[:(type + 2)]
		savings = []
		winnings = []

	elif warCard2>warCard1:
		x=1
		savings = []
		winnings = []
		while (type-x)>=-1:
			savings.append(hand2[x])
			winnings.append(hand1[x])
			x+=2
		print("player 2's " + hand2[type + 2] + " beat player 1's " + hand1[type + 2])		
		print("player 2 saved " + str(savings) + " and player 1 lost " + str(winnings))
		hand2.extend(hand1[:(type + 2)])
		hand2.extend(hand2[:(type + 2)])
		del hand1[:(type + 2)]
		del hand2[:(type + 2)]
		savings = []
		winnings = []

	else:
		type+=2
		war(type)

while len(hand1)>0 and len(hand2)>0:
	card1=cardso.index(hand1[0])
	card2=cardso.index(hand2[0])
	while card1>12:
		card1-=13
	while card2>12:
		card2-=13
	if card1>card2:
		hand1.append(hand1[0])
		hand1.append(hand2[0])
		print("player 1's " + hand1[0] + " beat player 2's " + hand2[0])  
		del hand1[0]
		del hand2[0]
		turns+=1
	elif card2>card1:
		hand2.append(hand1[0])
		hand2.append(hand2[0])
		print("player 2's " + hand2[0] + " beat  player 1's " + hand1[0]) 
		del hand1[0]
		del hand2[0]
		turns+=1
	else:
		try:
			turns+=1
			war(0)
		except IndexError:
				if len(hand1)<len(hand2):
					print("player 2 won in " + str(turns) + " turns")
					break
				else:
					print("player 1 won in " + str(turns) + " turns")
					break
if len(hand1)==0:
	print("player 2 won in " + str(turns) + " turns")
if len(hand2)==0:
	print("player 1 won in " + str(turns) + " turns")
	
			

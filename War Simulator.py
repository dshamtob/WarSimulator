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

def war():
	print("WAR!")
	print(hand1[0] + " and " + hand2[0] + " were played")
	if warCard1>warCard2:
			print("player 1's " + hand1[2] + " beat player 2's " + hand2[2])		
			print("player 1 saved " + hand1[1] + " and player 2 lost " + hand2[1])
			hand1.extend(hand1[:2])
			hand1.extend(hand2[:2])
			del hand1[:2]
			del hand2[:2]
			
	elif warCard2>warCard1:
			print("player 2's " + hand2[2] + " beat player 1's " + hand1[2])		
			print("player 2 saved " + hand2[1] + " and player 1 lost " + hand1[1])
			hand2.extend(hand1[:2])
			hand2.extend(hand2[:2])
			del hand1[:2]
			del hand2[:2]
			
	else:
			print("WAR!")
			print(hand1[2] + " and " + hand2[2] + " were played")
			doubleWarCard1=cardso.index(hand1[4])
			doubleWarCard2=cardso.index(hand2[4])
			while doubleWarCard1>12:
				doubleWarCard1-=13
			while doubleWarCard2>12:
				doubleWarCard2-=13
			if doubleWarCard1>doubleWarCard2:
					print("player 1's " + hand1[4] + " beat player 2's " + hand2[4])		
					print("player 1 saved " + hand1[3] + " and " + hand1[1] + " and player 2 lost " + hand2[1] + " and " + hand2[3])
					hand1.extend(hand1[:4])
					hand1.extend(hand2[:4])
					del hand1[:4]
					del hand2[:4]
			elif doubleWarCard2>doubleWarCard1:
					print("player 2's " + hand2[4] + " beat player 1's " + hand1[4])		
					print("player 2 saved " + hand2[1] + " and " + hand2[3] + " and player 1 lost " + hand1[1] + " and " + hand1[3] )
					hand2.extend(hand1[:4])
					hand2.extend(hand2[:4])
					del hand1[:4]
					del hand2[:4]
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
			warCard1=cardso.index(hand1[2])
			warCard2=cardso.index(hand2[2])
			while warCard1>12:
				warCard1-=13
			while warCard2>12:
				warCard2-=13
			turns+=1
			war()
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
	

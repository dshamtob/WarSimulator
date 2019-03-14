import random
cards=[]
face_cards=["Jack" ,"Queen" , "King" , "Ace"]
y=0
suit=["_hearts", "_spades", "_diamonds", "_clubs"]

for i in range(9):
	cards.append(i+2)
cards.extend(face_cards[:])
while y<4:
	cards.extend(list(map(lambda x: str(x)+ suit[y] , cards[:13])))
	y+=1
cards[:13]=[]
cardso=cards
random.shuffle(cards)
hand1=cards[:26]
hand2=cards[-26:]
random
def war():
	print("WAR!")
	print(hand1[0] + " and " + hand2[0] + " were played")
	if hand1[2]>hand2[2]:
			print("player 1's " + hand1[2] + " beat player 2's " + hand2[2])		
			print("player 1 saved " + hand1[1] + " and player 2 lost " + hand2[1])
			hand1.extend(hand1[:2])
			hand1.extend(hand2[:2])
			del hand1[:2]
			del hand2[:2]
	elif hand2[2]>hand1[2]:
			print("player 2's " + hand2[2] + " beat player 1's " + hand1[2])		
			print("player 2 saved " + hand2[1] + " and player 1 lost " + hand1[1])
			hand2.extend(hand1[:2])
			hand2.extend(hand2[:2])
			del hand1[:2]
			del hand2[:2]
	else:
			print("WAR!")
	print(hand1[2] + " and " + hand2[2] + " were played")
	if hand1[4]>hand2[4]:
			print("player 1's " + hand1[4] + " beat player 2's " + hand2[4])		
			print("player 1 saved " + hand1[3] + " and " + hand1[1] + " and player 2 lost " + hand2[1] + " and " + hand2[3])
			hand1.extend(hand1[:4])
			hand1.extend(hand2[:4])
			del hand1[:4]
			del hand2[:4]
	elif hand2[4]>hand1[4]:
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
	elif card2>card1:
		hand2.append(hand1[0])
		hand2.append(hand2[0])
		print("player 2's " + hand2[0] + " beat  player 1's " + hand1[0]) 
		del hand1[0]
		del hand2[0]
	else:
		try:
			war()
		except IndexError:
				if hand1<3:
					print("player 2 wins")
				else:
					print("player 1 wins")
if hand1==0:
	print("player 2 wins")
else:
	print("player 1 wins")
		
			
		

	

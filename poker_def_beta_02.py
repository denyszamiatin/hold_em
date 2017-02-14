#!/usr/bin/python3.5
# coding utf-8

"""
ENG: Poker - Texas Hold'em
RUS: Покер - Техасский Холдем
"""
import random


def deck_new():
        """ENG: It creates the deck
        RUS: Создает колоду"""
        deck = []
        ranks = [
                        "2", "3", "4", "5", "6", "7", "8", "9",
                        "10", "jack", "queen", "king", "ace"]
        # suits = ["spades", "hearts", "clubs", "diamonds"]
		# black symbols
        suits = [chr(0x2660), chr(0x2665), chr(0x2663), chr(0x2666)]
        # white symbols
        # suits = [chr(0x2664), chr(0x2661), chr(0x2667), chr(0x2662)]

        for suit in suits:
                for rank in ranks:
                        card = (rank, suit)
                        deck.append(card)
        return(deck)


def deck_rand():
        """ENG: It shuffle the deck
        RUS: Перемешивает колоду"""
        deck = deck_new()
        deck_rand = []
        while len(deck) > 0:
                card = random.choice(deck)
                deck.remove(card)
                deck_rand.append(card)
        # print(len(deck_rand))
        return deck_rand


def result_math(a):
		dict = {
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
		'10': 10,
		'jack': 11,
		'queen': 12,
		'king': 13,
		'ace': 14
		}
		return dict.get(a)

        
def result_pairs(user_card, table_card):
        """ENG: Finds and count pairs cards.
        RUS: Находит и считает парные карты."""
        result = 0
        if user_card[0][0].count(user_card[1][0]):
                result += result_math(user_card[1][0])
        while len(table_card) > 0:
                card = table_card[0][0]
                if user_card[0][0].count(card):
                        result += result_math(card)
                if user_card[1][0].count(card):
                        result += result_math(card)
                table_card.remove(table_card[0])
        return int(result)


def result_kicker_max(user_card):
        return max(result_math(user_card[0][0]), result_math(user_card[1][0]))
		
		
def result_kicker_min(user_card):
		return min(result_math(user_card[0][0]), result_math(user_card[1][0]))
		

# print(poker_deck())
deck = deck_rand()
table = deck[0:5]
user1 = deck[5:7]
user2 = deck[7:9]

print("Table: ", table[0:3])
print("User1: ", user1)
print("User2: ", user2)
input("move1 \n")
print("Table: ", table[0:4])
print("User1: ", user1)
print("User2: ", user2)
input("move2 \n")
print("Table: ", table[0:5])
print("User1: ", user1)
print("User2: ", user2)
input("move3 \n")

print("Score: The winner, who has a lot of pair cards!!!")
p1 = result_pairs(user1[:], table[:])
p2 = result_pairs(user2[:], table[:])

if p1 == p2:
	print("Score: The winner, who has a kicker_max!!!")
	p1 = result_kicker_max(user1[:])
	p2 = result_kicker_max(user2[:])
	if p1 == p2:
		p1 = result_kicker_min(user1[:])
		p2 = result_kicker_min(user2[:])

print("Score: User1 =", p1, " User2 =", p2)
if p1 > p2:
        print("Winner is User1!!!")
elif p1 < p2:
        print("Winner is User2!!!")
else:
        print("Friendship wins!!!")

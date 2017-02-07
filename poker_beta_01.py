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


def scroll_math(a):
        if a == "2":
                return int(2)
        elif a == "3":
                return int(3)
        elif a == "4":
                return int(4)
        elif a == "5":
                return int(5)
        elif a == "6":
                return int(6)
        elif a == "7":
                return int(7)
        elif a == "8":
                return int(8)
        elif a == "9":
                return int(9)
        elif a == "10":
                return int(10)
        elif a == "jack":
                return int(11)
        elif a == "queen":
                return int(12)
        elif a == "king":
                return int(13)
        elif a == "ace":
                return int(14)


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
p1 = 0
p2 = 0

if user1[0][0].count(user1[1][0]):
        print("player 1::", user1[1][0], ":::", p1, "+", scroll_math(user1[1][0]))
        p1 += scroll_math(user1[1][0])
player1_deck = table[:]
while len(player1_deck) > 0:
        card = player1_deck[0][0]
        if user1[0][0].count(card):
                print("player 1:", card, ":::", p1, "+", scroll_math(card))
                p1 += scroll_math(card)
        if user1[1][0].count(card):
                print("player 1:", card, ":::", p1, "+", scroll_math(card))
                p1 += scroll_math(card)
        player1_deck.remove(player1_deck[0])

if user2[0][0].count(user2[1][0]):
        print("player 2::", user2[1][0], ":::", p2, "+", scroll_math(user2[1][0]))
        p2 += scroll_math(user2[1][0])
player2_deck = table[:]
while len(player2_deck) > 0:
        card = player2_deck[0][0]
        if user2[0][0].count(card):
                print("player 2:", card, ":::", p2, "+", scroll_math(card))
                p2 += scroll_math(card)
        if user2[1][0].count(card):
                print("player 2:", card, ":::", p2, "+", scroll_math(card))
                p2 += scroll_math(card)
        player2_deck.remove(player2_deck[0])

if p1 == p2:
        print("Score: The winner, who has a big card!!!")
        p1 = scroll_math(user1[0][0]) + scroll_math(user1[1][0])
        p2 = scroll_math(user2[0][0]) + scroll_math(user2[1][0])

print("Score: p1 =", p1, " p2 =", p2)
if p1 > p2:
        print("Winner is pleyer1!!!")
elif p1 < p2:
        print("Winner is pleyer2!!!")
else:
        print("Friendship wins!!!")

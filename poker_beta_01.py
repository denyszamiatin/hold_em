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
        suits = [chr(0x2660), chr(0x2665), chr(0x2663), chr(0x2666)]  # black symbols
        # suits = [chr(0x2664), chr(0x2661), chr(0x2667), chr(0x2662)] white symbols

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
        print("player 1::", user1[1][0])
        p1 += 1
player1_deck = table[:]
while len(player1_deck) > 0:
        card = player1_deck[0][0]
        if user1[0][0].count(card):
                print("player 1:", card)
                p1 += 1
        if user1[1][0].count(card):
                print("player 1:", card)
                p1 += 1
        player1_deck.remove(player1_deck[0])

if user2[0][0].count(user2[1][0]):
        print("player 2::", user2[1][0])
        p2 += 1
player2_deck = table[:]
while len(player2_deck) > 0:
        card = player2_deck[0][0]
        if user2[0][0].count(card):
                print("player 2:", card)
                p2 += 1
        if user2[1][0].count(card):
                print("player 2:", card)
                p2 += 1
        player2_deck.remove(player2_deck[0])

if p1 > p2:
        print("Winner is pleyer1!!!")
elif p1 < p2:
        print("Winner is pleyer2!!!")
else:
        print("Friendship wins!!!")

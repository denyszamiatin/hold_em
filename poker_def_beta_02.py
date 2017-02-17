#!/usr/bin/python3.5
# coding utf-8

"""
ENG: Poker - Texas Hold'em
RUS: Покер - Техасский Холдем
"""
import random


def deck_rand():
        """ENG: It creates and shuffle the deck
        RUS: Создает и перемешивает колоду"""
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        suits = [chr(0x2660), chr(0x2665), chr(0x2663), chr(0x2666)]
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck


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


def result_three(user_card, table_card):
        result = 0
        table = [a for a, b in table_card]
        user = [a for a, b in user_card]
        for card in user:
                if table.count(card) == 2:
                        print("Three: ", card)
                        result = result_math(card)
        return int(result)


def result_pairs(user_card, table_card):
        """ENG: Finds and count pairs cards.
        RUS: Находит и считает парные карты."""
        result = 0
        table = [a for a, b in table_card]
        user = [a for a, b in user_card]
        for card in user:
                if table.count(card) == 1:
                        print("Pair: ", card)
                        result = result_math(card)
        return int(result)


def result_kicker_max(user_card):
        return max(result_math(user_card[0][0]), result_math(user_card[1][0]))


def result_kicker_min(user_card):
        return min(result_math(user_card[0][0]), result_math(user_card[1][0]))


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

print("Score: The winner, who has three identical cards!!!")
p1 = result_three(user1[:], table[:])
p2 = result_three(user2[:], table[:])
if p1 == p2:
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

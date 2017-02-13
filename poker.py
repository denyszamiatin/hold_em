#!/usr/bin/python3.6
# coding utf-8

import random
import itertools
from collections import deque

from enum import Enum, auto

# comment this to get real random
#random.seed(11)

class Suits(Enum):
    SPADE = auto()
    HEART = auto()
    CLOVER = auto()
    TILES = auto()

ranks = list(range(2, 15))

class Deck():
    def __init__(self):
        # be careful! deck is not shuffled after init
        self.deck = list(itertools.product(ranks, Suits))

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self, n): # maybe we should call it smt like deal ?
        try:
            return [self.deck.pop() for _ in range(n)]
        except IndexError:
            raise IndexError('deck is empty!!!')

def street_catcher(user_set):
    """mechanism for catching streets. Will (hopefully) return all streets included in user_set"""

    # user_set is of format [(rank, suite), ....]
    # we wanna use sets later, so packing it into dict
    # user_ranks = {
    #      rank: list(of suits )
    # }
    # ex:
    # user_set = [(2, spade), (3, spade), (2, hearts)]
    # will turn into
    # user_ranks = {
    #     2: [spade, hearts],
    #     3: [spade]
    # }
    # we will need to turn it back to tuples in the end

    user_ranks = dict.fromkeys([r for r, s in user_set], ())
    for r, s in user_set:
        user_ranks[r] += (s,)

    street_len = 5
    ranks_deq = deque(ranks)

    streets = []
    for _ in range(len(ranks)):
        street = set(list(ranks_deq)[:street_len])
        if street <= user_ranks.keys():
            streets.append(street)
        ranks_deq.rotate()

    # i know its not too readable
    catched_streets = \
        [list(itertools.product(*[[(rank, suit) for suit in user_ranks[rank]] for rank in s])) for s in streets]
    catched_streets = [j for i in catched_streets for j in i]

    return catched_streets

# these are good object for unittests
def biggest_card(user_set):
    user_ranks = [r for r, s in user_set]
    return max(user_ranks)

def pair(user_set):
    user_ranks = [r for r, s in user_set]
    return bool([r for r in ranks if user_ranks.count(r) == 2])

def double_pair(user_set):
    user_ranks = [r for r, s in user_set]
    return 1 < len([r for r in ranks if user_ranks.count(r) == 2])

def triple(user_set):
    user_ranks = [r for r, s in user_set]
    return bool([r for r in ranks if user_ranks.count(r) == 3])

def street(user_set):
    user_ranks = [r for r, s in user_set]
    return (max(user_ranks)-min(user_ranks) == 4) and len(set(user_ranks)) == 5

def flash(user_set):
    user_suits = set(s for r, s in user_set)
    return len(user_suits) == 1

def full(user_set):
    user_ranks = [r for r, s in user_set]
    ranks_count = {r: user_ranks.count(r) for r in ranks}
    return all([3 in ranks_count.values(), 2 in ranks_count.values()])

def kare(user_set):
    user_ranks = [r for r, s in user_set]
    return bool([r for r in ranks if user_ranks.count(r) == 4])

def street_flash(user_set):
    return street(user_set) and flash(user_set)


combinations = {
    #format is
    #combination check function (return bool),  : combination name (return bool), combination weight
    pair          : ('pair', 50),
    double_pair   : ('double_pair', 100),
    triple        : ('triple', 150),
    street        : ('street', 200),
    flash         : ('flash', 250),
    full          : ('full', 300),
    kare          : ('kare', 350),
}

def get_user_result(table, user_set):
    succeed = [check for check in combinations if check(table + user_set)]
    return sorted(succeed, key=lambda x: combinations[x][1])[-1] # i know this ugly


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    table = deck.pop(5)
    u1 = deck.pop(2)
    u2 = deck.pop(2)


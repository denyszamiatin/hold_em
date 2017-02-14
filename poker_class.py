from collections import UserDict, defaultdict

from collections import deque

import itertools
import random

from enum import Enum, auto

# TODO: ANY of poker hands is a 5-card combination - so each combination checking function have to return list of 5 cards.

# TODO: probably each combination can have its own type, types need to have defined priority against each other
# TODO: each type need to have comparison function to compare against combination of the same type

class Suits(Enum):
    SPADE = auto()
    HEART = auto()
    CLOVER = auto()
    TILES = auto()


RANKS = list(range(2, 15))

class Deck():
    def __init__(self):
        self.deck = list(itertools.product(RANKS, Suits))
        random.shuffle(self.deck)

    def pop(self, n):
        try:
            result = CardsSet()
            for _ in range(n):
                r, s = self.deck.pop()
                result += CardsSet({r: (s,)})
            return result

        except IndexError:
            raise IndexError('deck is empty!!!')


class CardsSet(UserDict):
    def __init__(self, cards_set_like=None):
        self.data = dict.fromkeys(RANKS, ())

        if cards_set_like:
            for r, s in cards_set_like.items():
                self.data[r] += s

    def __add__(self, other):
        if not isinstance(other, CardsSet):
            raise ValueError('Only CardsSet can be added to cards set')

        return CardsSet({rank: suites + other[rank] for rank, suites in self.data.items()})

    @property
    def ranks(self):
        return [rr for r, s in self.data.items() for rr in [r] * len(s)]

# straights

def straights_catcher(user_set: CardsSet):
    """mechanism for catching streets. Will (hopefully) return all streets included in user_set"""
    #TODO: https://www.contrib.andrew.cmu.edu/~gc00/reviews/pokerrules#straight
    user_ranks = set(user_set.ranks)

    street_len = 5
    ranks_deq = deque(RANKS)

    catched_streets = []
    for _ in range(len(RANKS)):
        street = set(list(ranks_deq)[:street_len])
        if street <= user_ranks:
            catched_streets.append(street)
        ranks_deq.rotate()

    return catched_streets

def straight_flush(user_set: CardsSet):
    """ return is a list of straight_flushes
    each straight flush is a tuple (straight_contents)
    """

    straights = straights_catcher(user_set)

    str_flushes = []
    for suite in Suits:
        for strght in straights:
            candidate = [r for r in strght if suite in user_set[r]]
            if 5 == len(candidate):
                str_flushes.append(candidate)

    return str_flushes

def royal_flush(user_set: CardsSet):
    return bool([f for f in straight_flush(user_set) if f == RANKS[-5:]])


def pair(user_set: CardsSet):
    user_ranks = user_set.ranks
    return [r for r in RANKS if user_ranks.count(r) == 2]

def two_pairs(user_set: CardsSet):
    #TODO: need to choose two highest pairs here as hand can contain more than 2
    return 2 <= len(pair(user_set))


if __name__ == '__main__':
    a = Deck()
    u1 = CardsSet(a.pop(2))
    u2 = CardsSet(a.pop(2))
    table = CardsSet(a.pop(5))

    b = CardsSet({4: (5, 6, 7, 8), 5: (9, 10)})


    # check straights
    print(royal_flush(CardsSet({
        9 :(Suits.SPADE,),
        10:(Suits.SPADE,),
        11:(Suits.SPADE,),
        12:(Suits.SPADE,),
        13:(Suits.SPADE,),
        14:(Suits.SPADE,),
    })))

    # check pairs

    print(two_pairs(
        CardsSet({
                9 :(Suits.SPADE, Suits.HEART),
                10:(Suits.SPADE,),
                11:(Suits.SPADE,),
                12:(Suits.SPADE, Suits.CLOVER),
                13:(Suits.SPADE,),
                14:(Suits.SPADE,),
        })))

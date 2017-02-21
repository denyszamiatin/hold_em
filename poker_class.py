#!/usr/bin/python3.6

from collections import UserDict
import itertools
import random
from enum import Enum, auto


class Suits(Enum):
    SPADE = auto()
    HEART = auto()
    CLOVER = auto()
    TILES = auto()


RANKS = list(range(2, 15))


class Deck:
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
    def flipped(self):
        return {suite: tuple([rank for rank in RANKS if suite in self.data[rank]]) for suite in Suits}

    @property
    def ranks(self):
        return [rr for r, s in self.data.items() for rr in [r] * len(s)]


def pair(user_set: CardsSet):
    return [r for r in RANKS if user_set.ranks.count(r) == 2]


def two_pairs(user_set: CardsSet):
    pairs =[]
    #TODO: need to choose two highest pairs here as hand can contain more than 2
    if len(pair(user_set)) >= 2:
        pairs = pair(user_set)
    return pairs


def triple(user_set: CardsSet):
    return [r for r in RANKS if user_set.ranks.count(r) == 3]


def straights_catcher(user_set: CardsSet):
    """mechanism for catching straights. Returns all streets included in user_set"""
    all_straights_n = 10
    user_ranks = set(user_set.ranks)
    street_len = 5
    
    source = RANKS[-1:] + RANKS
    catched_streets = [source[i: i + street_len] for i in range(all_straights_n) 
                       if set(source[i: i + street_len]) <= user_ranks]
    
    return catched_streets


def flush(user_set: CardsSet):
    flush_len = 5

    flush = {s: sorted(r)[-flush_len:] for s, r in user_set.flipped.items() if len(r) >= flush_len}

    return flush


def full(user_set: CardsSet):
    return triple(user_set), pair(user_set)


def kare(user_set: CardsSet):
    return [rank for rank in user_set.ranks if user_set.ranks.count(rank) == 4]


def straight_flush(user_set: CardsSet):
    """ returns is a list of straight_flushes
    each straight flush is a list for now (straight_contents)
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


class Player:

    def __init__(self, player_id):
        self.player_id = player_id
        self.user_cards = CardsSet()
        self.table_cards = CardsSet()
        self.user_set = self.user_cards + self.table_cards

    def get_cards(self, deck, n_cards):
        self.user_cards = self.user_cards + deck.pop(n_cards)
        self.user_set = self.user_cards + self.table_cards

    def add_table_cards(self, table):
        self.table_cards = self.table_cards + table

    def remove_user_cards(self):
        self.user_cards = CardsSet()

    def remove_table_cards(self):
        self.table_cards = CardsSet()

    def change_user_set(self, user_set):
        self.user_set = user_set

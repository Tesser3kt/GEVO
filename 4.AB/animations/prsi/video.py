import numpy as np

from dataclasses import dataclass
from enum import Enum
from random import shuffle, choice
from manim import *

PLAYER_COLORS = [
    TEAL,
    PINK,
    YELLOW
]
CENTER_CARD_FONT_SIZE = 60
CENTER_CARD_WIDTH = 1.5
CENTER_CARD_HEIGHT = 2

FIRST_CARD_COLOR = WHITE

HAND_CARD_FONT_SIZE = 30
HAND_CARD_WIDTH = 0.75
HAND_CARD_HEIGHT = 1


class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Rank(Enum):
    ACE = 1
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


@dataclass
class Card:
    suit: Suit
    rank: Rank


@dataclass
class Deck:
    deck: list[Card]
    stack: list[Card]

    def __renew_deck(self) -> None:
        last_card = self.stack.pop()
        self.deck = self.stack
        shuffle(self.deck)
        self.stack = [last_card]

    def pop(self) -> Card:
        if not self.deck:
            self.__renew_deck()

        return self.deck.pop()

    def add_to_stack(self, card: Card) -> None:
        self.stack.append(card)


def get_deck() -> list[Card]:
    deck = [Card(suit, rank) for suit in Suit for rank in Rank]
    shuffle(deck)

    return Deck(deck, [deck.pop()])


def get_suit_symbol(suit: Suit, color: str, size: int) -> VMobject:
    if suit == Suit.HEARTS:
        return MathTex(r"\heartsuit", color=color, font_size=size)
    elif suit == Suit.DIAMONDS:
        return MathTex(r"\diamondsuit", color=color, font_size=size)
    elif suit == Suit.CLUBS:
        return MathTex(r"\clubsuit", color=color, font_size=size)
    elif suit == Suit.SPADES:
        return MathTex(r"\spadesuit", color=color, font_size=size)


def get_card_rank(rank: Rank, color: str, size: int) -> VMobject:
    if rank == Rank.ACE:
        return Tex(r"A", color=color, font_size=size)
    elif rank == Rank.SEVEN:
        return Tex(r"7", color=color, font_size=size)
    elif rank == Rank.EIGHT:
        return Tex(r"8", color=color, font_size=size)
    elif rank == Rank.NINE:
        return Tex(r"9", color=color, font_size=size)
    elif rank == Rank.TEN:
        return Tex(r"10", color=color, font_size=size)
    elif rank == Rank.JACK:
        return Tex(r"J", color=color, font_size=size)
    elif rank == Rank.QUEEN:
        return Tex(r"Q", color=color, font_size=size)
    elif rank == Rank.KING:
        return Tex(r"K", color=color, font_size=size)


def get_card(suit: Suit, rank: Rank, color: str, font_size: int,
             width: int, height: int) -> VMobject:
    card_rank = get_card_rank(
        rank, color, font_size)
    suit_symbol = get_suit_symbol(
        suit, color, font_size
    )
    card = VGroup(card_rank, suit_symbol).arrange(RIGHT, buff=0.05)

    square = RoundedRectangle(
        corner_radius=0.1,
        color=color,
        width=width,
        height=height,
    ).align_to(card)
    card.add(square)

    return card


def get_hand(cards: list[Card], player: int) -> VGroup:
    hand = VGroup()
    for card in cards:
        card = get_card(
            card.suit, card.rank, PLAYER_COLORS[player],
            HAND_CARD_FONT_SIZE, HAND_CARD_WIDTH, HAND_CARD_HEIGHT
        )
        hand.add(card)

    hand.rotate_about_origin(-PI / 2 + (PI / 2) * player)

    return hand


def card_to_play(hand: list[Card], last_card: Card) -> tuple[int, int]:
    # always take 5 cards on king of spades
    if last_card.rank == Rank.KING and last_card.suit == Suit.SPADES:
        return -1, 5

    # count only rank for seven or ace
    valid_cards = [i for i, card in enumerate(
        hand) if card.suit == last_card.suit]

    # take 2 or 0 cards if last card is 7 or ace, resp.
    if last_card.rank == Rank.SEVEN:
        if not valid_cards:
            return -1, 2
        return choice(valid_cards), 0

    if last_card.rank == Rank.ACE:
        if not valid_cards:
            return -1, 0
        return choice(valid_cards), 0

    # count rank and suit for everything else
    # this function always gets queen of the changed suit if queen was played
    valid_cards = [i for i, card in enumerate(
        hand) if card.rank == last_card.rank or card.suit == last_card.suit]

    if not valid_cards:
        return -1, 1
    return choice(valid_cards), 0


class Prsi(Scene):
    def get_show_hand_anim(self, hand: VGroup, shift_by: np.ndarray,
                           arrange_by: np.ndarray) -> None:
        return [FadeIn(card) for card in hand] +\
            [hand.animate.arrange(arrange_by, buff=0.15).shift(shift_by)]

    def construct(self):
        deck = get_deck()
        players = [
            [deck.pop() for _ in range(4)]
            for _ in range(3)
        ]
        cur_player = 0

        # intro section
        self.next_section('Intro', skip_animations=True)

        first_card = get_card(
            deck.stack[-1].suit, deck.stack[-1].rank, FIRST_CARD_COLOR,
            CENTER_CARD_FONT_SIZE, CENTER_CARD_WIDTH, CENTER_CARD_HEIGHT
        )
        self.play(FadeIn(first_card))

        player_hands = [
            get_hand(players[i], i) for i in range(3)
        ]
        player_hands[0].shift(3 * LEFT)
        player_hands[1].shift(3 * DOWN)
        player_hands[2].shift(3 * RIGHT)

        self.play(
            *self.get_show_hand_anim(player_hands[0], 3 * LEFT, DOWN),
            *self.get_show_hand_anim(player_hands[1], 3 * DOWN, RIGHT),
            *self.get_show_hand_anim(player_hands[2], 3 * RIGHT, DOWN)
        )

        # game section
        self.next_section('Game', skip_animations=False)

        new_suit = 0
        while all((len(hand) > 0 for hand in players)):
            last_card = deck.stack[-1]

            # make a copy of last card and change suit to new suit if queen
            # was played
            if last_card.rank == Rank.QUEEN:
                last_card = last_card.copy()
                last_card.suit = Suit(new_suit)

            card_index, penalty = card_to_play(players[cur_player], last_card)
            break

        self.pause(2)

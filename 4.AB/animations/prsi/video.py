from dataclasses import dataclass
from enum import Enum
from queue import Queue
from random import shuffle
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


class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Ranks(Enum):
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
    suit: Suits
    rank: Ranks


def get_deck() -> list[Card]:
    cards = [Card(suit, rank) for suit in Suits for rank in Ranks]
    shuffle(cards)

    deck = Queue()
    for card in cards:
        deck.put(card)

    return deck


def get_suit_symbol(suit: Suits, color: str, size: int) -> VMobject:
    if suit == Suits.HEARTS:
        return MathTex(r"\heartsuit", color=color, font_size=size)
    elif suit == Suits.DIAMONDS:
        return MathTex(r"\diamondsuit", color=color, font_size=size)
    elif suit == Suits.CLUBS:
        return MathTex(r"\clubsuit", color=color, font_size=size)
    elif suit == Suits.SPADES:
        return MathTex(r"\spadesuit", color=color, font_size=size)


def get_card_rank(rank: Ranks, color: str, size: int) -> VMobject:
    if rank == Ranks.ACE:
        return Tex(r"A", color=color, font_size=size)
    elif rank == Ranks.SEVEN:
        return Tex(r"7", color=color, font_size=size)
    elif rank == Ranks.EIGHT:
        return Tex(r"8", color=color, font_size=size)
    elif rank == Ranks.NINE:
        return Tex(r"9", color=color, font_size=size)
    elif rank == Ranks.TEN:
        return Tex(r"10", color=color, font_size=size)
    elif rank == Ranks.JACK:
        return Tex(r"J", color=color, font_size=size)
    elif rank == Ranks.QUEEN:
        return Tex(r"Q", color=color, font_size=size)
    elif rank == Ranks.KING:
        return Tex(r"K", color=color, font_size=size)


def get_card(suit: Suits, rank: Ranks, color: str, font_size: int,
             width: int, height: int) -> VMobject:
    card_rank = get_card_rank(
        rank, color, font_size)
    suit_symbol = get_suit_symbol(
        suit, color, font_size
    )
    card = VGroup(card_rank, suit_symbol).arrange(RIGHT, buff=0.1)

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

    hand.arrange(RIGHT, buff=0.3)
    hand.rotate_about_origin(-PI / 2 + (PI / 2) * player)

    return hand


class Prsi(Scene):
    def construct(self):
        deck = get_deck()
        players = [
            [deck.get() for _ in range(4)]
            for _ in range(3)
        ]
        cur_player = 0
        first_card = deck.get()

        # intro section
        self.next_section('Intro', skip_animations=False)
        self.add(NumberPlane(
            background_line_style={
                'stroke_opacity': 0.5
            }
        ))

        first_card = get_card(
            first_card.suit, first_card.rank, FIRST_CARD_COLOR,
            CENTER_CARD_FONT_SIZE, CENTER_CARD_WIDTH, CENTER_CARD_HEIGHT
        )
        self.play(FadeIn(first_card))

        player_hands = [
            get_hand(players[i], i) for i in range(3)
        ]
        player_hands[0].shift(3 * LEFT)
        player_hands[1].shift(3 * DOWN)
        player_hands[2].shift(3 * RIGHT)

        self.add(*player_hands)

        self.pause(2)

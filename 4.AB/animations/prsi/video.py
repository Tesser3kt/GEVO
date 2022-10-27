from winreg import REG_NO_LAZY_FLUSH
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
CENTER_CARD_COLOR = LIGHT_BROWN

HAND_CARD_FONT_SIZE = 25
HAND_CARD_WIDTH = 0.6
HAND_CARD_HEIGHT = 0.8
HAND_CARD_BUFF = 0.15

QUESTION_COLOR = WHITE
QUESTION_FONT_SIZE = 60


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


def get_card(card: Card, color: str, font_size: int,
             width: int, height: int) -> VMobject:
    card_rank = get_card_rank(
        card.rank, color, font_size
    )
    suit_symbol = get_suit_symbol(
        card.suit, color, font_size
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
            card, PLAYER_COLORS[player],
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
    def hand_anim(self, hand: VGroup, player: int) -> AnimationGroup:
        if player == 0:
            anim = hand.animate.arrange_in_grid(
                6, 3, buff=HAND_CARD_BUFF, flow_order='dl').move_to(
                    3 * LEFT, aligned_edge=RIGHT
            )
        elif player == 1:
            anim = hand.animate.arrange_in_grid(
                3, 6, buff=HAND_CARD_BUFF, flow_order='rd').move_to(
                    2 * DOWN, aligned_edge=UP
            )
        else:  # player == 2
            anim = hand.animate.arrange_in_grid(
                6, 3, buff=HAND_CARD_BUFF, flow_order='dr').move_to(
                    3 * RIGHT, aligned_edge=LEFT
            )

        return AnimationGroup(
            *[FadeIn(card) for card in hand], anim
        )

    def adding_anim(self, hand: VGroup, cards: list[Card],
                    player: int) -> AnimationGroup:
        anim = []
        card_objects = [
            get_card(
                card, PLAYER_COLORS[player],
                HAND_CARD_FONT_SIZE, HAND_CARD_WIDTH, HAND_CARD_HEIGHT
            )
            for card in cards
        ]

        for card in card_objects:
            card.rotate(-PI / 2 + (PI / 2) * player)
            if player == 0:
                if len(hand) % 6:
                    card.next_to(hand[-1], DOWN, buff=HAND_CARD_BUFF)
                else:
                    card.next_to(hand[0], LEFT, buff=HAND_CARD_BUFF)
                anim.append(FadeIn(card, shift=0.2 * UP))
            elif player == 1:
                if len(hand) % 6:
                    card.next_to(hand[-1], RIGHT, buff=HAND_CARD_BUFF)
                else:
                    card.next_to(hand[0], DOWN, buff=HAND_CARD_BUFF)
                anim.append(FadeIn(card, shift=0.2 * LEFT))
            else:  # player == 2
                if len(hand) % 6:
                    card.next_to(hand[-1], DOWN, buff=HAND_CARD_BUFF)
                else:
                    card.next_to(hand[0], RIGHT, buff=HAND_CARD_BUFF)
                anim.append(FadeIn(card, shift=0.2 * UP))

            hand.add(card)

        if player == 0:
            anim.append(hand.animate.arrange_in_grid(
                6, 3, buff=HAND_CARD_BUFF, flow_order='dl').move_to(
                    3 * LEFT, aligned_edge=RIGHT
            ))
        elif player == 1:
            anim.append(hand.animate.arrange_in_grid(
                3, 6, buff=HAND_CARD_BUFF, flow_order='rd').move_to(
                    2 * DOWN, aligned_edge=UP
            ))
        else:  # player == 2
            anim.append(hand.animate.arrange_in_grid(
                6, 3, buff=HAND_CARD_BUFF, flow_order='dr').move_to(
                    3 * RIGHT, aligned_edge=LEFT
            ))

        return AnimationGroup(*anim)

    def question_anim(self, message: str,
                      center_card: VGroup) -> tuple[VGroup, AnimationGroup]:
        before, after = message.split('|c|', 1)
        card_label = VGroup(center_card[0], center_card[1])
        question = VGroup(
            Tex(before, color=QUESTION_COLOR, font_size=QUESTION_FONT_SIZE),
            card_label.copy(),
            Tex(after, color=QUESTION_COLOR, font_size=QUESTION_FONT_SIZE)
        ).arrange(RIGHT, buff=0.2).shift(3 * UP)

        self.add(card_label.copy())
        return question, AnimationGroup(
            AnimationGroup(
                card_label.animate.next_to(question[0], RIGHT, buff=0.2),
                Write(question[0]),
                lag_ratio=0.2
            ),
            Write(question[-1]),
            lag_ratio=0.7
        )

    def answer_anim(self, answer: bool,
                    question: VGroup) -> tuple[VMobject, AnimationGroup]:
        check = MathTex(r'\checkmark', color=GREEN).next_to(
            question, RIGHT, buff=0.2)
        cross = MathTex(r'\times', color=RED).next_to(
            question, RIGHT, buff=0.2)

        if answer:
            return check, AnimationGroup(Write(check))
        return cross, AnimationGroup(Write(cross))

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
            deck.stack[-1], CENTER_CARD_COLOR,
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
            self.hand_anim(player_hands[0], 0),
            self.hand_anim(player_hands[1], 1),
            self.hand_anim(player_hands[2], 2)
        )

        # game section
        self.next_section('Game', skip_animations=False)

        # check special cards

        new_suit = 0
        while all((len(hand) > 0 for hand in players)):
            last_card = deck.stack[-1]

            # check special cards
            question, anim = self.question_anim(
                'Je |c| speciální karta?', last_card
            )
            self.play(anim)
            special = (
                last_card.rank in (Rank.QUEEN, Rank.SEVEN, Rank.ACE)
                or (last_card.rank == Rank.KING and
                    last_card.suit == Suit.SPADES)
            )

            answer, anim = self.answer_anim(special, question)
            self.play(anim)

            # make a copy of last card and change suit to new suit if queen
            # was played
            if last_card.rank == Rank.QUEEN:
                last_card = last_card.copy()
                last_card.suit = Suit(new_suit)

            card_index, penalty = card_to_play(players[cur_player], last_card)

            # take cards
            if penalty:
                cards_to_add = [deck.pop() for _ in range(penalty)]
                players[cur_player] += cards_to_add
                self.play(
                    *self.adding_anim(players[cur_player],
                                      cards_to_add, cur_player)
                )

        self.pause(2)

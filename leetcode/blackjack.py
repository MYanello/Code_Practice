from icecream import ic
import random

class Deck:
    def __init__(self):
        self.deck = [i for i in range(1, 53)] # full deck
        self.values = [i for i in range(1,15)] # possible value of cards in blackjack
        self.deck_map = {card_num: self.card_value(card_num) for card_num in self.deck} # dict of card num and its value
    def card_value(self, card_num: int) -> int:
        return self.values[(card_num - 1) % 13]
    def face_cards(self, card_num: int) -> str:
        match card_num:
            case 11:
                return 'jack'
            case 12:
                return 'queen'
            case 13:
                return 'king'
            case 14:
                return 'ace'
            case _:
                return 'not a face'
    def give_card(self):
        to_deal = random.choice(list(self.deck_map.items()))
        self.deck_map.pop(to_deal[0])
        #ic(to_deal)
        return to_deal
    def show_deck(self):
        ic(self.deck_map)

class Hand:
    def __init__(self):
        self.hand = {}
        self.score = 0
    def get_card(self, deck):
        new_card = deck.give_card()
        #ic(new_card)
        self.hand[new_card[0]] = new_card[1]
    def calc_score(self):
        for value in self.hand.values():
            #ic(value)
            self.score += value
        return self.score


def deal_card(hand, deck, count):
    for _ in range(count):
        hand.get_card(deck) 

def play(hand, deck):
    rounds = 0
    while hand.score < 16:
        ic(rounds)
        rounds += 1
        hand.get_card(deck)
        hand.calc_score()
        ic(hand.score)
        if hand.score > 21:
            ic("Bust")
            ic(hand.hand)
            return
    ic(hand.hand)

def main():
    play_deck = Deck()
    my_hand = Hand()
    deal_card(my_hand, play_deck, 2)
    play(my_hand, play_deck)
    #my_hand = play(my_hand, play_deck)
    #ic(my_hand.score)

if __name__ == '__main__':
    main()
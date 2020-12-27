from typing import Dict, List

import pprint


def parse(filename: str) -> Dict[int, List[int]]:

    with open(filename, 'r') as f:
        content = f.read()
        raw_content_for_player_1, raw_content_for_player_2 = content.split('\n\n')

        deck_of_player_1 = [int(card) for card in raw_content_for_player_1.split('\n')[1:]]
        deck_of_player_2 = [int(card) for card in raw_content_for_player_2.split('\n')[1:]]

        return {
            0: deck_of_player_1,
            1: deck_of_player_2
        }


def score(hands: Dict[int, List[int]]) -> int:
    score = {}
    for hand in hands:
        player_score = 0
        cards = hands[hand].copy()
        cards.reverse()
        for i, card_value in enumerate(cards, start=1):
            player_score += i * card_value
        score[hand] = player_score
    return score


def combat(filename: str) -> Dict[int, int]:

    def finished(hands: Dict[int, List[int]]) -> bool:
        return len(hands[0]) == 0 or len(hands[1]) == 0    

    hands = parse(filename)

    while not finished(hands):

        card_by_player_1 = hands[0].pop(0)
        card_by_player_2 = hands[1].pop(0)

        if card_by_player_1 > card_by_player_2:
            hands[0] += [card_by_player_1, card_by_player_2]
        elif card_by_player_2 > card_by_player_1:
            hands[1] += [card_by_player_2, card_by_player_1]

    return hands


def recursive_combat(filename: str) -> Dict[int, int]:

    def finished(hands, previous_rounds):
        return len(hands[0]) == 0 or len(hands[1]) == 0

    def game(hands):

        previous_rounds = set()

        while not finished(hands, previous_rounds):

            hashes = score(hands)
            hashes = (hashes[0], hashes[1])
            if (hashes) in previous_rounds:
                hands[0] = [1]
                hands[1] = [0]
                return hands

            card_by_player_1 = hands[0].pop(0)
            card_by_player_2 = hands[1].pop(0)

            if card_by_player_1 <= len(hands[0]) and card_by_player_2 <= len(hands[1]):
                copied_hands = {
                    0: hands[0][:card_by_player_1].copy(),
                    1: hands[1][:card_by_player_2].copy()
                }
                score_of_subgame = score(game(copied_hands))
                
                if score_of_subgame[0] > score_of_subgame[1]:
                    hands[0] += [card_by_player_1, card_by_player_2]
                else:
                    hands[1] += [card_by_player_2, card_by_player_1]
            else:
                if card_by_player_1 > card_by_player_2:
                    hands[0] += [card_by_player_1, card_by_player_2]
                elif card_by_player_2 > card_by_player_1:
                    hands[1] += [card_by_player_2, card_by_player_1]

            previous_rounds.add(hashes)

        return hands

    hands = parse(filename)
    return game(hands)


print(score(combat('22.in')))
print(score(recursive_combat('22.in')))
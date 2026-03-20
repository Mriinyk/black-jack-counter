from valueconverter import value_converter as converter


class GetFirstCards:
    def __init__(self, first_cards: list) -> None:
        self.first_cards = first_cards

    def calculate_sum(self) -> int:
        converted_cards = converter(self.first_cards)
        first_cards_sum = 0
        for card in converted_cards:
            first_cards_sum += card
            if first_cards_sum > 21 and card == 11:
                first_cards_sum -= 10

        return first_cards_sum

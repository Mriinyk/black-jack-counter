#Клас, який приймає список з додатковими картами, конвертує їх в int та перевіряє на тузи. Повертає нову суму карт.
from app.logic.valueconverter import value_converter as converter


class GetExtraCard:
    def __init__(self, extra_cards: list, sum_of_cards: int) -> None:
        self.extra_cards = extra_cards
        self.sum_of_cards = sum_of_cards

    def calculate_new_sum(self) -> int:
        converted_cards = converter(self.extra_cards)
        for card in converted_cards:
            self.sum_of_cards += card
            if self.sum_of_cards > 21 and card == 11:
                self.sum_of_cards -= 10
                
        return self.sum_of_cards
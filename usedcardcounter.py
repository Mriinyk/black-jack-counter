#Контроль карт, які вже були використані в грі
class UsedTracker:
    def __init__(self, num_decks: int) -> None:
        self.used_cards = {
            "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
            "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0, "A": 0
        }

        self.num_decks = num_decks
        self.total_cards = num_decks * 52

    def update(self, *cards) -> dict:
        for card in cards:
            card_upper = str(card).upper()
            if card_upper in self.used_cards:
                self.used_cards[card_upper] += 1
        return self.used_cards

    @property
    def remaining_cards(self) -> int:
        used_cards_number = sum(self.used_cards.values())
        remainder = self.total_cards - used_cards_number
        return remainder

#Розрахунок відсотків випадання наступної карти

    @property
    def percentage_of_cards(self) -> dict:
        self.cards_dict = {
            "2": 4 * self.num_decks, "3": 4 * self.num_decks, "4": 4 * self.num_decks,
            "5": 4 * self.num_decks, "6": 4 * self.num_decks, "7": 4 * self.num_decks,
            "8": 4 * self.num_decks, "9": 4 * self.num_decks, "10": 4 * self.num_decks,
            "J": 4 * self.num_decks, "Q": 4 * self.num_decks, "K": 4 * self.num_decks,
            "A": 4 * self.num_decks
        }

        for key in self.cards_dict.keys():
            for key2 in self.used_cards.keys():
                if key == key2:
                    self.cards_dict[key] -= self.used_cards[key2]

        percentage_of_cards_dict = {}
        for key, value in self.cards_dict.items():
            try:
                percent_value = max(0, int(round((value / self.remaining_cards) * 100)))
                percentage_of_cards_dict[key] = f"{percent_value}%"
            except ZeroDivisionError:
                return "Карти закінчилися"

        return percentage_of_cards_dict

#Контроль карт, які вже були використані в грі
class UsedTracker:
    def __init__(self, num_decks: int) -> None:
        self.used_cards = {
            "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
            "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0, "A": 0
        }
        self.total_cards = num_decks * 52

    def update(self, *cards):
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
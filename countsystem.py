#Система розрахунку карт
class CountSystem:
    def __init__(self) -> None:
        self.wong_halves_values = {
            "2": 0.5,
            "3": 1.0,
            "4": 1.0,
            "5": 1.5,
            "6": 1.0,
            "7": 0.5,
            "8": 0.0,
            "9": -0.5,
            "10": -1.0,
            "J": -1.0,   # Валет (J)
            "Q": -1.0,   # Дама (Q)
            "K": -1.0,   # Король (K)
            "A": -1.0    # Туз (A)
        }

        self.current_score = 0.0

    def count_current_score(self, *cards) -> float:
        for card in cards:
            card_key = str(card).upper()
            if card_key in self.wong_halves_values:
                self.current_score += self.wong_halves_values[card_key]
        return self.current_score

    def true_score(self, remain_cards: int) -> float:
        actual_score = (self.current_score * 52) / remain_cards
        return round(actual_score, 2)
from usedcardcounter import remaining_cards

#Словник зі значеннями карт для розрахунків
def count_system(*cards):
    wong_halves_values = {
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
    for card in wong_halves_values:
        cards_upper = card.upper()
        current_score = 0
        if cards_upper in wong_halves_values:
            current_score += wong_halves_values[cards_upper]
        return current_score
    
#def actual_score(current_score, remaining_cards):
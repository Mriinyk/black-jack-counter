#Контроль карт, які вже були використані в грі
def used_cards_counter(*cards):
    used_cards = {
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "J": 0,   # Валет (J)
    "Q": 0,   # Дама (Q)
    "K": 0,   # Король (K)
    "A": 0    # Туз (A)
}
    for card in cards:
        cards_upper = card.upper()
        if cards_upper in used_cards:
            used_cards[cards_upper] += 1
    return used_cards

def remaining_cards(used_cards_dict) -> int:
    total_cards = 208
    used_cards_number = 0
    for values in used_cards_dict.values():
        used_cards_number += values
    remainder = total_cards - used_cards_number
    return remainder

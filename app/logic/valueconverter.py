#Мапа карт
card_map = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}

# Буде конвертувати змінні в int
def value_converter(cards) -> list[int]:
    cards_list = []
    for card in cards:
        cards_upper = card.upper()
        if cards_upper in card_map:
            cards_list.append(card_map[cards_upper])
        elif cards_upper.isdigit():
            cards_list.append(int(cards_upper))
    return cards_list

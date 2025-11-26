# Вхідні змінні
first_card_croupier = input("Введіть карту круп'є - ")
your_card_1, your_card_2 = input("Введіть свої карти через пробіл - ").split()

#Мапа карт
card_map = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}

#Контроль карт, які вже були використані в грі
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

def used_cards_counter(*cards):
    for card in cards:
        cards_upper = card.upper()
        if cards_upper in used_cards:
            used_cards[cards_upper] += 1
    return None
used_cards_counter(first_card_croupier, your_card_1, your_card_2)
print("Список карт, які були використані", used_cards)

# Буде конвертувати змінні в int
def value_converter(*cards) -> list[int]:
    cards_list = []
    for card in cards:
        cards_upper = card.upper()
        if cards_upper in card_map:
            cards_list.append(card_map[cards_upper])
        elif cards_upper.isdigit():
            cards_list.append(int(cards_upper))
    return cards_list

all_cards_list = value_converter(first_card_croupier, your_card_1, your_card_2)
first_card_croupier, your_card_1, your_card_2 = all_cards_list

print("first_card_croupier: - ", first_card_croupier)
print("your_card_1: - ", your_card_1)
print("your_card_2: - ", your_card_2)

#Розрахунок власних карт з урахуванням "А" 1, або 11
def sum_of_own_cards(your_card_1: int, your_card_2: int) -> int:
    if your_card_1 + your_card_2 > 21 and your_card_1 == 11:
        your_card_1 = 1
    if your_card_1 + your_card_2 > 21 and your_card_2 == 11:
        your_card_2 = 1
    return your_card_1 + your_card_2

own_cards_sum = sum_of_own_cards(your_card_1, your_card_2)
print(f"sum of own cards: - {own_cards_sum}")


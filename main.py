from usedcardcounter import used_cards_counter as used_cards
from usedcardcounter import remaining_cards
from countsystem import count_system

# Вхідні змінні
first_card_croupier = input("Введіть карту круп'є - ")
your_card_1, your_card_2 = input("Введіть свої карти через пробіл - ").split()

#Мапа карт
card_map = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}

#Контроль карт, які вже були використані в грі
used_cards_state = used_cards(first_card_croupier, your_card_1, your_card_2)
print("Список карт які були використані: ", used_cards_state)
print("Кількість карт, які залишилися: ", remaining_cards(used_cards_state))

#Розрахунок карт


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
    current_sum = your_card_1 + your_card_2
    if current_sum > 21 and your_card_1 == 11:
        current_sum -= 10 # 22 -> 12
    if current_sum > 21 and your_card_2 == 11:
        current_sum -= 10 # 22 -> 12
    return current_sum

own_cards_sum = sum_of_own_cards(your_card_1, your_card_2)
print(f"sum of own cards: - {own_cards_sum}")


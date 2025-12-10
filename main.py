from usedcardcounter import used_cards_counter as used_cards, remaining_cards
from countsystem import count_system, actual_score


#Значення карт суперників, якщо їх нема
rival_1_card1, rival_1_card2 = None, None
rival_2_card1, rival_2_card2 = None, None

# Вхідні змінні
first_card_croupier = input("Введіть карту круп'є - ")
your_card_1, your_card_2 = input("Введіть свої карти через пробіл - ").split()
play_with_rivals = str(input("Ви граєте з суперниками ? - ")).lower().strip()

if play_with_rivals == "так":
    print("="*12,"Вхідні дані суперників","="*12)
    rival_1_card1, rival_1_card2 = input("Введіть карти свого першого суперника через пробіл - ").split()
    rival_2_card1, rival_2_card2 = input("Введіть карти свого другого суперника через пробіл - ").split()

#Мапа карт
card_map = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}

#Фільтрація карт, включаючи можливі None
all_cards = [
    first_card_croupier, your_card_1, your_card_2, 
    rival_1_card1, rival_1_card2, rival_2_card1, rival_2_card2
]
cards_to_count = [card for card in all_cards if card is not None]

#Контроль карт, які вже були використані в грі
print("="*12,"Дані гри","="*12)
used_cards_state = used_cards(*cards_to_count)
print("Список карт які були використані: ", used_cards_state)
remain_cards = remaining_cards(used_cards_state)
print("Кількість карт, які залишилися: ", remain_cards)

#Розрахунок карт
current_score = count_system(*cards_to_count)
true_score = actual_score(current_score, remain_cards)
print("Справжній рахунок: ", true_score)

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

all_cards_list = value_converter(*cards_to_count)
first_card_croupier, your_card_1, your_card_2 = all_cards_list[:3]

if len(all_cards_list) > 3:
    rival_1_card1, rival_1_card2, rival_2_card1, rival_2_card2 = all_cards_list[3:7]

print("="*12,"Значення кожної карти","="*12)
print("Карта круп'є: - ", first_card_croupier)
print("Ваша перша карта: - ", your_card_1)
print("Ваша друга карта: - ", your_card_2)
if rival_1_card1 != None:
    print("Перший суперник, карта 1: - ", rival_1_card1)
    print("Перший суперник, карта 2: - ", rival_1_card2)
    print("Другий суперник, карта 1: - ", rival_2_card1)
    print("Другий суперник, карта 2: - ", rival_2_card2)


#Розрахунок власних карт з урахуванням "А" 1, або 11
def sum_of_own_cards(card_1: int, card_2: int) -> int:
    current_sum = card_1 + card_2
    if current_sum > 21 and card_1 == 11:
        current_sum -= 10 # 22 -> 12
    if current_sum > 21 and card_2 == 11:
        current_sum -= 10 # 22 -> 12
    return current_sum

own_cards_sum = sum_of_own_cards(your_card_1, your_card_2)
rival_1_cards_sum = sum_of_own_cards(rival_1_card1, rival_1_card2) if rival_1_card1 is not None else "Немає гравця"
rival_2_cards_sum = sum_of_own_cards(rival_2_card1, rival_2_card2) if rival_2_card1 is not None else "Немає гравця"

print("="*12,"Суми карт","="*12)
print(f"Сума ваших карт: - {own_cards_sum}")
if rival_1_card1 != None:
    print(f"Сума карт першого суперника: - {rival_1_cards_sum}")
    print(f"Сума карт другого суперника: - {rival_2_cards_sum}")


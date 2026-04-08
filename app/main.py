import os
import colorama
from colorama import Fore
from app.logic.getfirstcards import GetFirstCards
from app.logic.getextracard import GetExtraCard
from app.logic.usedcardcounter import UsedTracker
from app.logic.countsystem import CountSystem
from prettytable import PrettyTable, TableStyle


#Налаштування кольору інтерфейсу
colorama.init()
print(Fore.GREEN, end="")

#Вхідні дані колод
num_decks = int(input("Введіть кількість колод - "))

#Об'єкти статистики ПОЗА циклом
tracker = UsedTracker(num_decks)
score = CountSystem()

#Цикл гри
while True:

    #Об'єкт таблиці(інтерфейсу) та налаштування вікон
    table = PrettyTable()
    table.set_style(TableStyle.DOUBLE_BORDER)
    sums_table = PrettyTable()
    sums_table.set_style(TableStyle.DOUBLE_BORDER)

    #Значення карт суперників, якщо їх нема
    rival_1_cards = []
    rival_2_cards = []

    # Вхідні змінні
    play_with_rivals = str(input("Ви граєте з суперниками ? (y/n) - ")).lower().strip()
    your_cards = input("Введіть свої карти через пробіл - ").split()
    your_first_cards = GetFirstCards(your_cards)

    if play_with_rivals == "y":
        print("="*12,"Вхідні дані суперників","="*12)
        rival_1_cards = input("Введіть карти свого першого суперника через пробіл - ").split()
        rival_1_first_cards = GetFirstCards(rival_1_cards)
        rival_2_cards = input("Введіть карти свого другого суперника через пробіл - ").split()
        rival_2_first_cards = GetFirstCards(rival_2_cards)

    card_of_croupier = input("Введіть карту круп'є - ").split()
    first_card_croupier = GetFirstCards(card_of_croupier)
    croupier_cards_sum = first_card_croupier.calculate_sum()

    #Список усіх перших карт
    cards_to_count = []
    cards_to_count.extend(your_cards)
    cards_to_count.extend(card_of_croupier)
    if rival_1_cards:
        cards_to_count.extend(rival_1_cards)
    if rival_2_cards:
        cards_to_count.extend(rival_2_cards)

    #Контроль карт, які вже були використані в грі

    used_cards_list_for_print = tracker.update(*cards_to_count)

    #Розрахунок карт
    score.count_current_score(*cards_to_count)
    true_count = score.true_score(tracker.remaining_cards)


    #Таблиця виводу даних
    table.title = "Дані гри"
    table.field_names = [
        "Список карт які були використані",
        "Кількість карт, які залишилися",
        "Відсотки випадання наступних карт"
    ]

    table.add_row(
        [
            used_cards_list_for_print,
            tracker.remaining_cards,
            tracker.percentage_of_cards
        ]
    )

    table.add_row(["", f"Справжній рахунок: {true_count}", ""])

    table.max_width = 50
    table.hrules = 1
    print(table)
    table.clear_rows()


    #Підрахунок суми карт
    own_cards_sum = your_first_cards.calculate_sum()
    if rival_1_cards:
        rival_1_cards_sum = rival_1_first_cards.calculate_sum()
    if rival_2_cards:
        rival_2_cards_sum = rival_2_first_cards.calculate_sum()


    #Таблиця для сумкарт
    sums_table.title = "Суми карт"

    headers = ["Сума ваших карт", "Cума карт круп'є"]
    rows = [own_cards_sum, croupier_cards_sum]

    if rival_1_cards:
        headers.append("Сума карт першого суперника")
        rows.append(rival_1_cards_sum)
    if rival_2_cards:
        headers.append("Сума карт другого суперника")
        rows.append(rival_2_cards_sum)

    sums_table.field_names = headers
    sums_table.add_row(rows)

    sums_table.max_width = 50
    sums_table.hrules = 1
    print(sums_table)
    sums_table.clear_rows()


    #Логіка додавання карт
    print("="*12,"Роздача додаткових карт","="*12)
    # Цикл який приймає інпути додаткових карт, рахує нову суму карт
    while True:
        own_extra_cards = input(f"Введіть ваші додаткові карту (для пропуску натисніть Enter): ").split()
        own_exra = GetExtraCard(own_extra_cards, own_cards_sum)
        own_cards_sum = own_exra.calculate_new_sum()

        if rival_1_cards:
            rival_1_extra_cards = input(f"Введіть додаткові карти Суперника 1 (для пропуску натисніть Enter): ").split()
            rival_1_extra = GetExtraCard(rival_1_extra_cards, rival_1_cards_sum)
            rival_1_cards_sum = rival_1_extra.calculate_new_sum()

        if rival_2_cards:
            rival_2_extra_cards = input(f"Введіть додаткові карти Суперника 2 (для пропуску натисніть Enter): ").split()
            rival_2_extra = GetExtraCard(rival_2_extra_cards, rival_2_cards_sum)
            rival_2_cards_sum = rival_2_extra.calculate_new_sum()

        #Вивід оновлених даних гри з урахуванням 1 чи більше гравців
        all_active_extra = []
        all_active_extra.extend(own_extra_cards)

        if rival_1_cards:
            all_active_extra.extend(rival_1_extra_cards)
        if rival_2_cards:
            all_active_extra.extend(rival_2_extra_cards)

        used_extra_cards= tracker.update(*all_active_extra)
        score.count_current_score(*all_active_extra)
        true_count = score.true_score(tracker.remaining_cards)

        #Таблиця оновлених даних
        table.title = "Оновлені дані гри"
        table.add_row(
            [
                used_extra_cards,
                tracker.remaining_cards,
                tracker.percentage_of_cards
            ]
        )

        table.add_row(["", f"Справжній рахунок: {true_count}", ""])

        table.max_width = 50
        table.hrules = 1
        print(table)
        table.clear_rows()


        #Виводить таблицю оновлених сум карт

        sums_table.title =  "Оновлені суми карт"

        rows = [own_cards_sum, croupier_cards_sum]

        if rival_1_cards:
            rows.append(rival_1_cards_sum)
        if rival_2_cards:
            rows.append(rival_2_cards_sum)

        sums_table.add_row(rows)

        sums_table.max_width = 50
        sums_table.hrules = 1
        print(sums_table)
        sums_table.clear_rows()

        stop = input("Бажаєте додати ще карти? (y/n): ").lower()
        if stop == 'n':
            break

    #Ввід додаткових карт круп'є
    croupier_extra_cards = input(f"Введіть відкриту та додаткові карти круп'є: ").split()
    croupier_cards_sum = first_card_croupier.calculate_sum()
    croupier_extra = GetExtraCard(croupier_extra_cards, croupier_cards_sum)
    croupier_cards_sum = croupier_extra.calculate_new_sum()

    #Вивід фінальної інформації
    print("="*12, "Фінальні дані гри", "="*12)

    used_croupier_cards = tracker.update(*croupier_extra_cards)
    score.count_current_score(*croupier_extra_cards)
    true_count = score.true_score(tracker.remaining_cards)

    #Вивід таблиці фінальних даних гри
    table.title = "Фінальні дані гри"

    table.add_row(
            [
                used_croupier_cards,
                tracker.remaining_cards,
                tracker.percentage_of_cards
            ]
        )

    table.add_row(["", f"Справжній рахунок: {true_count}", ""])

    table.max_width = 50
    table.hrules = 1
    print(table)
    table.clear_rows()

    #Вивід таблиці фінальних сум карт
    sums_table.title = "Фінальні суми карт"

    rows = [own_cards_sum, croupier_cards_sum]

    if rival_1_cards:
        rows.append(rival_1_cards_sum)
    if rival_2_cards:
        rows.append(rival_2_cards_sum)

    sums_table.add_row(rows)

    sums_table.max_width = 50
    sums_table.hrules = 1
    print(sums_table)
    sums_table.clear_rows()


#Перевірка на автоматичне перетасування (якщо залишилось менше 20% карт)
    if tracker.remaining_cards < (num_decks * 52 * 0.2):
        print("Увага: в колоді залишилося мало карт! Можливе перетасування.")

#Запит на продовження гри та перетасовку карт
    exit_game = input("Бажаєте почати наступний раунд? (y/n): ").lower().strip()
    shuffling_cards = input("Чи круп'є перетасовує карти? (y/n): ").lower().strip()

    if exit_game == 'n':
        break

#Обнулення статистичних даних
    if shuffling_cards == 'y' or tracker.remaining_cards <= 0:
        tracker = UsedTracker(num_decks)
        score = CountSystem()

        # Очищуємо термінал
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Карти перетасовано! Статистику обнулено.")
    else:
        # Очищуємо термінал
        os.system('cls' if os.name == 'nt' else 'clear')

        print("="*20, "ПОЧАТОК НОВОГО РАУНДУ", "="*20)

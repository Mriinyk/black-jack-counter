from getfirstcards import GetFirstCards
from getextracard import GetExtraCard
from usedcardcounter import UsedTracker
from countsystem import CountSystem

#Вхідні дані колод
num_decks = int(input("Введіть кількість колод - "))

#Об'єкти статистики ПОЗА циклом
tracker = UsedTracker(num_decks)
score = CountSystem()

#Цикл гри
while True:
    #Значення карт суперників, якщо їх нема
    rival_1_cards = []
    rival_2_cards = []

    # Вхідні змінні
    your_cards = input("Введіть свої карти через пробіл - ").split()
    your_first_cards = GetFirstCards(your_cards)
    play_with_rivals = str(input("Ви граєте з суперниками ? (y/n) - ")).lower().strip()

    if play_with_rivals == "y":
        print("="*12,"Вхідні дані суперників","="*12)
        rival_1_cards = input("Введіть карти свого першого суперника через пробіл - ").split()
        rival_1_first_cards = GetFirstCards(rival_1_cards)
        rival_2_cards = input("Введіть карти свого другого суперника через пробіл - ").split()
        rival_2_first_cards = GetFirstCards(rival_2_cards)

    card_of_croupier = input("Введіть карту круп'є - ").split()
    first_card_croupier = GetFirstCards(card_of_croupier)

    #Список усіх перших карт
    cards_to_count = []
    cards_to_count.extend(your_cards)
    cards_to_count.extend(card_of_croupier)
    if rival_1_cards:
        cards_to_count.extend(rival_1_cards)
    if rival_2_cards:
        cards_to_count.extend(rival_2_cards)

    #Контроль карт, які вже були використані в грі
    print("="*12,"Дані гри","="*12)
    print("Список карт які були використані: ", tracker.update(*cards_to_count))
    print("Кількість карт, які залишилися: ", tracker.remaining_cards)

    #Розрахунок карт
    score.count_current_score(*cards_to_count)
    print("Справжній рахунок: ", score.true_score(tracker.remaining_cards))

    #Підрахунок суми карт
    own_cards_sum = your_first_cards.calculate_sum()
    if rival_1_cards:
        rival_1_cards_sum = rival_1_first_cards.calculate_sum()
    if rival_2_cards:
        rival_2_cards_sum = rival_2_first_cards.calculate_sum()

    print("="*12,"Суми карт","="*12)
    print(f"Сума ваших карт: - {own_cards_sum}")
    if rival_1_cards:
        print(f"Сума карт першого суперника: - {rival_1_cards_sum}")
    if rival_2_cards:
        print(f"Сума карт другого суперника: - {rival_2_cards_sum}")

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
        print("="*12, "Оновлені дані гри", "="*12)
        all_active_extra = []
        all_active_extra.extend(own_extra_cards)

        if rival_1_cards:
            all_active_extra.extend(rival_1_extra_cards)
        if rival_2_cards:
            all_active_extra.extend(rival_2_extra_cards)

        used_extra_cards= tracker.update(*all_active_extra)
        score.count_current_score(*all_active_extra)

        #Виводимо результат (один блок для всіх сценаріїв)
        print("Список карт які були використані: ", used_extra_cards)
        print("Кількість карт, які залишилися: ", tracker.remaining_cards)
        print("Справжній рахунок: ", score.true_score(tracker.remaining_cards))

        #Виводить оновлені суми карт
        print("="*12, "Оновлені суми карт", "="*12)
        print(f"Ваша поточна сума: {own_cards_sum}")
        
        if rival_1_cards:
            print(f"Поточна сума Першого суперника: {rival_1_cards_sum}")
            
        if rival_2_cards:
            print(f"Поточна сума Другого суперника: {rival_2_cards_sum}")

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

    print("Список карт які були використані: ", used_croupier_cards)
    print("Кількість карт, які залишилися: ", tracker.remaining_cards)
    print("Справжній рахунок: ", score.true_score(tracker.remaining_cards))

    print("="*12, "Фінальні суми карт", "="*12)
    print(f"Фінальна сума карт круп'є: {croupier_cards_sum}")
    print(f"Ваша сума: {own_cards_sum}")
        
    if rival_1_cards:
        print(f"Сума Першого суперника: {rival_1_cards_sum}")
            
    if rival_2_cards:
        print(f"Сума Другого суперника: {rival_2_cards_sum}")

    exit_game = input("Бажаєте почати наступний раунд? (y/n): ").lower().strip()
    if exit_game == 'n':
        break
    else:
        print("="*20, "ПОЧАТОК НОВОГО РАУНДУ", "="*20)

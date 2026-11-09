# Black Jack Counter

## English

A card-counting program for Black Jack. Implements the **Wong Halves** counting system, calculates the current and "true" count (true count), tracks used cards, computes probabilities of the next cards, and sums up players' and dealer's cards.

### Features

- Card counting using the Wong Halves system (2: +0.5, 3–4–6: +1, 5: +1.5, 7: +0.5, 8: 0, 9: –0.5, 10/J/Q/K/A: –1)
- True count calculation based on the number of remaining cards
- Multiple decks support (entered by the user)
- Play with one or two opponents
- Tracking of used cards and percentages of each card rank
- Card sum calculation (aces counted as 1 or 11)
- Colored text interface (colorama, prettytable)

### Requirements

- Python 3.10+
- `colorama`
- `prettytable`

### Installation

```bash
git clone https://github.com/Mriinyk/black-jack-counter.git
cd black-jack-counter
py -m pip install colorama prettytable pytest
```

### Running

```bash
py -m app.main
```

Or from the project root:

```bash
py app/main.py
```

The program will ask for the number of decks, whether you play with opponents, the players' and dealer's cards, and then display a table with the count, remaining cards, and percentages.

### Testing

The project includes automated tests (pytest) for the counting logic:

```bash
py -m pytest tests/ -v
```

### Note on `os.system`

The original code used `os.system('cls' if os.name == 'nt' else 'clear')`, which IDE linters (Pylance) strike through because `os.system` is considered unsafe and obsolete: it spawns a system shell (command injection risk), is hard to test, and depends on the operating system. It has been replaced with a safe `clear_screen()` function that clears the screen using ANSI escape sequences (`\033[2J\033[H`).

## Українська

Програма для підрахунку карт у Black Jack. Реалізує рахунок за системою **Wong Halves**, обчислює поточний та «справжній» рахунок (true count), відстежує використані карти, вирахує ймовірності випадання наступних карт та рахує суми карт гравців і круп'є.

## Можливості

- Підрахунок карт за системою Wong Halves (2: +0.5, 3–4–6: +1, 5: +1.5, 7: +0.5, 8: 0, 9: –0.5, 10/J/Q/K/A: –1)
- Обчислення справжнього рахунка з урахуванням кількості залишкових карт
- Підтримка кількох колод (вводиться користувачем)
- Gra з одним або двома суперниками
- Відстеження використаних карт та відсотків випадання кожної картки
- Підрахунок сум карт (з урахуванням тузів як 1 або 11)
- Кольоровий текстовий інтерфейс (colorama, prettytable)

## Вимоги

- Python 3.10+
- `colorama`
- `prettytable`

## Встановлення

```bash
git clone https://github.com/Mriinyk/black-jack-counter.git
cd black-jack-counter
py -m pip install colorama prettytable pytest
```

## Запуск

```bash
py -m app.main
```

Або з кореня проєкту:

```bash
py app/main.py
```

Програма запитає кількість колод, чи граєте ви з суперниками, карти гравців та круп'є, а потім виведе таблицю з рахунком, залишком карт і відсотками.

## Тестування

У проєкті є автоматичні тести (pytest) для логіки підрахунку карт:

```bash
py -m pytest tests/ -v
```

## Структура проєкту

```
black-jack-counter/
├── app/
│   ├── main.py              # Головний файл з точкою входу (if __name__ == "__main__")
│   ├── logic/
│   │   ├── countsystem.py   # Система рахунку Wong Halves та true count
│   │   ├── getfirstcards.py # Сума перших карт
│   │   ├── getextracard.py  # Сума після додаткових карт
│   │   ├── usedcardcounter.py # Облік використаних карт і відсотків
│   │   └── valueconverter.py    # Конвертація карт у числа
│   └── ux_settings/
│       └── uxsettings.py    # Логотип та кольори інтерфейсу
├── tests/                   # Тести pytest
├── README.md
└── .gitignore
```

## Примітка про os.system

У оригінальному коді виклик `os.system('cls' if os.name == 'nt' else 'clear')` підкреслюється/перекреслюється в IDE (Pylance), бо `os.system` вважається небезпечною: вона породжує оболонку системи, створює ризик ін'єкції команд, важко тестується і залежить від ОС. У цій версії її заміщено на безпечну функцію `clear_screen()`, яка очищує екран через ANSI-ескейп-послідовності (`\033[2J\033[H`).
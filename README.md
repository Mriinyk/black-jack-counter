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

### Using the executable file (.exe)

A ready-to-use `+21.exe` file is available in the project root for **Windows**. It does not require Python or any dependencies to be installed.

**How to run:**

```bash
+21.exe
```

The program is a console application. After finishing the game, press **Enter** to close the window.

> ⚠️ The `.exe` file is built for Windows only. On Linux/macOS, run the Python source code:
> ```bash
> py app/main.py
> ```

### Using the installer (.exe)

The `Output/mysetup.exe` file is a full installer for **Windows**. It installs the program on your computer like a regular application, creating shortcuts and adding an entry to the Start menu.

**How to install:**

1. Go to the `Output` folder.
2. Run `mysetup.exe`.
3. Follow the installer instructions.

After installation, you can launch the program from the Start menu or desktop shortcut. No Python installation is required on the target computer.

> ⚠️ The installer is built for Windows only. On Linux/macOS, run the Python source code:
> ```bash
> py app/main.py
> ```

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

## Використання виконуваного файлу (.exe)

Готовий до використання файл `+21.exe` знаходиться в корені проєкту для **Windows**. Він не вимагає встановленого Python або залежностей.

**Як запустити:**

```bash
+21.exe
```

Програма є консольною. Після завершення гри натисніть **Enter**, щоб закрити вікно.

> ⚠️ Файл `.exe` створено тільки для Windows. На Linux/macOS запустіть вихідний код Python:
> ```bash
> py app/main.py
> ```

## Використання інсталятора (.exe)

Файл `Output/mysetup.exe` є повноцінним інсталятором для **Windows**. Він встановлює програму на комп'ютер як звичайний додаток, створює ярлики та додає запис у меню Пуск.

**Як встановити:**

1. Перейдіть до папки `Output`.
2. Запустіть `mysetup.exe`.
3. Дотримуйтесь інструкцій інсталятора.

Після встановлення можна запускати програму з меню Пуск або ярлика на робочому столі. Python на цільовому комп'ютері встановлювати не потрібно.

> ⚠️ Інсталятор створено тільки для Windows. На Linux/macOS запустіть вихідний код Python:
> ```bash
> py app/main.py
> ```

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
├── +21.exe                  # Готовий виконуваний файл для Windows
├── Output/
│   └── mysetup.exe          # Інсталятор для Windows (встановлює програму в систему)
├── tests/                   # Тести pytest
├── README.md
└── .gitignore
```

## Примітка про os.system

У оригінальному коді виклик `os.system('cls' if os.name == 'nt' else 'clear')` підкреслюється/перекреслюється в IDE (Pylance), бо `os.system` вважається небезпечною: вона породжує оболонку системи, створює ризик ін'єкції команд, важко тестується і залежить від ОС. У цій версії її заміщено на безпечну функцію `clear_screen()`, яка очищує екран через ANSI-ескейп-послідовності (`\033[2J\033[H`).
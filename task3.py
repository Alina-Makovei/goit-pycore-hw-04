
import sys
from pathlib import Path
from colorama import Fore, init

# Ініціалізуємо бібліотеку colorama
init(autoreset=True)


def print_directory_tree(directory, prefix=""):
    """
    Рекурсивно виводить структуру директорій та файлів.
    Директорії відображаються синім кольором, файли — зеленим.
    """

    try:
        # Отримуємо вміст поточної директорії
        # Сортуємо: спочатку директорії, потім файли
        items = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower())
        )

    except PermissionError:
        print(prefix + "Недостатньо прав для доступу до директорії.")
        return

    # Перебираємо всі елементи директорії
    for index, item in enumerate(items):

        # Перевіряємо, чи є поточний елемент останнім
        is_last = index == len(items) - 1

        # Визначаємо символ для відображення елемента
        if is_last:
            connector = "└── "
        else:
            connector = "├── "

        # Визначаємо колір залежно від типу елемента
        if item.is_dir():
            name = Fore.BLUE + item.name
        else:
            name = Fore.GREEN + item.name

        # Виводимо назву елемента
        print(prefix + connector + name)

        # Якщо елемент є директорією, заходимо в неї
        if item.is_dir():

            # Визначаємо відступ для наступного рівня вкладеності
            if is_last:
                extension = "    "
            else:
                extension = "│   "

            # Рекурсивно викликаємо функцію для вкладеної директорії
            print_directory_tree(
                item,
                prefix + extension
            )


def main():

    # Перевіряємо, чи передано шлях до директорії
    if len(sys.argv) != 2:
        print("Використання: python task3.py <шлях_до_директорії>")
        return

    # Отримуємо шлях до директорії з аргументів командного рядка
    directory = Path(sys.argv[1]).expanduser()

    # Перевіряємо, чи існує вказаний шлях
    if not directory.exists():
        print("Помилка: вказаний шлях не існує.")
        return

    # Перевіряємо, чи є вказаний шлях директорією
    if not directory.is_dir():
        print("Помилка: вказаний шлях не є директорією.")
        return

    # Виводимо назву кореневої директорії синім кольором
    print(Fore.BLUE + directory.name)

    # Виводимо структуру директорії
    print_directory_tree(directory)


# Self-check:
# python task3.py picture
# python task3.py
# python task3.py unknown_folder
# python task3.py cats.txt
# python task3.py "/Users/alinamakovei/Desktop/Projects VSC/vsc-basics/my_stydies/home_work/goit-pycore-hw-04/picture"

if __name__ == "__main__":
    main()

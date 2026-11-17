
from pathlib import Path


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except (FileNotFoundError, ValueError, UnicodeError):
        return 0, 0


# self-check

BASE_DIR = Path(__file__).parent

salary_file = BASE_DIR / "salary_file.txt"
unknown_file = BASE_DIR / "unknown.txt"
empty_file = BASE_DIR / "empty.txt"
wrong_file = BASE_DIR / "wrong.txt"

total, average = total_salary(salary_file)

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")

print("Перевірка основного файлу:", total_salary(salary_file))
print("Перевірка відсутнього файлу:", total_salary(unknown_file))
print("Перевірка порожнього файлу:", total_salary(empty_file))
print("Перевірка файлу з неправильними даними:", total_salary(wrong_file))

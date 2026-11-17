
from pathlib import Path


def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_info.append(cat)

    except FileNotFoundError:
        print(f"File not found: {path}")
    except OSError as error:
        print(f"Error reading file: {error}")

    return cats_info


# self-check

cats_file = Path(__file__).parent / "cats.txt"

cats_info = get_cats_info(cats_file)
print(cats_info)

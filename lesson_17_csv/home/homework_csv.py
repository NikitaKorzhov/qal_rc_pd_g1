import csv
from enum import unique
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content[0])
        writer.writeheader()
        writer.writerows(content)

    

to_tuple=lambda row: tuple(sorted(row.items()))
to_set = lambda data: set(map(to_tuple, data))

def main(data_1, data_2):
    """
    Чого не вистачає — основна логіка
    Задача — знайти та прибрати дублікати. Ця логіка ще не написана
    """
    s1, s2 = to_set(data_1), to_set(data_2)
    unique = s1 | s2
    total_duplicates = (len(data_1) + len(data_2)) - len(unique)
    list_unique = [dict(row) for row in unique]
    return (list_unique,total_duplicates)


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "users_1.csv"
    my_csv2 = Path(__file__).parent / "users_2.csv"
    result_csv = Path(__file__).parent / "clean_users_3.csv"
    content = read_file(my_csv)
    content2 = read_file(my_csv2)
    unique, total_duplicates = main(content, content2)
    print(f"Знайдено дублікатів: {total_duplicates}")
    print(f"Унікальних записів збережено: {len(unique)}")
    print(f"Файл: {result_csv.name}")
    write_csv(result_csv, unique)
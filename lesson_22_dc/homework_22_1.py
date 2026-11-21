"""Домашнє завдання 22, Частина 1. Функціональна практика (filter/map/reduce/lambda)."""

from functools import reduce

# ---------------------------------------------------------------------------
# Завдання 1. Охоронці воріт
# ---------------------------------------------------------------------------

passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]


def is_strong(password: str) -> bool:
    """Надійний: 8-20 символів, є цифра, є велика літера, без пробілів."""
    if not (8 <= len(password) <= 20):
        return False
    if " " in password:
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    if not any(ch.isupper() for ch in password):
        return False
    return True


def task1() -> None:
    print("=== Завдання 1. Охоронці воріт ===\n")

    strong = list(filter(lambda p: is_strong(p), passwords))
    weak = list(filter(lambda p: not is_strong(p), passwords))

    for p in strong:
        print(f"✅ {p} — надійний")
    for p in weak:
        print(f"❌ {p} — відхилено")
    print()


# ---------------------------------------------------------------------------
# Завдання 2. Перепис козацького реєстру
# ---------------------------------------------------------------------------

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]


def _title_case(text: str) -> str:
    """Кожне слово — з великої літери, решта рядка лишається як є."""
    return " ".join(word.capitalize() for word in text.strip().split())


def parse_registry_line(line: str) -> dict:
    name_part, rank_part, warriors_part = line.split("|")
    return {
        "name": _title_case(name_part),
        "rank": _title_case(rank_part),
        "warriors": int(warriors_part.strip()),
    }


def task2() -> None:
    print("=== Завдання 2. Перепис козацького реєстру ===\n")

    registry = list(map(parse_registry_line, raw_registry))
    active = list(filter(lambda r: r["warriors"] > 0, registry))
    total_warriors = reduce(lambda acc, r: acc + r["warriors"], active, 0)
    sorted_registry = sorted(active, key=lambda r: r["warriors"], reverse=True)

    print(f"Козацький реєстр ({len(sorted_registry)} записи):")
    print("─" * 50)
    print(f"{'№':>2}  {'Імʼя':<20}  {'Посада':<12}  {'Воїни':>6}")
    print("─" * 50)
    for i, r in enumerate(sorted_registry, start=1):
        print(f"{i:>2}  {r['name']:<20}  {r['rank']:<12}  {r['warriors']:>6}")
    print("─" * 50)
    print(f"Разом воїнів: {total_warriors}\n")


# ---------------------------------------------------------------------------
# Завдання 3. Пошук козацьких шифрів
# ---------------------------------------------------------------------------

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def task3() -> None:
    print("=== Завдання 3. Пошук козацьких шифрів ===\n")

    ciphers = list(filter(lambda m: is_palindrome(m), messages))
    transformed = list(
        map(lambda m: f"🔐 {m} → {m.replace(' ', '').lower()[::-1]}", ciphers)
    )

    for line in transformed:
        print(line)
    print()


if __name__ == "__main__":
    task1()
    task2()
    task3()

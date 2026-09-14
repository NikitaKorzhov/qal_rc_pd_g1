import json
import os
import pathlib
from typing import List, Dict, Any, Optional, Union

project_root = pathlib.Path(__file__).parent.parent
# Створюємо шлях до директорії для роботи з файлами
files_dir = project_root / "lesson_16_json" / "data"
# Створюємо директорію, якщо її ще не існує у папці уроку 16
files_dir.mkdir(parents=True, exist_ok=True)

# ==========================================
# ЗАВДАННЯ 1: Перші кроки — серіалізація вручну
# ==========================================

folklore_unit = {
    "title": "Ой у лузі червона калина",
    "genre": "пісня",
    "region": "Полтавщина",
    "narrator": "Ганна Остапенко",
    "year": 1932,
    "content": "Ой у лузі червона калина похилилася...",
    "tags": ["веснянка", "патріотична", "народна"],
    "verified": True
}

# 1. Перетворення на JSON-рядок
json_string = json.dumps(folklore_unit)
print("1. JSON рядок:", json_string)
print("   Тип:", type(json_string))

# 2. Виведення з indent=4 та ensure_ascii=False
formatted_json_string = json.dumps(folklore_unit, indent=4, ensure_ascii=False)
print("\n2. Форматований JSON:\n", formatted_json_string)

# 3. Відновлення об'єкта через json.loads()
restored_dict = json.loads(json_string)
print("\n3. Відновлений тип:", type(restored_dict))
print(f"   Назва: {restored_dict['title']}, Регіон: {restored_dict['region']}")
print("-" * 50)


# ==========================================
# ЗАВДАННЯ 2: Архів експедиції — запис і читання файлу
# ==========================================

archive_list = [
    {
        "title": "Ой у лузі червона калина",
        "genre": "пісня",
        "region": "Полтавщина",
        "narrator": "Ганна Остапенко",
        "year": 1932,
        "content": "Текст пісні...",
        "tags": ["пісня"],
        "verified": True
    },
    {
        "title": "Про лисицю та журавля",
        "genre": "казка",
        "region": "Поділля",
        "narrator": "Петро Сливка",
        "year": 1975,
        "content": "Жили-були лисиця та журавель...",
        "tags": ["казка", "тварини"],
        "verified": True
    },
    {
        "title": "Чого не можна свистіти в хаті",
        "genre": "прислів'я",
        "region": "Волинь",
        "narrator": "Марія Крук",
        "year": 1988,
        "content": "Грошей не буде...",
        "tags": ["забобони"],
        "verified": False
    },
    {
        "title": "Легенда про Білу Криницю",
        "genre": "легенда",
        "region": "Карпати",
        "narrator": "Іван Довбуш",
        "year": 1950,
        "content": "У давні часи...",
        "tags": ["гори", "вода"],
        "verified": True
    },
    {
        "title": "Щедрик-ведрик",
        "genre": "пісня",
        "region": "Чернігівщина",
        "narrator": "Ольга Шевченко",
        "year": 1965,
        "content": "Щедрик, щедрик, щедрівочка...",
        "tags": ["календарні", "зимові"],
        "verified": True
    }
]

filename_archive = "folklore_archive.json"
file_path_archive = files_dir / filename_archive
# 1. Збереження у файл
with open(file_path_archive, "w", encoding="utf-8") as f:
    json.dump(archive_list, f, indent=4, ensure_ascii=False)

# 2. Читання назад
with open(file_path_archive, "r", encoding="utf-8") as f:
    loaded_archive = json.load(f)

print(f"Завантажено записів: {len(loaded_archive)}")

# 3. Виведення заголовків
for idx, item in enumerate(loaded_archive, 1):
    print(f'{idx}. "{item["title"]}" ({item["genre"]}, {item["region"]})')
print("-" * 50)


# ==========================================
# ЗАВДАННЯ 3: Клас FolkloreRecord
# ==========================================

class FolkloreRecord:
    def __init__(self, title: str, genre: str, region: str, narrator: str, year: int, content: str, tags: List[str], verified: bool):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FolkloreRecord':
        return cls(
            title=data["title"],
            genre=data["genre"],
            region=data["region"],
            narrator=data["narrator"],
            year=data["year"],
            content=data["content"],
            tags=data["tags"],
            verified=data["verified"]
        )

    def __str__(self) -> str:
        return f'[{self.genre}] "{self.title}" — {self.region}, {self.year} (оповідач: {self.narrator})'

# Перевірка повного циклу Завдання 3
records_objects = [
    FolkloreRecord("Дума про казака Голоту", "пісня", "Слобожанщина", "Опанас Сластьон", 1905, "Ой тим же то казак Голота...", ["історичні"], True),
    FolkloreRecord("Про змія та коваля", "казка", "Полтавщина", "Семен Гончар", 1948, "Жив-був коваль...", ["казка", "героїчні"], True),
    FolkloreRecord("Про іншу сторону", "легенда", "Поділля", "Ярина Бойко", 1962, "Старі люди кажуть...", ["містика"], False)
]

records_filename = "records.json"
records_file_path = files_dir / records_filename
with open(records_file_path, "w", encoding="utf-8") as f:
    json.dump([r.to_dict() for r in records_objects], f, indent=4, ensure_ascii=False)

with open(records_file_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)
    restored_records = [FolkloreRecord.from_dict(d) for d in raw_data]

for rec in restored_records:
    print(rec)
print("-" * 50)


# ==========================================
# ЗАВДАННЯ 4: Клас FieldExpedition
# ==========================================

class FieldExpedition:
    def __init__(self, expedition_id: str, researcher: str, location: str, date: str, records: Optional[List[FolkloreRecord]] = None):
        self.expedition_id = expedition_id
        self.researcher = researcher
        self.location = location
        self.date = date
        self.records = records if records is not None else []

    def add_record(self, record: FolkloreRecord) -> Optional[str]:
        for r in self.records:
            if r.title.lower() == record.title.lower():
                return f"Запис '{record.title}' вже є в експедиції"
        self.records.append(record)
        return None

    def remove_record(self, title: str) -> str:
        for r in self.records:
            if r.title.lower() == title.lower():
                self.records.remove(r)
                return f"Запис '{title}' успішно видалено"
        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre: str) -> List[FolkloreRecord]:
        return [r for r in self.records if r.genre.lower() == genre.lower()]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": [r.to_dict() for r in self.records]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FieldExpedition':
        recs = [FolkloreRecord.from_dict(rd) for rd in data.get("records", [])]
        return cls(
            expedition_id=data["expedition_id"],
            researcher=data["researcher"],
            location=data["location"],
            date=data["date"],
            records=recs
        )

    def save(self, filepath: Union[pathlib.Path, str]) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    @classmethod
    def load(cls, filepath: Union[pathlib.Path, str]) -> Optional['FieldExpedition']:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return cls.from_dict(data)
        except FileNotFoundError:
            print(f"Попередження: Файл '{filepath}' не знайдено.")
            return None
        except json.JSONDecodeError:
            print(f"Попередження: Помилка декодування JSON у файлі '{filepath}'.")
            return None

# Перевірка Завдання 4
exp = FieldExpedition("EXP-01", "Дмитро Яворницький", "село Кринички", "2026-06-15")
exp.add_record(FolkloreRecord("Ой на горі жнутьці", "пісня", "Подніпров'я", "Орися", 1920, "Жнутьці...", ["пісня"], True))
exp.add_record(FolkloreRecord("Про золотий кубок", "казка", "Подніпров'я", "Гриць", 1920, "Давним-давно...", ["казка"], True))
exp.add_record(FolkloreRecord("Про походження назви села", "легенда", "Подніпров'я", "Дід Максим", 1920, "Колись тут...", ["легенда"], False))
exp.add_record(FolkloreRecord("Без труда нема плода", "прислів'я", "Подніпров'я", "Баба Гапка", 1920, "Праця...", ["мудрість"], True))

exp_file = "expedition_01.json"
file_path_exp = files_dir / exp_file
exp.save(file_path_exp)

loaded_exp = FieldExpedition.load(file_path_exp)
if loaded_exp:
    songs = loaded_exp.find_by_genre("пісня")
    print(f"Знайдено пісень в експедиції: {len(songs)}")
    print(loaded_exp.remove_record("Про золотий кубок"))
    loaded_exp.save(file_path_exp)
print("-" * 50)


# ==========================================
# ЗАВДАННЯ 5: Центральний архів — колекція
# ==========================================

def merge_archives(filepaths: List[Union[pathlib.Path, str]]) -> List[FolkloreRecord]:
    all_records = []
    for path in filepaths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "records" in data:
                    for rd in data["records"]:
                        all_records.append(FolkloreRecord.from_dict(rd))
                elif isinstance(data, list):
                    for rd in data:
                        all_records.append(FolkloreRecord.from_dict(rd))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Попередження: Пропущено файл '{path}' через помилку: {e}")
    return all_records

def filter_records(records: List[FolkloreRecord], genre: Optional[str] = None, region: Optional[str] = None, verified: Optional[bool] = None) -> List[FolkloreRecord]:
    result = records
    if genre is not None:
        result = [r for r in result if r.genre.lower() == genre.lower()]
    if region is not None:
        result = [r for r in result if r.region.lower() == region.lower()]
    if verified is not None:
        result = [r for r in result if r.verified == verified]
    return result

def export_summary(records: List[FolkloreRecord], filepath: Union[pathlib.Path, str]) -> None:
    summary_data = [
        {
            "title": r.title,
            "genre": r.genre,
            "region": r.region,
            "verified": r.verified
        }
        for r in records
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=4, ensure_ascii=False)

# Перевірка Завдання 5
file_list = [file_path_exp, file_path_archive]
merged = merge_archives(file_list)
filtered = filter_records(merged, verified=True)
export_summary(filtered, files_dir / "archive_summary.json")
print(f"Експортовано зведених записів до архіву: {len(filtered)}")
print("-" * 50)


# ==========================================
# БОНУС: Пошук дублікатів за назвою
# ==========================================

def find_duplicates(filepaths: List[Union[pathlib.Path, str]]) -> Dict[str, List[str]]:
    records = merge_archives(filepaths)
    title_data: Dict[str, Dict[str, Any]] = {}

    for r in records:
        display_title = r.title.strip()
        norm_title = display_title.lower()

        if norm_title not in title_data:
            title_data[norm_title] = {
                "display_title": display_title,
                "regions": set()
            }
        title_data[norm_title]["regions"].add(r.region)

    duplicates = {}
    for norm_title, data in title_data.items():
        matching_count = sum(1 for r in records if r.title.strip().lower() == norm_title)
        if matching_count > 1:
            duplicates[data["display_title"]] = list(data["regions"])

    return duplicates

# Створюємо дублікат із назвою, яка вже є у файлі archive_list / file_path_archive
dup_test_exp = FieldExpedition("EXP-02", "М. Лисенко", "село Великі Сорочинці", "2026-07-01")
dup_test_exp.add_record(FolkloreRecord("Ой у лузі червона калина", "пісня", "Харківщина", "Хтось", 1935, "Текст...", ["пісня"], True))
dup_test_exp_path = files_dir / "expedition_02.json"
dup_test_exp.save(dup_test_exp_path)

# Перевіряємо дублікати між файлом архіву та новою експедицією, де перетинається назва
print("Результат пошуку дублікатів:", find_duplicates([file_path_archive, dup_test_exp_path]))
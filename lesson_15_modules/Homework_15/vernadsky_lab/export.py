import csv
import pathlib
from .observations import _journal
def to_csv(file_name):
    project_folder = pathlib.Path(__file__).parent.parent
    file_path = project_folder / file_name
    with open(file_path, "w", newline="", encoding="utf-8") as file:
       writer = csv.DictWriter(file, fieldnames=_journal[0].keys())
       writer.writeheader()
       writer.writerows(_journal)
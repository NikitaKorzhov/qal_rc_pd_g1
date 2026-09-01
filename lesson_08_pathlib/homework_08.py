from pathlib import Path
### Робота з файлами та папками — завдання
def print_task(task_number:int):
    print(f"Task {task_number}")

def write_file(file_path:Path,content:str):
    with open(file_path,"w",encoding="UTF-8") as file:
        file.write(content)

def append_file(file_path:Path,content:str):
    with open(file_path,"a",encoding="utf-8") as file:
        file.write(content)

def read_file(file_path:Path)->str:
    with open(file_path,"r",encoding="utf-8") as file:
        return file.read()

target_file_name="hello.txt"
        
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
print_task(1)
if __name__ == "__main__":
    content="Hello, Python!"
    current=Path(__file__)
    path=current.parent/target_file_name
    try:
        write_file(path,content)
        print("Created succesfuly!")
    except:
      print("Error")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
print_task(2)
if __name__=="__main__":
    current=Path(__file__)
    path=current.parent/target_file_name
    try:
        content=read_file(path)
        print(f"File content is:\n{content}")
    except:
        print(f"File {target_file_name} exiist")

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
print_task(3)
content_for_append="\nLearning file operations."
if __name__=="__main__":
    current=Path(__file__)
    path=current.parent/target_file_name
    try:
      append_file(path,content_for_append)
      print(f"File {target_file_name} is appand with {content_for_append}")
    except:
       print(f"File {target_file_name} exiist")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
print_task(4)
if __name__ == "__main__":
    current = Path(__file__)
    path = current.parent / target_file_name
    try:
        with open(path, "r", encoding="utf-8") as file:
            print("Reading lines one by one:")
            for line in file:
                print(line.rstrip())
    except:
        print(f"File {target_file_name} does not exist")

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
print_task(5)
def count_chars_in_file(path:Path)->int:
    with open(path,"r",encoding="utf-8") as file:
        return sum(len(line) for line in file)
    
if __name__ == "__main__":
    current = Path(__file__)
    path = current.parent / target_file_name
    try:
        char_count = count_chars_in_file(path)
        print(f"Кількість символів (через sum): {char_count}")
    except FileNotFoundError:
        print(f"File {target_file_name} does not exist")

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
print_task(6)
if __name__ == "__main__":
    file_name="notes.txt"
    current_script_dir = Path(__file__).parent
    target_directory = current_script_dir/ "directory" / "data"
    file_path = target_directory / file_name
    try:
      target_directory.mkdir(parents=True, exist_ok=True)   
      print("Директорія створена успішно!")
      file_path.write_text("My first note.", encoding="utf-8")
      print(f"Файл '{file_name}' успішно створено у палці '{target_directory.name}'!")
    except OSError as e:
        print(f"Сталася помилка при роботі з файловою системою: {e}")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
print_task(7)
if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    target_directory = current_script_dir/ "directory" / "data"

    try:
        for file in target_directory.iterdir():
            print(file.name)
    except OSError as e:
        print(f"Помилка при читанні директорії: {e}")

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
print_task(8)
if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    target_directory = current_script_dir/ "directory" / "data"
    source_file = target_directory / "notes.txt"
    copy_file = target_directory / "copy.txt"

    try:
        content = source_file.read_text(encoding="utf-8")
        copy_file.write_text(content, encoding="utf-8")
        print(f"Вміст успішно скопійовано з '{source_file.name}' у '{copy_file.name}'!")
        
    except OSError as e:
        print(f"Сталася помилка при роботі з файлами: {e}")

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
print_task(9)
if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    folder = current_script_dir/ "directory" / "data"
    
    try:
        combined = (folder / "a.txt").read_text(encoding="utf-8") + (folder / "b.txt").read_text(encoding="utf-8")
        (folder / "ab.txt").write_text(combined, encoding="utf-8")
        print("Успішно об'єднано!")
    except OSError as e:
        print(f"Помилка: {e}")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
print_task(10)
word="note"
if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    target_directory = current_script_dir/ "directory" / "data"
    target_file = target_directory / "notes.txt"

    try:
        content = target_file.read_text(encoding="utf-8")
        
        if word in content:
            print("Знайдено")
        else:
            print("Не знайдено")
            
    except OSError as e:
        print(f"Помилка при роботі з файлом: {e}")

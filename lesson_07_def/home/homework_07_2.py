#Tech_block
def print_task(number:int,description:str="")->None:
    """Print task number

    :param number: Task number
    :type number: int
    :param description: Task description
    :type description: str
    """
    print(f"Task {number}. {description}")

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number: int) -> None:
    multiplier = 1
    while number * multiplier <= 25:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print_task(1)
print(" Numbers with results for 25")
multiplication_table(5)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print_task(2,"Написати функцію, яка обчислює суму двох чисел.")
def custom_sum(a:float,b:float)->float:
    """Функція, що рахує сумм 2 чисел"""
    return a+b

a=2.6
b=3.4
print(f"Use custom sum for numbers {a} and {b} is {custom_sum(a,b)}")
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print_task(3,"Написати функцію, яка розрахує середнє арифметичне списку чисел")
def get_average(numbers: list) -> float:
    """Розраховує середнє арифметичне списку чисел.
    
    :param numbers Список чисел
    :type numbers list"""
    return sum(numbers) / len(numbers)
numbers_list = [5, 6, 7, 8]
print(f"Середнє арифметичне списку {numbers_list}: {get_average(numbers_list)}")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print_task(4,"Написати функцію, яка приймає рядок та повертає його у зворотному порядку.")

def reverse_text(text:str)->str:
    """Функція, що приймає рядок і виводить його у зворотному порядку
    
    :param text: Рядок тексту
    :type text: str"""
    return text[::-1]

text=input("Введіть текст для його виводу у зворотному порядку: ")
print(f"Введений текст: {text}\nЗворотний порядок: {reverse_text(text)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print_task(5,"Написати функцію, яка приймає список слів та повертає найдовше слово у списку.")
def find_longest_word(words: list[str]) -> str:
    """Find the longest word in a list.

    :param words: List of string elements
    :type words: list[str]
    :return: The longest word or None if list is empty
    """
  
    return max(words, key=len)
word_list=[]
print("Input words, for exit and see result print q : ")
while True:
    word=input("Input your word, for exot print 'q' : ")
    if word=="q":
        break
    word_list.append(word)

if len(word_list)>0:
    print(f"Largest word in list is {find_longest_word(word_list)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print_task(6)
def find_substring(str1: str, str2: str) -> int:
    """Find the index of the first occurrence of str2 in str1.

    :param str1: Main string
    :param str2: Substring to search for
    :return: First index of str2 in str1, or -1 if not found
    """
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7. Знайдіть всі унікальні елементи в списку small_list
print_task(7,"Знайдіть всі унікальні елементи в списку small_list")
def find_unique_elements(items:list)->list:
    """Функція на вхід приймає список і повертає список усіх унікальних елементів
    
    :param items: List of numbers
    :type items: list"""
    return list(set(items))

small_list = [3, 1, 4, 5, 2, 5, 3]
unique_list = find_unique_elements(small_list)
print(f"Original list: {small_list}\nUnique elements in original list {unique_list}")


# task 8-10
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

print("Початковий текст для завдань 8-10",adwentures_of_tom_sawer,"\n")
task8_desc=""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print_task(8,task8_desc)

def replace_new_line_char_with_space(text:str)->str:
    """Функція, що змінює '\n' на пробіл і повертає новий рядок
            
        :param text: Переданий текст
        :type text: str"""
    return text.replace("\n", " ")
adwentures_of_tom_sawer =replace_new_line_char_with_space(adwentures_of_tom_sawer)
print("Result of task 8 ",adwentures_of_tom_sawer)
print_task(9,"Написати функцію,  що вертає рядок без входжень '....' ЇЇ використання у наступному завдані.")
def get_text_without_dot_repeating(text:str)->str:
    """Функція, що видаляє '....' і повертає новий рядок
        
    :param text: Переданий текст
    :type text: str"""
    return text.replace("....", " ")
print_task(10,"Виведіть кількість слів останнього речення з adwentures_of_tom_sawer")
def count_words_in_last_sentense(text:str)->int:
    """Функція, що рахує кількість слів у останньому ркчені
    
    :param text: Переданий текст
    :type text: str"""
    cleaned_text = get_text_without_dot_repeating(text)    
    sentenses = [s.strip() for s in cleaned_text.split(".") if s.strip()]
    last_sentense = sentenses[-1]
    return len(last_sentense.split())

print("Текст:", adwentures_of_tom_sawer)
print("Кількість слів у всьому реченні:", count_words_in_last_sentense(adwentures_of_tom_sawer))
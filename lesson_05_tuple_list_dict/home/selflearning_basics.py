# -*- coding: utf-8 -*-
# Самостійне вивчення методів list, tuple, set, dict
# Виконайте завдання та збережіть результати у вказаних змінних

print("=== РОБОТА З СПИСКАМИ (LIST) ===")

# Task 1. Створіть список з числами від 1 до 5
numbers = [x for x in range(1, 6)] # Ваш код тут

# Task 2. Додайте число 6 в кінець списку numbers
# Ваш код тут
numbers.append(6)

# Task 3. Вставте число 0 на початок списку numbers  
# Ваш код тут
numbers.insert(0, 0)

print(f"Numbers {numbers}")

# Task 4. Видаліть перше входження числа 3 зі списку numbers
# Ваш код тут
numbers.remove(3)

# Task 5. Знайдіть індекс елемента 'cherry' у списку fruits
fruits = ['apple', 'banana', 'cherry', 'banana', 'date']
cherry_index = fruits.index("cherry")  # Ваш код тут
print(f"Chery {cherry_index}")

# Task 6. Порахуйте кількість входжень 'banana' у списку fruits
banana_count = fruits.count("banana")  # Ваш код тут

# Task 7. Відсортуйте список fruits за алфавітом
# Ваш код тут
sorted_friuts=fruits.sort()

# Task 8. Створіть копію списку fruits
fruits_copy = fruits.copy()

print("\n=== РОБОТА З КОРТЕЖАМИ (TUPLE) ===")

# Task 9. Створіть кортеж з днями тижня
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')  # Ваш код тут

# Task 10. Знайдіть індекс 'Wednesday' у кортежі weekdays
wednesday_index = weekdays.index("Wednesday")  # Ваш код тут

# Task 11. Порахуйте кількість входжень 'Monday' у кортежі
test_tuple = ('Monday', 'Tuesday', 'Monday', 'Friday', 'Monday')
monday_count=test_tuple.count('Monday')  # Ваш код тут
print(f"Task 11 Monday is {monday_count} times tape weekdays")

# Task 12. Перетворіть кортеж weekdays на список
weekdays_list = list(weekdays)  # Ваш код тут


print("\n=== РОБОТА З МНОЖИНАМИ (SET) ===")

# Task 13. Створіть множину з унікальних чисел
unique_numbers = set([x for x in range(1,6)])  # Ваш код тут: додайте числа 1, 2, 3, 4, 5

# Task 14. Додайте число 6 до множини unique_numbers
# Ваш код тут
unique_numbers.add(6)
# Task 15. Видаліть число 3 з множини unique_numbers
# Ваш код тут
unique_numbers.remove(3)
# Task 16. Створіть дві множини та знайдіть їх об'єднання
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a|set_b  # Ваш код тут

# Task 17. Знайдіть перетин множин set_a та set_b
intersection_set = set_a&set_b  # Ваш код тут

# Task 18. Знайдіть різницю set_a - set_b
difference_set = set_a-set_b  # Ваш код тут

# Task 19. Перевірте, чи є число 4 у множині unique_numbers
is_four_present = 4 in unique_numbers  # Ваш код тут

print("\n=== РОБОТА З СЛОВНИКАМИ (DICT) ===")

# Task 20. Створіть словник з інформацією про студента
student = {}  # Ваш код тут: додайте ім'я, вік, група
student=dict(name="Nikita",age=28,group=4)

# Task 21. Додайте до словника student ключ 'grade' зі значенням 'A'
# Ваш код тут
student["grade"]="A"

# Task 22. Отримайте значення ключа 'name' зі словника student
student_name = student['name']  # Ваш код тут

# Task 23. Отримайте всі ключі словника student
student_keys =  student.keys()  # Ваш код тут
print(f"Student keys are {student_keys}")

# Task 24. Отримайте всі значення словника student  
student_values = student.values()  # Ваш код тут
print(f"Student values are {student_values}")

# Task 25. Видаліть ключ 'grade' зі словника student
# Ваш код тут
student.remove("grade")
print(f"Student dict is {student}")

# Task 26. Створіть словник з квадратами чисел від 1 до 5
squares_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  # Ваш код тут: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(f"squares_dict is {squares_dict}")
# Task 27. Перевірте, чи існує ключ 3 у словнику squares_dict
key_exists = 3 in squares_dict  # Ваш код тут
print(f"Value 3 in squares_dict {key_exists}")
# Task 28. Оновіть словник student новими даними
new_data = {'city': 'Kyiv', 'hobby': 'programming'}
# Ваш код тут
new_data["country"]="Ukraine"
if __name__ == "__main__":
    print("\n=== ЗАВЕРШЕННЯ ===")
    print("Всі завдання виконано! Запустіть test_selflearning.py для перевірки.")
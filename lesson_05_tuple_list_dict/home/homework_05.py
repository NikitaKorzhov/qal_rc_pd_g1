# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_list = list(set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = sum(small_list) / len(small_list)
print(average)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
has_duplicates = len(big_list) != len(set(big_list))
print(has_duplicates)
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key = max(add_dict, key=add_dict.get)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
inverted_dict = {value: key for key, value in base_dict.items()}
print(inverted_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
sum_dict = base_dict.copy()
for k, v in add_dict.items():
    if k in sum_dict:
        sum_dict[k] = f"{sum_dict[k]}{v}"  
    else:
        sum_dict[k] = v

print(sum_dict)

# task 7.
line = "Створіть список з всіх символів, які входять у заданий рядок"
char_list = list(line)
print(char_list)

# task 8. Обчисліть суму елементів двох змінних через sum()
value_1  = [1, 2, 3, 4, 5]
value_2 = (4, 6, 5, 10)
total_sum = sum(value_1) + sum(value_2)
print(total_sum)


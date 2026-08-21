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
task_name=""
def print_result(result_text,result):
    print(f"{task_name}\n {result_text}: {result}")
# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
task_name="Task1"
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print_result("Result",adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
task_name="Task 2"
adwentures_of_tom_sawer=adwentures_of_tom_sawer.replace("...."," ")
print_result("Result",adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
task_name="Task 3"
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print_result("Result",adwentures_of_tom_sawer)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
task_name="Task 4"
print_result("Кількість літер 'h' у речені",adwentures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
task_name="Task 5"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
capital_count=0
for later in alphabet:
    capital_count+=adwentures_of_tom_sawer.count(later)
print_result("Слів з великої літери у тексті",capital_count)



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
task_name="Task 6"
word = "Tom"
first_pos = adwentures_of_tom_sawer.find(word)
second_pos = adwentures_of_tom_sawer.find(word, first_pos + 1)
print_result("Слово Tom вдруге зустрічається на позиції",second_pos)
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
task_name="Task 7"
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print_result("Result", adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
task_name="Task 8"
print_result("4 речення",adwentures_of_tom_sawer_sentences[3].lower().strip())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
has_by_the_time = any(sentence.strip().startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)

print_result("Чи починається якесь речення з 'By the time'", has_by_the_time)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
task_name="Task 10"
words = adwentures_of_tom_sawer_sentences[-1].split()

# Якщо після останньої крапки був пробіл і розбиття дало порожній список — беремо передостаннє речення:
if not words:
    words = adwentures_of_tom_sawer_sentences[-2].split()

print_result("Кількість слів останнього речення", len(words))
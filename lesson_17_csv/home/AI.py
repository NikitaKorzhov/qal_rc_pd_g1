import random

# 1. Підготовка даних для навчання (наші «приклади»)
# Якщо x = 1, то y = 2
# Якщо x = 2, то y = 4
# Якщо x = 3, то y = 6
inputs = [1, 4, 16, 64]
outputs = [4, 16, 64, 256]  # Очікувані результати (y = x * 10)

# 2. Ініціалізація моделі "з нуля"
# Беремо випадкове число як початкову вагу (weight) нашої нейромережі
weight = random.random()
learning_rate = 0.0000001  # Швидкість навчання (як сильно ми змінюємо вагу за раз)

print(f"Початкова випадкова вага моделі: {weight:.4f}\n")

# 3. Процес навчання (епохи)
for epoch in range(1000000):
  total_error = 0

  for x, y_true in zip(inputs, outputs):
    # А. Прогноз моделі (Prediction): множимо вхід на нашу вагу
    y_pred = x * weight

    # Б. Обчислюємо помилку (Error): наскільки ми помилилися
    error = y_pred - y_true
    total_error += error**2

    # В. Коригування ваги (Зворотне поширення помилки / Backpropagation)
    # Змінюємо вагу так, щоб зменшити похибку
    weight -= learning_rate * (2 * error * x)

  # Виводимо прогрес кожні 200 кроків
  if (epoch + 1) % 2 == 0:
    print(f"Епоха {epoch + 1}: поточна вага = {weight:.4f}, помилка = {total_error:.4f}")

print(f"\nНавчання завершено! Фінальна вага: {weight:.4f}")

# 4. Тестуємо нашу модель на нових даних, яких вона не бачила
test_input = 5
prediction = test_input * weight
print(f"Якщо на вхід подати {test_input}, модель прогнозує: {prediction:.2f} (очікувалося 10)")
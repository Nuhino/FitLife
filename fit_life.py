print(
    "Здравствуйте, Вас приветствует цифровой фитнес-трекер FitLife MVP! "
    "Для продолжения работы введите своё имя и возраст."
)
user_name = input("Введите своё имя: ")

while True:
    try:
        user_age = int(input("Введите свой возраст: "))
        break  # если число введено корректно — выходим из цикла
    except ValueError:
        print("Пожалуйста, введите свой возраст, используя целое число.")


while True:
    try:
        user_weight = float(input("Введите свой вес в килограммах: "))
        break
    except ValueError:
        print("Пожалуйста, введите свой вес, используя число.")


while True:
    try:
        user_height = float(input("Введите свой рост в метрах: "))
        break
    except ValueError:
        print("Пожалуйста, введите свой рост, используя число.")

bmi = user_weight / (user_height ** 2)  # формула вычисления имт
water_ml = user_weight * 30  # формула расчета дневной нормы потребления воды
water_l = water_ml / 1000

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.2f} л. в день \n")
print("Расчет окончен. Будьте здоровы!")

# Задание 1

def city_generator(cities, total=1_000_000):
    if not cities:
        raise ValueError("Список городов пуст")

    index = 0
    for _ in range(total):
        yield cities[index]
        index = (index + 1) % len(cities)


if __name__ == "__main__":
    cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
    gen = city_generator(cities)
    for i in range(20):
        print(next(gen))

from app.task1 import city_generator

def test_cycle():
    cities = ["A", "B", "C"]
    gen = city_generator(cities, total=5)
    result = [next(gen) for _ in range(5)]
    assert result == ["A", "B", "C", "A", "B"]

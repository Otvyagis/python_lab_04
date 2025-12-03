from app.task2 import tuple_generator

def test_tuple_length():
    gen = tuple_generator(5, -1, 1)
    val = next(gen)
    assert len(val) == 5

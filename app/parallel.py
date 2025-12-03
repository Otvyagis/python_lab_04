import time
from multiprocessing import Pool
from app.task1 import city_generator

def generate_single_process(cities, total=1_000_000):
    for _ in city_generator(cities, total):
        pass

def worker(chunk):
    for _ in chunk:
        pass

def generate_multi_process(cities, total=1_000_000_000, processes=4):
    gen = city_generator(cities, total)
    chunk_size = total // processes
    chunks = [[next(gen) for _ in range(chunk_size)] for _ in range(processes)]

    with Pool(processes=processes) as pool:
        pool.map(worker, chunks)

def benchmark(cities, total=1_000_000, processes=4):
    print("БЕНЧМАРК")

    t1 = time.perf_counter()
    generate_single_process(cities, total)
    t1 = time.perf_counter() - t1

    t2 = time.perf_counter()
    generate_multi_process(cities, total, processes)
    t2 = time.perf_counter() - t2
    print(f"Многопроцессорная версия ({processes} процессов): {t1:.4f} сек")
    print(f"Обычный генератор (1 процесс): {t2:.4f} сек")

    print(f"Ускорение: {t2 / t1:.2f}x")

if __name__ == "__main__":
    cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
    benchmark(cities)

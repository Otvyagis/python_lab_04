# Задание 3

def build_table(text: str):
    words = text.split()
    if len(words) < 3:
        raise ValueError("Слов должно быть минимум 3")

    truncated = words[:len(words) // 3 * 3]

    rows = zip(*(iter(truncated),) * 3)

    return [" ".join(row) for row in rows]


if __name__ == "__main__":
    s = "123 321 123 321 6543 754 687"
    for line in build_table(s):
        print(line)

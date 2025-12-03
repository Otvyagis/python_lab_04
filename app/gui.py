from PySide6.QtWidgets import (
    QApplication, QWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QLineEdit,
    QPushButton, QLabel, QHBoxLayout
)

from .task1 import city_generator
from .task2 import tuple_generator
from .task3 import build_table


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генераторы Python — 3 задачи")

        layout = QVBoxLayout()
        tabs = QTabWidget()

        tab1 = QTextEdit()
        tab1.setReadOnly(True)
        cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
        gen = city_generator(cities)
        tab1.setText("\n".join(next(gen) for _ in range(20)))
        tabs.addTab(tab1, "Задание 1")

        tab2 = QWidget()
        t2_layout = QVBoxLayout()

        line_n = QLineEdit()
        line_a = QLineEdit()
        line_b = QLineEdit()

        line_n.setPlaceholderText("Длина кортежа n")
        line_a.setPlaceholderText("Минимум (a)")
        line_b.setPlaceholderText("Максимум (b)")

        btn_gen2 = QPushButton("Сгенерировать 20x20 таблицу")
        output2 = QTextEdit()
        output2.setReadOnly(True)

        def run_task2():
            try:
                n = int(line_n.text())
                a = int(line_a.text())
                b = int(line_b.text())
                gen = tuple_generator(n, a, b)
                matrix = [next(gen) for _ in range(20)]
                output2.setText("\n".join(" ".join(map(str, row)) for row in matrix))
            except Exception as e:
                output2.setText(f"Ошибка: {e}")

        btn_gen2.clicked.connect(run_task2)

        t2_layout.addWidget(QLabel("Введите параметры генератора:"))
        t2_layout.addWidget(line_n)
        t2_layout.addWidget(line_a)
        t2_layout.addWidget(line_b)
        t2_layout.addWidget(btn_gen2)
        t2_layout.addWidget(output2)

        tab2.setLayout(t2_layout)
        tabs.addTab(tab2, "Задание 2")

        tab3 = QWidget()
        t3_layout = QVBoxLayout()

        input3 = QLineEdit()
        input3.setPlaceholderText("Введите строку из слов...")
        btn_gen3 = QPushButton("Построить таблицу 3×N")

        output3 = QTextEdit()
        output3.setReadOnly(True)

        def run_task3():
            try:
                text = input3.text()
                result = build_table(text)
                output3.setText("\n".join(result))
            except Exception as e:
                output3.setText(f"Ошибка: {e}")

        btn_gen3.clicked.connect(run_task3)

        t3_layout.addWidget(QLabel("Введите строку слов через пробел:"))
        t3_layout.addWidget(input3)
        t3_layout.addWidget(btn_gen3)
        t3_layout.addWidget(output3)

        tab3.setLayout(t3_layout)
        tabs.addTab(tab3, "Задание 3")

        layout.addWidget(tabs)
        self.setLayout(layout)


def run_gui():
    app = QApplication([])
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    app.exec()

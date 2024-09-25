import tkinter as tk
import random


def generate_full_groups(probabilities, N: int = 10**6):
    k = len(probabilities)
    indicators = []

    cumulative_probabilities = [sum(probabilities[:i + 1]) for i in range(k)]

    for _ in range(N):
        rand_num = random.random()

        for i, cp in enumerate(cumulative_probabilities):
            if rand_num < cp:
                indicators.append(i)
                break

    frequencies = [indicators.count(i) / N for i in range(k)]

    return frequencies


def on_run_button_click():
    try:
        input_probabilities = probabilities_entry.get()
        probabilities = list(map(float, input_probabilities.split(',')))

        if not all(0 <= p <= 1 for p in probabilities):
            result_label.config(text='Ошибка! Все вероятности должны быть между 0 и 1')
            return

        if abs(sum(probabilities) - 1.0) > 1e-9:
            result_label.config(text='Ошибка! Сумма вероятностей должна быть равна 1')
            return

        frequencies = generate_full_groups(probabilities)
        result_text = ''

        for i, (p, f) in enumerate(zip(probabilities, frequencies)):
            result_text += f'Событие {i + 1}: Теоретическая вероятность = {p}, Частота = {f:.4f}\n'
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text='Ошибка! Введите корректные данные!')


root = tk.Tk()
root.title('Task4')

probabilities_label = tk.Label(root, text='Введите вероятности через запятую')
probabilities_label.pack()

probabilities_entry = tk.Entry(root, width=50)
probabilities_entry.pack()

run_button = tk.Button(root, text='Run', command=on_run_button_click)
run_button.pack(pady=10)

result_label = tk.Label(root, text='Results')
result_label.pack()

root.mainloop()

import random
import tkinter as tk


def generate_events(probabilities, N: int = 10 ** 6):

    #Генерирует список значений True/False, соответствующих случайным событиям с заданными вероятностями.

    events = []

    # Проходим по каждому событию
    for _ in range(N):
        event_happened = True  # Изначально событие предполагается успешным

        # Для каждого события проверяем выполнение всех вероятностей
        for probability in probabilities:
            if random.random() > probability:  # Событие не происходит, если случайное значение больше вероятности
                event_happened = False
                break

        events.append(event_happened)

    return events


def calculate_frequencies(events):
    return sum(events) / len(events) # частота выпадения события True в списке.


def on_run_button_click():
    try:
        input_probabilities = probabilities_entry.get()
        probabilities = list(map(float, input_probabilities.split(',')))

        if not all(0 <= p <= 1 for p in probabilities):
            result_label.config(text='Ошибка! Все вероятности должны быть между 0 и 1')
            return

        # Теоретическая вероятность - произведение всех вероятностей
        common_probability = 1
        for probability in probabilities:
            common_probability *= probability

        # Генерация событий и расчет частоты
        events = generate_events(probabilities)
        frequencies = calculate_frequencies(events)
        result_text = f'Теоретическая вероятность = {common_probability:.4f}, Частота события = {frequencies:.4f}'
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text='Ошибка! Введите корректные данные!')


root = tk.Tk()
root.title('Task2')

probabilities_label = tk.Label(root, text='Введите вероятности через запятую')
probabilities_label.pack()

probabilities_entry = tk.Entry(root, width=50)
probabilities_entry.pack()

run_button = tk.Button(root, text='Run', command=on_run_button_click)
run_button.pack(pady=10)

result_label = tk.Label(root, text='Results')
result_label.pack()

root.mainloop()

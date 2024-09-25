import tkinter as tk
import random


def get_event_freq(events, N: int = 10**6):
    return sum(events) / N


def generate_simple_events(probability: float, N: int = 10**6):
    events = [random.random() < probability for _ in range(N)]
    frequency = get_event_freq(events)

    return frequency


def on_run_button_click():
    probability = slider.get()
    theoretical_value = probability
    frequency = generate_simple_events(probability)

    result_label.config(text=f'Частота события: {frequency:.4f}')
    theoretical_label.config(text=f'Теоретическое значение: {theoretical_value:.4f}')


root = tk.Tk()
root.title('Task1')

slider_label = tk.Label(root, text='Выберите вероятность события от 0 до 1')
slider_label.pack()

slider = tk.Scale(root, from_=0, to=1, orient='horizontal', resolution=0.01, length=300)
slider.set(0.75)
slider.pack()

run_button = tk.Button(root, text='Run', command=on_run_button_click)
run_button.pack(pady=10)

result_label = tk.Label(root, text='Частота события: --')
result_label.pack()

theoretical_label = tk.Label(root, text='Теоретическое значение: --')
theoretical_label.pack()

root.mainloop()

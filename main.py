import tkinter as tk
from tkinter import messagebox
import random
import time

# Create a list of words
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

# Generate a random paragraph of 150 words
paragraph = " ".join(random.choice(words) for _ in range(150))

# Create the GUI
root = tk.Tk()

text_widget = tk.Text(root, width=50, height=10)
text_widget.insert(tk.END, paragraph)
text_widget.pack()

entry_widget = tk.Entry(root)
entry_widget.pack()

start_button = tk.Button(root, text="Start", command=lambda: start_test())
start_button.pack()

timer_label = tk.Label(root, text="1:00")
timer_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

start_time = None
remaining_time = 60

def start_test():
    global start_time
    start_time = time.time()
    countdown(remaining_time)
    root.after(60000, end_test)  # end the test after 60000 milliseconds (1 minute)

def countdown(time_left):
    if time_left > 0:
        timer_label.config(text=f"{time_left // 60}:{time_left % 60:02}")
        root.after(1000, countdown, time_left - 1)

def check_spelling(event):
    typed_words = entry_widget.get().split()
    if len(typed_words) <= len(paragraph.split()) and typed_words[-1] != paragraph.split()[len(typed_words)-1]:
        messagebox.showwarning("Typing Error", "You missed or spelled a word wrong. Please backspace.")

entry_widget.bind("<space>", check_spelling)

def end_test():
    typed_words = entry_widget.get().split()
    paragraph_words = paragraph.split()
    correct_words = 0

    for typed_word, paragraph_word in zip(typed_words, paragraph_words):
        if typed_word == paragraph_word:
            correct_words += 1

    words_per_minute = correct_words / 1  # 1 minute
    result_label.config(text=f"You typed {words_per_minute} words per minute.")

root.mainloop()


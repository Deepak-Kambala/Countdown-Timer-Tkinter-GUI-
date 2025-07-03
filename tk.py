
import tkinter as tk
from tkinter import messagebox
import time
import threading

def start_countdown():
    try:
        total_time = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter time in seconds (number only).")
        return

    def countdown():
        nonlocal total_time  
        while total_time >= 0:
            mins, secs = divmod(total_time, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            label.config(text=time_str)
            time.sleep(1)
            total_time -= 1
        messagebox.showinfo("Time's up!", "⏰ Countdown Finished!")

    threading.Thread(target=countdown, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("250x150")

tk.Label(root, text="Enter time (seconds):").pack(pady=0)

entry = tk.Entry(root, justify='center')
entry.pack(pady=5)

tk.Button(root, text="Start Timer", command=start_countdown).pack(pady=5)

label = tk.Label(root, text="00:00", font=("Arial", 30))
label.pack(pady=10)

root.mainloop()

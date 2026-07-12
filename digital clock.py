from tkinter import *
import time
root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_time)
clock = Label(
    root,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="cyan"
)
clock.pack(expand=True)
update_time()
root.mainloop()
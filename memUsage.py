import tkinter as tk
import psutil


def update_ram_label():
    ram_percent = psutil.virtual_memory().percent
    ram_label.config(text=f"Mem: {ram_percent:.2f}%")
    root.after(600, update_ram_label) 


root = tk.Tk()
root.title("RAM Usage Monitor")
root.overrideredirect(True)  # Hiding the title bar and window controls
root.config(bg="#212121")

# Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position
window_width = 105
window_height = 32
taskbar_height = 50  # Adjust this based on your taskbar height
window_x = screen_width - window_width
window_y = screen_height - window_height - taskbar_height

root.geometry(f"{window_width}x{window_height}+{window_x - 4}+{window_y}")

# Make the RamUsage window stay on top
root.wm_attributes("-topmost", 1)

ram_label = tk.Label(root, font=("Arial", 10, "bold"), bg="#212121", fg="#f5f5f5")
ram_label.pack(padx=10, pady=5)

update_ram_label()  # Calling the Function

print("Memory(RAM) Monitor Script is Running")

root.mainloop()

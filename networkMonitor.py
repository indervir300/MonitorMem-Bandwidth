import tkinter as tk
import psutil

def get_size(bytes):
    """Returns size of bytes in a nice format."""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def update_stats():
    global io_1
    io_2 = psutil.net_io_counters()
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

    # Calculating the speed (new - old stats)
    us, ds = bytes_sent - io_1.bytes_sent, bytes_recv - io_1.bytes_recv

    # Update labels
    upload_label.config(text=f"Up: {get_size(bytes_sent)}")
    download_label.config(text=f"Down: {get_size(bytes_recv)}")
    upload_speed_label.config(text=f"Up Speed: {get_size(us / UPDATE_DELAY)}/s")
    download_speed_label.config(text=f"Down Speed: {get_size(ds / UPDATE_DELAY)}/s")

    # Update the bytes_sent and bytes_recv for the next iteration
    io_1 = io_2
    root.after(UPDATE_DELAY * 1000, update_stats)

# Create the main window
root = tk.Tk()
root.title("Network Bandwidth Monitor")
root.configure(bg="#212121")
root.resizable(False, False)

# Initialize the initial network stats
io_1 = psutil.net_io_counters()

# Create a main frame
main_frame = tk.Frame(root, bg="#212121")
main_frame.pack(fill="x", pady=10, padx=5)

# Create labels
upload_label = tk.Label(main_frame, text=f"Up: {get_size(io_1.bytes_sent)}", font=("Arial", 8, "bold"), fg="#f5f5f5", bg="#212121")
download_label = tk.Label(main_frame, text=f"Down: {get_size(io_1.bytes_recv)}", font=("Arial", 8, "bold"), fg="#f5f5f5", bg="#212121")
upload_speed_label = tk.Label(main_frame, text="Up Speed: N/A", font=("Arial", 8, "bold"), fg="#f5f5f5", bg="#212121")
download_speed_label = tk.Label(main_frame, text="Down Speed: N/A", font=("Arial", 8, "bold"), fg="#f5f5f5", bg="#212121")

upload_label.grid(row=0, column=0, padx=5)
download_label.grid(row=0, column=1, padx=5)
upload_speed_label.grid(row=0, column=2, padx=5)
download_speed_label.grid(row=0, column=3, padx=5)

UPDATE_DELAY = 1 # 1sec Delay
root.after(0, update_stats)

print("Network BandWidth Monitor Script is Running")

root.mainloop()
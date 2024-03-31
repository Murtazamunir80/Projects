import tkinter as tk
from tkinter import ttk
from datetime import datetime


# Function to update the clock labels with current time, day, and date
def update_clock():
    # Get current time, day, and date
    current_time = datetime.now().strftime('%H:%M:%S')
    current_day = datetime.now().strftime('%A')
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Update the clock labels with current time, day, and date
    clock_label.config(text=current_time)
    day_label.config(text=current_day)
    date_label.config(text=current_date)

    # Schedule the update_clock function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_clock)


# Create main Tkinter window
root = tk.Tk()
root.title("Live Clock By Murtaza")

# Set background color to pink
root.configure(background='pink')

# Set window size to 400x200 pixels
root.geometry('800x300')

# Create label to display current time
clock_label = ttk.Label(root, font=('calibri', 60, 'bold'), background='pink', anchor='center')
clock_label.pack(fill='both', expand=True)

# Create label to display current day
day_label = ttk.Label(root, font=('calibri', 30, 'bold'), background='pink', anchor='center')
day_label.pack(fill='both', expand=True)

# Create label to display current date
date_label = ttk.Label(root, font=('calibri', 30, 'bold'), background='pink', anchor='center')
date_label.pack(fill='both', expand=True)

# Call the update_clock function to start updating the clock labels
update_clock()

# Start the Tkinter event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def log_sleep():
    """Get the values from the input boxes and display them"""
    try:
        hours = int(hours_entry.get())
        energy = int(energy_entry.get())
        
        # Simple validation
        if hours < 0 or hours > 24:
            messagebox.showerror("Error", "Hours must be between 0 and 24")
            return
        
        if energy < 1 or energy > 10:
            messagebox.showerror("Error", "Energy must be between 1 and 10")
            return
        
        # Show success message
        messagebox.showinfo("Success", f"Logged: {hours} hours of sleep, {energy}/10 energy!")
        
        # Clear the input boxes
        hours_entry.delete(0, tk.END)
        energy_entry.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Sleep Tracker")
root.geometry("300x200")

# Create labels and input boxes
tk.Label(root, text="Sleep Tracker", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Hours of sleep:").pack()
hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

tk.Label(root, text="Energy level (1-10):").pack()
energy_entry = tk.Entry(root)
energy_entry.pack(pady=5)

# Create button
log_button = tk.Button(root, text="Log Sleep Data", command=log_sleep, 
                      bg="lightblue", font=("Arial", 10, "bold"))
log_button.pack(pady=15)

# Start the GUI
root.mainloop()

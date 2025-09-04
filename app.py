import tkinter as tk

def update_label():
    """Updates the label text with content from the entry field."""
    user_input = entry_field.get()
    label.config(text=f"Hello, {user_input}!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("400x200") # Set initial window size

# Create a label widget
label = tk.Label(root, text="HELLO WORLD!", font=("Arial", 16))
label.pack(pady=10) # Add padding around the label

# Start the Tkinter event loop
root.mainloop()
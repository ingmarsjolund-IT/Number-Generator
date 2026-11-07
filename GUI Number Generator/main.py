#Library Import
import tkinter as tk
from tkinter import messagebox, filedialog
import random

def generate_numbers():
    try:
        num_sets = int(entry_sets.get())
        numbers_per_set = int(entry_numbers.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        return

    results = []
    for _ in range(num_sets):
        numbers = [random.randint(1, 49) for _ in range(numbers_per_set)]
        results.append(numbers)

# Clear previous results
    text_output.delete("1.0", tk.END)

# Show results in text box
    for i, numbers in enumerate(results, 1):
        text_output.insert(tk.END, f"Set {i}: {', '.join(map(str, numbers))}\n")

# Ask where to save
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as f:
            for i, numbers in enumerate(results, 1):
                f.write(f"Set {i}: {', '.join(map(str, numbers))}\n")
        messagebox.showinfo("Success", f"Numbers saved to {file_path}")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("400x400")

# Labels and inputs
tk.Label(root, text="How many sets of numbers?").pack(pady=5)
entry_sets = tk.Entry(root)
entry_sets.pack(pady=5)

tk.Label(root, text="How many numbers per set?").pack(pady=5)
entry_numbers = tk.Entry(root)
entry_numbers.pack(pady=5)

# Generate button
btn_generate = tk.Button(root, text="Generate Numbers", command=generate_numbers)
btn_generate.pack(pady=10)

# Output box
text_output = tk.Text(root, height=10, width=40)
text_output.pack(pady=10)

# Run the app
root.mainloop()

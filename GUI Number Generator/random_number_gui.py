#Library Import
import tkinter as tk
from tkinter import messagebox, filedialog
import random

def generate_numbers():
    try:
        num_sets = int(entry_sets.get())
        numbers_per_set = int(entry_numbers.get())
        min_range = int(entry_min.get())
        max_range = int(entry_max.get())

        if min_range >= max_range:
            messagebox.showerror("Input Error", "Minimum must be less than Maximum")
            return

        if numbers_per_set > (max_range - min_range + 1):
            messagebox.showerror("Input Error",
                                 "The number of unique numbers requested per set exceeds the available range.")
            return

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        return

    results = []
    for _ in range(num_sets):
        numbers = random.sample(range(min_range, max_range + 1), numbers_per_set)
        results.append(numbers)

# Clear previous results
    text_output.delete("1.0", tk.END)

# Show results in text box
    for i, numbers in enumerate(results, 0):  # start from 0
        letter = chr(65 + i)  # 65 = 'A' in ASCII
        text_output.insert(tk.END, f"Set {letter}: {', '.join(map(str, numbers))}\n")

# Ask where to save
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as f:
            for i, numbers in enumerate(results, 0):
                letter = chr(65 + i)
                f.write(f"Set {letter}: {', '.join(map(str, numbers))}\n")
        messagebox.showinfo("Success", f"Numbers saved to {file_path}")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("400x500")

# Labels and inputs
tk.Label(root, text="How many sets of numbers?").pack(pady=5)
entry_sets = tk.Entry(root)
entry_sets.pack(pady=5)

tk.Label(root, text="How many numbers per set?").pack(pady=5)
entry_numbers = tk.Entry(root)
entry_numbers.pack(pady=5)

tk.Label(root, text="Minimum number in range:").pack(pady=5)
entry_min = tk.Entry(root)
entry_min.pack(pady=5)

tk.Label(root, text="Maximum number in range:").pack(pady=5)
entry_max = tk.Entry(root)
entry_max.pack(pady=5)

# Generate button
btn_generate = tk.Button(root, text="Generate Numbers", command=generate_numbers)
btn_generate.pack(pady=10)

# Output box
text_output = tk.Text(root, height=25, width=60)
text_output.pack(pady=10)

# Run the app
root.mainloop()

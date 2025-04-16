import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    location = location_var.get()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for weight.")
        return

    if location == "Epe":
        if weight >= 10:
            cost = 10000
        else:
            cost = 5000
    elif location == "Ibeju-Lekki":
        if weight >= 10:
            cost = 5000
        else:
            cost = 3500
    else:
        messagebox.showerror("Invalid Input", "Please select a location.")
        return

    result_label.config(text=f"Delivery Cost: ₦{cost:,}")

root = tk.Tk()
root.title("Delivery Cost Calculator")
root.geometry("400x250")

tk.Label(root, text="Simi Services Delivery Cost Calculator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Select Delivery Location:").pack()
location_var = tk.StringVar()
location_menu = tk.OptionMenu(root, location_var, "Epe", "Ibeju-Lekki")
location_menu.pack()

tk.Label(root, text="Enter Package Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()

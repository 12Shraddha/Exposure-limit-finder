import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load data from a CSV file
mfile = pd.read_csv('modified_file _cas_twa.csv')



# Create a Tkinter window
root = tk.Tk()
root.title("Exposure limit finder")

# Set window size and position
win_width = 400
win_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (win_width/2))
y = int((screen_height/2) - (win_height/2))
root.geometry(f"{win_width}x{win_height}+{x}+{y}")

# Create style for the entry fields
style = ttk.Style()
style.configure("TEntry", font=("Arial", 14))

# Create labels and entry fields for chemical name and CAS number inputs
tk.Label(root, text="Chemical Name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(root, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="CAS Number:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
cas_entry = ttk.Entry(root, font=("Arial", 14))
cas_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a function to find TWA value for the entered chemical or CAS number
def find_twa():
    x_name = name_entry.get().lower()
    x_cas = cas_entry.get()

    for i in mfile.index:
        if str(mfile["Chemical"][i]).lower() == x_name or str(mfile["CAS Number"][i]) == x_cas:
            twa = mfile['Vacated 1989 OSHA PELs'][i]
            result_label.config(text="TWA Value: " + str(twa))
            name_entry.delete(0, tk.END)  # Clear the name entry field
            cas_entry.delete(0, tk.END)   # Clear the CAS entry field
            return

    result_label.config(text="No record")
    name_entry.delete(0, tk.END)  # Clear the name entry field
    cas_entry.delete(0, tk.END)   # Clear the CAS entry field

# Create a button to trigger the TWA value search
search_button = ttk.Button(root, text="Search", command=find_twa)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the TWA value search result
result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()



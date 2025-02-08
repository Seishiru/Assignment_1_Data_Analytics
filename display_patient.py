import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load dataset
df = pd.read_csv("patient_data.csv")

# Create GUI window
root = tk.Tk()
root.title("Patient Data Viewer")

# Create table
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create Treeview widget
tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")

# Define column headings
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert data into table
for i, row in df.iterrows():
    tree.insert("", "end", values=list(row))

tree.pack(fill=tk.BOTH, expand=True)

# Run GUI
root.mainloop()

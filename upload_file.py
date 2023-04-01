from tkinter import filedialog
import tkinter as tk
import pandas as pd

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Show the file selection dialog and get the file path
file_path = filedialog.askopenfilename()

# Load the file as a pandas DataFrame
data = pd.read_csv(file_path)

print(data.head(10))




# Now you can use the data for machine learning

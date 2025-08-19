import tkinter as tk
from commands import check_balance
# Create the main window
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")
# Specify main window sixe
root.geometry("500x400")

#add account number entry
account_number_entry = tk.Entry(root, width=100)
account_number_entry.pack(side="top")
# Add check balance button
check_balance_button = tk.Button(
  root, 
  text="Check balance",
  command=lambda : check_balance(account_number = account_number_entry.get()))
check_balance_button.pack(side="top")

# add deposit button
Deposit_btn = tk.Button (root, text = "Deposit")
Deposit_btn.pack (side="top")

# Open the main window
root.mainloop()
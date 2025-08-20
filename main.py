import tkinter as tk
from commands import check_balance
# Create the main window
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")

# create a tk frame for main window
frame = tk.Frame(root, padx=50, pady=50)
frame.pack()


#add account number entry
account_number_entry = tk.Entry(frame, width=50)
account_number_entry.grid(column=1, row=1)

# Add check balance button
check_balance_button = tk.Button(
  frame, 
  text="Check balance",
  command=lambda : check_balance(account_number = account_number_entry.get()))
check_balance_button.grid(column=2, row=1)

# add deposit button
Deposit_btn = tk.Button (frame, text = "Deposit")
Deposit_btn.grid(column=3, row=1)


# Open the main window
root.mainloop()
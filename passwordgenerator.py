import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    passlen = int(passlen_entry.get())
    capans = capvar.get()
    smallans = smallvar.get()
    digans = digvar.get()
    spans = spvar.get()
    rep = repvar.get()

    capchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', ',', '.']
    smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    comblis = []
    if capans == 'Yes':
        if smallans == 'Yes':
            if digans == 'Yes':
                if spans == 'Yes':
                    comblis = capchar + dig + spchar + smallchar
                else:
                    comblis = capchar + dig + smallchar
            else:
                if spans == 'Yes':
                    comblis = capchar + spchar + smallchar
                else:
                    comblis = capchar + smallchar
        else:
            if digans == 'Yes':
                if spans == 'Yes':
                    comblis = capchar + dig + spchar
                else:
                    comblis = capchar + dig
            else:
                if spans == 'Yes':
                    comblis = capchar + spchar
                else:
                    comblis = capchar
    else:
        if smallans == 'Yes':
            if digans == 'Yes':
                if spans == 'Yes':
                    comblis = dig + spchar + smallchar
                else:
                    comblis = dig + smallchar
            else:
                if spans == 'Yes':
                    comblis = spchar + smallchar
                else:
                    comblis = smallchar
        else:
            if digans == 'Yes':
                if spans == 'Yes':
                    comblis = dig + spchar
                else:
                    comblis = dig
            else:
                if spans == 'Yes':
                    comblis = spchar
                else:
                    messagebox.showerror("Error", "You denied the usage of all possible characters")
                    return

    # Generate the password
    password = ""
    if rep == 'Minimal Resource Usage (Way 1)':
        for i in range(passlen):
            password += comblis[random.randint(0, len(comblis) - 1)]
    else:
        random.shuffle(comblis)
        for i in range(passlen):
            q = random.choice(comblis)
            random.shuffle(comblis)
            password = password + q

    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and labels
tk.Label(root, text="Password Length:").grid(row=0, column=0)
passlen_entry = tk.Entry(root)
passlen_entry.grid(row=0, column=1)

capvar = tk.StringVar(value="Yes")
tk.Label(root, text="CAPITAL Alphabets:").grid(row=1, column=0)
tk.OptionMenu(root, capvar, "Yes", "No").grid(row=1, column=1)

smallvar = tk.StringVar(value="Yes")
tk.Label(root, text="Lowercase Alphabets:").grid(row=2, column=0)
tk.OptionMenu(root, smallvar, "Yes", "No").grid(row=2, column=1)

digvar = tk.StringVar(value="Yes")
tk.Label(root, text="Digits:").grid(row=3, column=0)
tk.OptionMenu(root, digvar, "Yes", "No").grid(row=3, column=1)

spvar = tk.StringVar(value="Yes")
tk.Label(root, text="Special Characters:").grid(row=4, column=0)
tk.OptionMenu(root, spvar, "Yes", "No").grid(row=4, column=1)

repvar = tk.StringVar(value="Minimal Resource Usage (Way 1)")
tk.Label(root, text="Password Generation Method:").grid(row=5, column=0)
tk.OptionMenu(root, repvar, "Minimal Resource Usage (Way 1)", "More Secure Generation (Way 2)").grid(row=5, column=1)

# Create the generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=6, column=0, columnspan=2)

# Create a label to display the generated password
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()

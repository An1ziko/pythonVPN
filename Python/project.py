import tkinter as tk
from tkinter import messagebox

def connect_to_vpn():
    server_address = entry_server.get()
    username = entry_username.get()
    password = entry_password.get()

    if server_address and username and password:
        # simulate a connection to VPN server
        messagebox.showinfo("Connected", "Connected to VPN Server")
    else:
        messagebox.showerror("Error", "Please fill in all the fields")

# create the main window
root = tk.Tk()
root.title("VPN")

# server address
label_server = tk.Label(root, text=" Server Address")
label_server.pack
entry_server = tk.Entry(root)
entry_server.pack()

# Username
label_username = tk.Label(root, text=" Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Password
label_password = tk.Label(root, text=" Password")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# connect the button
connect_button = tk.Button(root, text="connect", command=connect_to_vpn)
connect_button.pack()

# run the main loop()
root.mainloop()
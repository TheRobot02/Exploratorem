import tkinter as tk

class Application(tk.Frame):
    #A Tkinter GUI application that displays a list of connected clients.

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Connected Clients")
        self.pack()
        self.create_widgets()
        self.client_list_items = [] # initialize an empty list to hold client addresses


    def create_widgets(self):
        #Create the GUI widgets.
 
        self.client_list = tk.Listbox(self)
        self.client_list.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update_client_list(self, client_addr):
        #Update the client list in the GUI with the given client address.

        self.client_list.insert(tk.END, client_addr)
        for item in self.client_list_items:
            self.client_list.insert(tk.END, item)
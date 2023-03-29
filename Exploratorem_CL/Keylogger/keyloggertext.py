import tkinter as tk
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start Logging"
        self.start_button["command"] = self.start_logging
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop Logging"
        self.stop_button["command"] = self.stop_logging
        self.stop_button.pack(side="left")

    def start_logging(self):
        subprocess.call(["your_program.exe", "start"])

    def stop_logging(self):
        subprocess.call(["your_program.exe", "stop"])


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
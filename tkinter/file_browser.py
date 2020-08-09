import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def create_widgets(self):


    def create_search_location_entry(self):


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
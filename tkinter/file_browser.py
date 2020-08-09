import pathlib
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.path = tk.StringVar()
        self.path.set(pathlib.Path.cwd())
        self.path_temp = tk.StringVar()
        self.path_temp.set(self.path.get())

        self.create_widgets()

    def create_widgets(self):
        self.create_quit_button()
        self.create_search_location_entry()
        self.create_path_display()

    def create_search_location_entry(self):
        self.path_box = tk.Entry(self.master, width=100)
        self.path_box['textvariable'] = self.path_temp
        self.path_box.bind("<Return>", self.update_current_dir)
        self.path_box.pack()

    def update_current_dir(self, event):
        """Updates display of current directory (if valid) after user enters a new one"""
        if not pathlib.Path.is_dir(pathlib.Path(event.widget.get())):  # do nothing if path isn't valid directory
            return

        # self.path.set(self.path_box.get())
        self.path.set(self.path_temp.get())
        self.update_path_display()

    def create_path_display(self):
        """Does nothing more or less than displays the path where the user is currently browsing"""
        self.path_display = tk.Label(self.master)
        self.path_display['text'] = self.path.get()
        self.path_display.pack()

    def update_path_display(self):
        """Simply updates the displayed path.  Assumes that the path in `self.path"""
        self.path_display['text'] = self.path.get()

    def create_quit_button(self):
        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom", anchor="s")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
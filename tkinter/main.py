import tkinter as tk
import time, datetime as dt

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.contents = tk.StringVar()
        self.contents.set("POOP")
        self.window_title = tk.StringVar()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = "hello world!\n(Click me!)"
        self.hi_there['command'] = self.say_hi
        # self.hi_there.clipboard_append("POOP")
        self.hi_there.pack(ipadx=61, ipady=88, padx=79, pady=73)

        # self.hi_there.after(ms=200, func=self.make_new_button)
        # self.hi_there['command'] += self.do_stuff

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable
        self.contents = tk.StringVar()
        # Set it to some value
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.  It prints the current value of the variable
        self.entrythingy.bind('<Key-Return>', self.update_button_text_and_print_contents)

        self.window_title_updater = tk.Entry()
        self.window_title_updater.pack()

        self.redden = tk.Button()
        self.redden['text'] = "Turn stuff red!"
        self.redden.bind("<Button-1>", self.turn_red)
        self.redden.pack()

        # Make it kill the window when we click "QUIT"
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def turn_red(self, event):
        """This callback gets access to the widget that is experiencing the event via `event.widget`"""
        event.widget["activeforeground"] = 'red'
        event.widget["activebackground"] = '#aaaaaa'
        event.widget['width'] = 44

    def say_hi(self):
        print("Hi there, everyone!")
        self.make_new_button()

    def do_stuff(self):
        print(dt.datetime.now())

    def make_new_button(self):
        self.new_button = tk.Button(self)
        self.new_button['text'] = "another button!\n(Click me!)"
        self.new_button['command'] = self.do_stuff

        self.new_button.pack(side="left")

    def update_button_text_and_print_contents(self, event):
        self.hi_there['text'] = self.contents.get()
        self.print_contents(event)

    def print_contents(self, event):
        print(f"contents: {self.contents.get()}")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

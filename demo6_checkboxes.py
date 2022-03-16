import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create three IntVar objects to use with the checkboxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #Set the IntVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Option 1", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Option 2", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Option 3", variable=self.cb_var3)




     

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.myButton = tkinter.Button(
            self.main_window, text="Click me!", command=self.do_something
        )
        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.myButton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks for clicking into the button")

        tkinter.mainloop()


my_gui = MyGUI()


print("Moving on...")
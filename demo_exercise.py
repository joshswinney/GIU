from statistics import mean
import tkinter
import tkinter.messagebox 

class GradeAverage: 
    def __init__(self): 
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window) 

        self.prompt_label1 = tkinter.Label(self.top_frame,text = "Enter the score for test 1")
        self.prompt_label2 = tkinter.Label(self.top_frame,text = "Enter the score for test 2")
        self.prompt_label3 = tkinter.Label(self.top_frame,text = "Enter the score for test 3")

        self.test1_entry = tkinter.Entry(self.top_framce,width = 10)
        self.test2_entry = tkinter.Entry(self.top_framce,width = 10)
        self.test3_entry = tkinter.Entry(self.top_framce,width = 10)



        self.avg_button = tkinter.Button(self.main_window, text = "Average", command = self.average)
        self.quit_button = tkinter.Button(se)
    

        self.avgbutton.pack(side = "left")
        self.kilo_entry.apck(side = "right")

        self.descr_label = tkinter.Label(self.midframe, text = "Converted to miles:")

        self.miles_var = tkinter.StringVar()

        self.miles_label - tkinter.Label(self.mid_frame, textvaribale = self.miles_variable)
        

        tkinter.mainloop()

    def average(self):

        test1 = float(self.kilo_entry.get())
        
        average = mean()

        tkinter.mesagebox.showinfo("Average:", average)
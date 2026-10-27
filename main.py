import tkinter as tk
import tkinter.font as tkFont
from controller import *

#Name an instance variable for the controller
#What class are we instancing?

f_controller = controller()

class App:
    def __init__(self, root):
        #setting title
        root.title("Student Input")
        #setting window size
        width=476
        height=286
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        name_lbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        name_lbl["font"] = ft
        name_lbl["fg"] = "#333333"
        name_lbl["justify"] = "center"
        name_lbl["text"] = "Name"
        name_lbl.place(x=110,y=80,width=70,height=25)

        name_txt=tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        name_txt["font"] = ft
        name_txt["fg"] = "#333333"
        name_txt["justify"] = "center"
        name_txt["text"] = "Name_Entry"
        name_txt.place(x=210,y=80,width=70,height=25)


        class_lbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        class_lbl["font"] = ft
        class_lbl["fg"] = "#333333"
        class_lbl["justify"] = "center"
        class_lbl["text"] = "Class"
        class_lbl.place(x=110,y=120,width=70,height=25)

        class_txt=tk.Entry(root)
        class_txt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        class_txt["font"] = ft
        class_txt["fg"] = "#333333"
        class_txt["justify"] = "center"
        class_txt["text"] = "Class_Entry"
        class_txt.place(x=210,y=120,width=70,height=25)


        section_lbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        section_lbl["font"] = ft
        section_lbl["fg"] = "#333333"
        section_lbl["justify"] = "center"
        section_lbl["text"] = "Section"
        section_lbl.place(x=110,y=160,width=70,height=25)


        section_txt=tk.Entry(root)
        section_txt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        section_txt["font"] = ft
        section_txt["fg"] = "#333333"
        section_txt["justify"] = "center"
        section_txt["text"] = "Section_Entry"
        section_txt.place(x=210,y=160,width=70,height=25)

        #Button to submit the data to the database

        submit_btn=tk.Button(root)
        submit_btn["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        submit_btn["font"] = ft
        submit_btn["fg"] = "#000000"
        submit_btn["justify"] = "center"
        submit_btn["text"] = "Submit"
        submit_btn.place(x=210,y=240,width=70,height=25)
        submit_btn["command"] =lambda: self.submit_command(name_txt.get(), class_txt.get(), section_txt.get())


    #Submit button command to send the data to the controller
    def submit_command(self, p_name, p_class, p_section):
        print(p_name, p_class, p_section)
        f_controller.insert_student(p_name, p_class, p_section)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

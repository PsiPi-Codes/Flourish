import tkinter as tk
import tkinter.font as tkFont
import customtkinter
import os
import psutil
import time
from PIL import Image
from PIL import ImageTk
from tkinter import PhotoImage
import sprout.backend as Sprout

class App:
    def __init__(self, root : customtkinter.CTk):
        self.counter = psutil.boot_time()
        self.chosen = False


        root.lift()
        root._set_appearance_mode('dark')
        #setting title
        root.title("Flourish")
        root.resizable(False,False)
        #root.wm_iconphoto(False, ImageTk.PhotoImage('res/logo.png'))
        #setting window size
        width=250
        height=260
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        image_1 = customtkinter.CTkImage(light_image=Image.open('res\\b9709638-c419-4fb1-976c-20ca8a01a9f3.jpeg'), size=(100, 115))
        GLabel_243=customtkinter.CTkLabel(root, image=image_1, width=100, height=115)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["justify"] = "center"
        GLabel_243["text"] = "label"
        GLabel_243.place(x=10,y=10)

        image_2 = customtkinter.CTkImage(light_image=Image.open('res\\b9709638-c419-4fb1-976c-20ca8a01a9f3.jpeg'), size=(100, 115))
        GLabel_390=customtkinter.CTkLabel(root, image=image_1, width=100, height=115)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_390["font"] = ft
        GLabel_390["fg"] = "#333333"
        GLabel_390["justify"] = "center"
        GLabel_390["text"] = "label"
        GLabel_390.place(x=140,y=10)

        GButton_26=customtkinter.CTkButton(root, width=80,height=80, command=self.GButton_26_command, bg_color='transparent', text='Start Session')
        ft = tkFont.Font(family='Times',size=10)
        GButton_26["font"] = ft
        GButton_26["fg"] = "#000000"
        GButton_26["justify"] = "center"
        GButton_26["text"] = "Button"
        GButton_26.place(x=80,y=160)

    def GButton_26_command(self):
        print('command')
        desktopwindow = customtkinter.CTkToplevel(root)
        desktopwindow.title("test")
        desktopwindow.geometry("200x100")
        
        self.selected_process = customtkinter.StringVar()
        dropdown = customtkinter.CTkOptionMenu(desktopwindow, values=Sprout.get_current_running_applications(), variable=self.selected_process)
        self.entry_text = customtkinter.StringVar()
        entry = customtkinter.CTkEntry(desktopwindow)
        submit_button = customtkinter.CTkButton(desktopwindow, command=self.variable_handler)
        checkbox = customtkinter.CTkCheckBox(desktopwindow)


        dropdown.pack()
        entry.pack()
        checkbox.pack()
        submit_button.pack()
        
    def variable_handler(self):
        print(self.selected_process)
        print(self.entry_text)

        Sprout.append_application(self.selected_process.get(), self.entry_text)
        self.chosen = True

        #testing kill function

    
    def kill_process(self, process):
        os.system('taskkill /f /im {process}'.format(process = process))

    def process(self):
        self.counter = time.time()
        print(self.counter)
        
        if self.chosen:
            if (self.selected_process in Sprout.get_listed_running_applications()) and (Sprout.process_uptime(self.selected_process) >= int(Sprout.read_config(self.selected_process, 1))):
                self.kill_process(self.selected_process)
        root.after(1000, self.process)

        


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    app.process()
    root.mainloop()

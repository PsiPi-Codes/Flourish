import customtkinter
import sprout.backend as Sprout
import subprocess  
import numpy
import psutil
import time
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 

 
counter = 0
should_warn = False
# app_limit_list = Sprout.read_all_config()
warn = True
app_limit_graph_data = [1] * Sprout.find_info_length()


# Runs every second, whatever you need!
def process():
    global counter
    counter += 1
    print(counter)
    widget.after(1000, process)
    # check if any of the processes have run out of time.
    # loop through each process and see if the time that they have been running is greater than their limits
    for ii in Sprout.get_listed_running_applications():
        if Sprout.process_uptime(ii) >= Sprout.read_config(ii, 2) and should_warn:
            # Find the process and kill it.
            for jj in psutil.process_iter():
                if jj.name == ii:
                    jj.kill()


in_desktop = False
def expand(): #stuff for the desktop window configuration
    global in_desktop
    global should_warn
    if not in_desktop:
        desktopwindow = customtkinter.CTkToplevel(widget)
        desktopwindow.title('Flourish Desktop')
        desktopwindow.geometry('300x200')


        info_appname = customtkinter.StringVar()
        info_time_limit = customtkinter.StringVar()
        info_check_warn = str(customtkinter.BooleanVar())

        enter_appname = customtkinter.CTkEntry(desktopwindow, placeholder_text='carrot cake', textvariable=info_appname)
        enter_time_limit = customtkinter.CTkEntry(desktopwindow, placeholder_text='breading (s)')
        should_warn = customtkinter.CTkCheckBox(desktopwindow)

        # Imma just print out the different fields of the different inputs for debug purposes
        print('(+) info_appname, info_time_limit, info_check_warn', info_appname, str(info_time_limit), str(info_check_warn))
        # Edit the styles

        #Image Files: Image Stuff

        #Plus Button on New Limit Section
        btn_submit_image = customtkinter.CTkImage(Image.open('res\\Group_327.png'))
        # When the submit button is pressed, append the data into the text file.
        btn_submit = customtkinter.CTkButton(desktopwindow, command=lambda: Sprout.append_application(info_appname, None, info_time_limit, info_check_warn), image=btn_submit_image)

        # flourish_info
        flourish_info = customtkinter.CTkFrame(master=desktopwindow, width=319, height=178, corner_radius=20)
        flourish_info.pack(padx=20, pady=20)


        # name_img = Image.open('path-to-image')
        # name = customtkinter.CTkLabel(master=desktopwindow, image=name_img)
        # name.place(xcoord, ycoord)


        screen_width = desktopwindow.winfo_width()
        screen_height = desktopwindow.winfo_height()

        Rectangle_185_2_img = customtkinter.CTkImage(Image.open('res\\Rectangle_185_2.png'), size=(Image.open('res\\Rectangle_185_2.png').width ,Image.open('res\\Rectangle_185_2.png').height))
        Rectangle_185_2 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_185_2_img)
        Rectangle_185_2.place(x=32, y=29)
        
        Rectangle_182_img = customtkinter.CTkImage(Image.open('res\\Rectangle_182.png'), size=(Image.open('res\\Rectangle_182.png').width, Image.open('res\\Rectangle_182.png').height))
        Rectangle_182 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_182_img)
        Rectangle_182.place(x=58, y=459)

        Rectangle_180_img = customtkinter.CTkImage(Image.open('res\\Rectangle_180.png'), size=(Image.open('res\\Rectangle_180.png').width, Image.open('res\\Rectangle_180.png').height))
        Rectangle_180 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_180_img)
        Rectangle_180.place(x=32, y=353)

        Rectangle_178_img = customtkinter.CTkImage(Image.open('res\\Rectangle_178.png'), size=(Image.open('res\\Rectangle_178.png').width, Image.open('res\\Rectangle_178.png').height))
        Rectangle_178_2 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_178_img)
        Rectangle_178_2.place(x=556, y=629)

        Rectangle_177_img = customtkinter.CTkImage(Image.open('res\\Rectangle_177.png'), size=(Image.open('res\\Rectangle_177.png').width, Image.open('res\\Rectangle_177.png').height))
        Rectangle_177 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_177_img)
        Rectangle_177.place(x=884, y=130)

        Rectangle_139_img = customtkinter.CTkImage(Image.open('res\\Rectangle_139.png'), size=(Image.open('res\\Rectangle_139.png').width, Image.open('res\\Rectangle_139.png').height))
        Rectangle_139 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_139_img)
        Rectangle_139.place(x=419, y=29)

        Rectangle_121_img = customtkinter.CTkImage(Image.open('res\\Rectangle_121.png'), size=(Image.open('res\\Rectangle_121.png').width, Image.open('res\\Rectangle_121.png').height))
        Rectangle_121 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_121_img)
        Rectangle_121.place(x=418, y=489)

        Rectangle_121_2 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_121_img)
        Rectangle_121_2.place(x=593, y=489)

        Rectangle_121_3 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_121_img)
        Rectangle_121_3.place(x=705, y=489)

        Rectangle_16_img = customtkinter.CTkImage(Image.open('res\\Rectangle_16.png'), size=(Image.open('res\\Rectangle_16.png').height, Image.open('res\\Rectangle_16.png').width))
        Rectangle_16 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_16_img)
        Rectangle_16.place(x=880, y=30)

        Rectangle_45_img = customtkinter.CTkImage(Image.open('res\\Rectangle_45.png'), size=(Image.open('res\\Rectangle_45.png').width, Image.open('res\\Rectangle_45.png').height))
        Rectangle_45 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_45_img)
        Rectangle_45.place(x=926, y=389)

        Rectangle_45_2 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_45_img)
        Rectangle_45_2.place(x=926, y=470)

        Rectangle_45_3 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_45_img)
        Rectangle_45_3.place(x=926, y=552)

        Rectangle_45_3 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_45_img)
        Rectangle_45_3.place(x=926, y=635)

        Rectangle_42_img = customtkinter.CTkImage(Image.open('res\\Rectangle_42.png'), size=(Image.open('res\\Rectangle_42.png').width, Image.open('res\\Rectangle_42.png').height))
        Rectangle_42 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_42_img)
        Rectangle_42.place(x=63, y=142)

        Rectangle_37_img = customtkinter.CTkImage(Image.open('res\\Rectangle_37.png'), size=(Image.open('res\\Rectangle_37.png').width, Image.open('res\\Rectangle_37.png').height))
        Rectangle_37 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_37_img)
        Rectangle_37.place(x=430, y=632)

        Rectangle_180_img = customtkinter.CTkImage(Image.open('res\\Rectangle_180.png'), size=(Image.open('res\\Rectangle_180.png').width, Image.open('res\\Rectangle_180.png').height))
        Rectangle_180 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Rectangle_180_img)
        Rectangle_180.place(x=32, y=353)

        Group_327_img = customtkinter.CTkImage(Image.open('res\\Group_327.png'), size=(Image.open('res\\Group_327.png').width, Image.open('res\\Group_327.png').height))
        Group_327 = customtkinter.CTkLabel(master=desktopwindow, text= '', image=Group_327_img)
        Group_327.place(x=32, y=29)
# 


        enter_appname.pack()
        enter_time_limit.pack()
        check_warn.pack()
        btn_submit.pack()


        in_desktop = True


# Main Window & its propteries
# widget stuff below: 
widget = customtkinter.CTk()
customtkinter.set_appearance_mode('dark')

up_frame = customtkinter.CTkFrame(widget)

#bargraph stuff below
bargraph= Figure(figsize=(5,4), dpi=100)
specific_apps = bargraph.add_subplot(111)

graph_x_location = numpy.arange(Sprout.find_info_length())  # the x locations for the groups
spacing = .5

rects1 = specific_apps.bar(graph_x_location, tuple(app_limit_graph_data), spacing)

canvas = FigureCanvasTkAgg(bargraph, master=up_frame)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1)

#button stuff below
button_frame = customtkinter.CTkFrame(widget)

# Add and implement the button that expands to the mainwindow
#Testing if it works
test_image = customtkinter.CTkImage(light_image=Image.open('res\\b9709638-c419-4fb1-976c-20ca8a01a9f3.jpeg'), size=(300,300))
test_image_holder = customtkinter.CTkLabel(up_frame, image=test_image, text="")

btn_expand = customtkinter.CTkButton(master=button_frame, text='//\/\nThis is supposed to be a plant^', command=expand)
up_frame.pack()
button_frame.pack()
test_image_holder.grid(row=0, column=0)
btn_expand.pack()

process()
widget.mainloop()
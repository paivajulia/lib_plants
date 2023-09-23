import tkinter as tk
from PIL import ImageTk, Image
import pyglet
import sqlite3


window_width=500
window_height=600
window_bg="#F0E2EA"
logo_padx=50
logo_pady=(50,0)
font_color="#4F7B4F"

# load custom fonts
pyglet.font.add_file("/home/juliapaiva/Documents/Py_estudo/fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("/home/juliapaiva/Documents/Py_estudo/fonts/Shanti-Regular.ttf")

# initiallize app
root = tk.Tk()
root.title("Plant library")
root.eval("tk::PlaceWindow . center")

#create a frame
frame1 = tk.Frame(root, width=window_width, height=window_height, bg=window_bg)
frame1.grid(row=6, column=4)
frame2 = tk.Frame(root, bg=window_bg)
frame2.grid(row= 6, column=4)
frame3 = tk.Frame(root, bg=window_bg)
frame3.grid(row= 6, column=4)


 # configure the grid
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(2, weight=1)
frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(3, weight=1)


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():

    frame1.tkraise()
    frame1.pack_propagate(False)

    #frame1 widgets
    logo_img=ImageTk.PhotoImage(file="/home/juliapaiva/Documents/Py_estudo/assets/logo_image.png")
    logo_widget = tk.Label(frame1, image = logo_img, bg=window_bg) 
    logo_widget.image=logo_img
    logo_widget.pack(pady=logo_pady, padx=logo_padx)

    tk.Label(frame1,
            text="Choose your plant!",bg=window_bg,
            fg=font_color, 
            font=("Shanti", 14)
            ).pack()

    #button widget
    tk.Button(frame1,
            text="CHOOSE",
            font=("Ubuntu", 20),
            bg="#E4BAD9",
            fg=font_color,
            cursor="hand2",
            activebackground="#FFF8FB",
            activeforeground=font_color,
            command= lambda:load_frame2()
            ).pack(pady=20)
    
def load_frame2():

    clear_widgets(frame1)

    frame2.tkraise()
    frame2.pack_propagate(False)

    maranta_img=ImageTk.PhotoImage(file="/home/juliapaiva/Documents/Py_estudo/assets/logo_image.png")
    maranta_widget = tk.Label(frame2, image = maranta_img, bg=window_bg) 
    maranta_widget.image=maranta_img
    maranta_widget.grid(row=1,column=1, pady = 2)
    tk.Button(frame2,
            text="Maranta",
            font=("Ubuntu", 20),
            bg="#E4BAD9",
            fg=font_color,
            cursor="hand2",
            activebackground="#FFF8FB",
            activeforeground=font_color,
            command= lambda:load_frame3()
            ).grid(row=2,column=1, pady = 2)
    
    hoya_img=ImageTk.PhotoImage(file="/home/juliapaiva/Documents/Py_estudo/assets/logo_image.png")
    hoya_widget = tk.Label(frame2, image = hoya_img, bg=window_bg) 
    hoya_widget.image=hoya_img
    hoya_widget.grid(row=1,column=3, pady = 2)
    tk.Button(frame2,
            text="Hoya",
            font=("Ubuntu", 20),
            bg="#E4BAD9",
            fg=font_color,
            cursor="hand2",
            activebackground="#FFF8FB",
            activeforeground=font_color,
            command= lambda:load_frame4()
            ).grid(row=2,column=3, pady = 2)
    
    peperomia_img=ImageTk.PhotoImage(file="/home/juliapaiva/Documents/Py_estudo/assets/logo_image.png")
    peperomia_widget = tk.Label(frame2, image = peperomia_img, bg=window_bg) 
    peperomia_widget.image=peperomia_img
    peperomia_widget.grid(row=4,column=3, pady = 2)
    tk.Button(frame2,
            text="Peperomia",
            font=("Ubuntu", 20),
            bg="#E4BAD9",
            fg=font_color,
            cursor="hand2",
            activebackground="#FFF8FB",
            activeforeground=font_color,
            command= lambda:load_frame5()
            ).grid(row=5,column=3, pady = 2)

def load_frame3():

    global frame2
    clear_widgets(frame2)

    frame3.tkraise()
    frame3.pack_propagate(False)

    maranta_img=ImageTk.PhotoImage(file="/home/juliapaiva/Documents/Py_estudo/assets/logo_image.png")
    maranta_widget = tk.Label(frame3, image = maranta_img, bg=window_bg) 
    maranta_widget.image=maranta_img
    maranta_widget.grid(row=0,columnspan=4, pady = 2)
    
    tk.Label(frame3,
            text="Maranta",bg=window_bg,
            fg=font_color, 
            font=("Shanti", 25)
            ).grid(row=1,column=0,sticky="s")
    
    connection = sqlite3.connect("/home/juliapaiva/Documents/Py_estudo/plants_new.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Maranta from plants")
    table_records = cursor.fetchall()
    print (table_records)
    

def load_frame4():
    print("Hoya")

def load_frame5():
    print("Peperomia")




load_frame1()


# run app
root.mainloop()
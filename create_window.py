import tkinter as tk
from ChessBoardCorrect import ChessBoardAndCircle
import os
from PIL import ImageTk,Image

chessboard_circle=ChessBoardAndCircle()
chessboard_root_dir=chessboard_circle.chessboard_root_dir
circle_root_dir=chessboard_circle.circle_root_dir


window=tk.Tk()
window.title('CameraCalibrate')
window.geometry('1530x800')

'''
Commands(or functions) and operations targeted at chessboard picture
'''
global cb_dist


def picture_resize(width,height,pil_image):
    factor=0.45
    height_re=int(factor*height)
    width_re=int(factor*width)
    return pil_image.resize((width_re,height_re),Image.ANTIALIAS)


def upload_chess_dist():
    # canvas_dist_cb.delete('all')
    image_dir=os.path.join(chessboard_root_dir, cb_dist)
    image_open=Image.open(image_dir)
    width,height=image_open.size
    image_open_resize=picture_resize(width,height,image_open)
    image_file=ImageTk.PhotoImage(image_open_resize)
    label_distimg_cb.config(image=image_file)
    label_distimg_cb.image=image_file


def undistort_chessboard():
    chessboard_circle.undistort_picture(os.path.join(chessboard_root_dir, cb_dist))
    image_open=Image.open(chessboard_circle.undistort_fname)
    width, height = image_open.size
    image_open_resize = picture_resize(width, height, image_open)
    image_file = ImageTk.PhotoImage(image_open_resize)
    label_undistimg_cb.config(image=image_file)
    label_undistimg_cb.image=image_file


def select_chess_dist():
    global cb_dist
    cb_dist=listbox_cb_dir.get(listbox_cb_dir.curselection())


title=tk.Label(window,text='Camera Calibration and Image Undistortion',bg='green',font=('Arial',20),width=40,height=2)
title.place(x=450,y=20,anchor='nw')
right=tk.Label(window,text='班级：机械1505班\n学号：U201510674\n姓名：杨靖宇',bg='green',font=('宋体',14),width=16,height=6)
right.place(x=680,y=120,anchor='nw')
button_selec_cb= tk.Button(window, text='Press to select chessboard image', width=35, height=2, command=select_chess_dist)
button_selec_cb.place(x=120,y=100,anchor='nw')
button_upload_cb= tk.Button(window, text='Upload distorted chess board image ', width=35, height=2, command=upload_chess_dist)
button_upload_cb.place(x=120,y=160,anchor='nw')
button_undistort_cb= tk.Button(window, text='To undistort image', width=35, height=2, command=undistort_chessboard)
button_undistort_cb.place(x=120,y=220,anchor='nw')

var_chess_dir=tk.StringVar()
var_chess_dir.set(list(chessboard_circle.chessboard_fname))
listbox_cb_dir=tk.Listbox(window,listvariable=var_chess_dir,width=35,height=9)
listbox_cb_dir.place(x=400,y=100,anchor='nw')
label_distimg_cb=tk.Label(window)
label_distimg_cb.place(x=30,y=280,anchor='nw')
label_undistimg_cb=tk.Label(window)
label_undistimg_cb.place(x=400,y=280,anchor='nw')


'''
Commands(or functions) and operations targeted at circle
'''
global circle_dist


def upload_circle_dist():
    image_dir=os.path.join(circle_root_dir, circle_dist)
    image_open=Image.open(image_dir)
    width,height=image_open.size
    image_open_resize=picture_resize(width,height,image_open)
    image_file=ImageTk.PhotoImage(image_open_resize)
    label_distimg_circle.config(image=image_file)
    label_distimg_circle.image=image_file


def undistort_circle():
    chessboard_circle.undistort_picture(os.path.join(circle_root_dir, circle_dist))
    image_open=Image.open(chessboard_circle.undistort_fname)
    width, height = image_open.size
    image_open_resize = picture_resize(width, height, image_open)
    image_file = ImageTk.PhotoImage(image_open_resize)
    label_undistimg_circle.config(image=image_file)
    label_undistimg_circle.image=image_file


def select_circle_dist():
    global circle_dist
    circle_dist=listbox_circle_dir.get(listbox_circle_dir.curselection())


button_selec_circle= tk.Button(window, text='Press to select circle image ', width=35, height=2, command=select_circle_dist)
button_selec_circle.place(x=870,y=100,anchor='nw')
button_upload_circle= tk.Button(window, text='Upload distorted circle image ', width=35, height=2, command=upload_circle_dist)
button_upload_circle.place(x=870,y=160,anchor='nw')
button_undistort_circle= tk.Button(window, text='To undistort image', width=35, height=2, command=undistort_circle)
button_undistort_circle.place(x=870,y=220,anchor='nw')

var_circle_dir=tk.StringVar()
var_circle_dir.set(list(chessboard_circle.circle_fname))
listbox_circle_dir=tk.Listbox(window,listvariable=var_circle_dir,width=35,height=9)
listbox_circle_dir.place(x=1150,y=100,anchor='nw')
label_distimg_circle=tk.Label(window)
label_distimg_circle.place(x=780,y=280,anchor='nw')
label_undistimg_circle=tk.Label(window)
label_undistimg_circle.place(x=1150,y=280,anchor='nw')

window.mainloop()



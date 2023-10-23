from tkinter import *
from tkinter.ttk import Progressbar,Style
import speedtest
from threading import Thread
from queue import Queue

def format_speed(speed):
    return round(speed / (1024 * 1024), 2)

def test(queue):
    std = speedtest.Speedtest().download()
    stu = speedtest.Speedtest().upload()
    queue.put(f" точная скорость скачать: {format_speed(std)} Мб/с,загрузить:{format_speed(stu)} Мб/с")

def main():
    res["text"] = "Измерения скорости интернета в процесе"
    btn["state"] = DISABLED
    
    style = Style()
    style.theme_use('clam')
    style.configure("green.Horizontal.TProgressbar", troughcolor='black', bordercolor='#2f1cad', background='#2f1cad', lightcolor='#2f1cad', darkcolor='black')

    progress = Progressbar(root, length=300, mode='indeterminate',style='green.Horizontal.TProgressbar')
    progress['value'] = 70
    progress.pack(pady=10)
    progress.start(10)
    queue = Queue()
    thread = Thread(target=test, args=(queue,))
    thread.start()
    root.after(100, check_queue, queue, progress)

def check_queue(queue,progress):
    if queue.empty():
        root.after(100, check_queue, queue, progress)
    else:
        res["text"] = queue.get()
        btn["state"] = ACTIVE
        progress.stop()
        progress.destroy()

root = Tk()
root.title("SpeedTest by _sineD_0")
root["bg"] = "#172230"
root.geometry('600x600')


btn = Button(text="Начать проверку скорости",command=main,bg="#172230",font="Arial 15 bold",fg="#2f1cad")
btn.pack(pady=200)
res = Label(text="Ожидание нажатия кнопки",bg="#172230",font="Arial 15 bold",fg="#2f1cad")
res.pack()

root.mainloop()
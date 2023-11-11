import tkinter as tk
from tkinter import ttk
from cLasses import GUItodo
import customtkinter as ck

root = tk.Tk()
root.geometry("400x500")
taskList = []


def onStart():
    global root
    root.title("Todo list")
    mainTitle = tk.Label(root, text="MyTodo List", justify="center")
    mainTitle.pack()
    TaskButton = tk.Button(
        root, text="New task", justify="center", command=generateTask
    ).pack()


def generateTask():
    taskList.append(GUItodo(root, taskList, len(taskList)))
    print(len(taskList))


onStart()
root.mainloop()

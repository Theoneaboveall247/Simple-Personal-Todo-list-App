# CLasses

import datetime as dt
import tkinter as tk


class todo:
    def __init__(self, name="", timed=False):
        self.__name = name
        self.__timed = timed
        self.__isCompleted = False
        self.isPastDue = False
        self.__completionTime = 0

    def setTime(self, time, day, month, year):
        if time == 0:
            time = "235959"  # hour minute second
        if year == 0:
            year = 0
        if month == 0:
            month == dt.datetime.strftime("%H%M%S")
        self.__completionTime = f"{day} {month} {year} {time}"

    def getCompletionTime(self):
        return self.__completionTime

    def getCompletionStatus(self):
        return self.__isCompleted

    def getTimed(self):
        return self.__timed

    def setCompletionStatus(self, bool):
        self.__isCompleted = bool

    def setTimerStatus(self, bool):
        self.__timed = bool

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GUItodo:
    def __init__(self, root, list, ListPos=0):
        self.root = root
        self.entry = tk.Entry(root)
        if ListPos == 0:
            self.entry.pack()
        else:
            pastTodo = list[ListPos - 1]
            pastPosition = pastTodo.getPosition(pastTodo.entry)
            self.entry.place(x=pastPosition.x, y=pastPosition.y + 25)

        self.entry.insert(0, "Make a todo")
        self.entry.bind("<Return>", self.makeTodo)

    def getPosition(self, widget):
        x = widget.winfo_x()
        y = widget.winfo_y()
        return Vector(x, y)

    def makeTodo(self, event=None):
        self.todo = todo(self.entry.get())
        entryPosition = self.getPosition(self.entry)
        self.checked = tk.IntVar()
        self.checkBox = tk.Checkbutton(
            self.root,
            variable=self.checked,
            onvalue=1,
            offvalue=0,
            command=self.complete,
        )
        self.checkBox.place(x=entryPosition.x - 25, y=entryPosition.y - 2.5)
        self.todoLabel = tk.Label(self.root, text=self.entry.get())
        self.todoLabel.place(x=entryPosition.x, y=entryPosition.y)
        self.entry.pack_forget()
        self.entry.place_forget()

    def complete(self):
        if self.checked.get() == 1:
            self.todoLabel.config(text=self.todoLabel.cget("text") + " (completed)")
        else:
            self.todoLabel.config(text=self.todo.getName())

    def Todo(self):
        return self.todo

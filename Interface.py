from tkinter import *
import tkinter.ttk as ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Functions import *
from Methods import *
import matplotlib.pyplot as plt



def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Root(Tk):
    def __init__(self):
        self.method = None
        super(Root, self).__init__()
        self.title("Лаборатоная работа 4")
        self.minsize(640, 400)
        nb = ttk.Notebook(self)
        self.answer_label = Label(self, text="Здесь появится ответ")
        self.answer_label.pack()
        validation = (self.register(self.on_validate), '%P')
        validation_for_dots = (self.register(self.on_validate_for_dot), '%P')
        nb.pack(fill='both', expand='yes')
        child = ttk.Frame(self)
        method_label = Label(child, text="Интерполяция многочленом Лагранжа")
        method_label.pack()
        equation_label = Label(child, text="Выберите уравнение (интервал для каждого уравнения от 0 до 10 пи:")
        equation_label.pack()
        self.var = IntVar()
        self.var.set(0)
        equation1 = Radiobutton(child, text="sinx", variable=self.var, value=0)
        equation1.pack()
        equation2 = Radiobutton(child, text="ln(x+1)", variable=self.var, value=1)
        equation2.pack()
        equation3 = Radiobutton(child, text="sqrtx", variable=self.var, value=2)
        equation3.pack()
        equation4 = Radiobutton(child, text="sin6x*cosx", variable=self.var, value=3)
        equation4.pack()
        dots_label = Label(child, text="Выберите набор точек: ")
        dots_label.pack()
        self.var_for_dots = IntVar()
        self.var_for_dots.set(0)
        dots1 = Radiobutton(child, text="3 точки", variable=self.var_for_dots, value=3)
        dots1.pack()
        dots2 = Radiobutton(child, text="8 точек", variable=self.var_for_dots, value=8)
        dots2.pack()
        dots3 = Radiobutton(child, text="12 точек", variable=self.var_for_dots, value=12)
        dots3.pack()
        dots4 = Radiobutton(child, text="31 точек", variable=self.var_for_dots, value=31)
        dots4.pack()

        self.dot = StringVar()
        dot_label = Label(child, text="Изменить значение точки (№):")
        dot_label.pack()
        dot_entry = ttk.Entry(child, textvariable=self.dot, validate="key",  validatecommand=validation_for_dots)
        dot_entry.pack()
        button_for_dot = Button(child, text="Показать значение", command=self.show_value)
        button_for_dot.pack()
        self.old_dot_label = Label(child, text="")
        self.old_dot_label.pack()
        self.new_dot = StringVar()
        dot_new_label = Label(child, text="Новое значение Y:")
        dot_new_label.pack()
        new_dot_entry = ttk.Entry(child, textvariable=self.new_dot, validate="key",  validatecommand=validation)
        new_dot_entry.pack()
        button = Button(child, text="Посчитать", command=self.do_lagrange)
        button.pack()
        nb.add(child, text='Интерполяция')

    def show_value(self):
        if self.var.get() == 0:
            function = f
        elif self.var.get() == 1:
            function = g
        elif self.var.get() == 2:
            function = z
        else:
            function = s
        self.method = Interpolation(self.var_for_dots.get(), function)
        y = self.method.get_value(int(self.dot.get()))
        self.old_dot_label.config(text="Значение "+str(y))

    def on_validate(self, P):
        return is_digit(P)

    def on_validate_for_dot(self, P):
        return is_digit(P) and (0 <= float(P) < self.var_for_dots.get())

    def do_lagrange(self):
        if self.var.get() == 0:
            function = f
        elif self.var.get() == 1:
            function = g
        elif self.var.get() == 2:
            function = z
        else:
            function = s
        if self.method is None:
            self.method = Interpolation(self.var_for_dots.get(), function)
        elif (self.method.count_of_dots != self.var_for_dots.get()) or (self.method.function != function):
            self.method = Interpolation(self.var_for_dots.get(), function)

        if self.new_dot.get() != "":
            self.method.set_value(int(self.dot.get()), float(self.new_dot.get()))

        plt.title("График")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        array = self.method.get_dots_for_function()
        x = [array[i][0] for i in range(len(array))]
        y = [array[i][1] for i in range(len(array))]
        plt.plot(x, y, color='#008B8B', label='результат')
        plt.plot(x,  [function(i) for i in x], color="#1E90FF", label='функция')
        array_with_dots = self.method.array_with_dots
        for i in range(len(array_with_dots)):
            plt.scatter(array_with_dots[i][0], array_with_dots[i][1], color='red', s=20, marker='o')
        plt.legend()
        plt.show()





root = Root()
root.mainloop()
import customtkinter
from tkinter import ttk
class Solver(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#fbf2fb")
        self.button = customtkinter.CTkButton(self, text="Решить задачу", command=self.solve)
        self.button.pack()

    def solve(self):
        print("Решение запущено")
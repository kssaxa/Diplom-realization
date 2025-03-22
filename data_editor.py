import customtkinter
from database import add_definition, get_definitions

class DataEditor(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#fbf2fb")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Введите определение")
        self.entry.pack()
        self.button = customtkinter.CTkButton(self, text="Добавить", command=self.add_definition)
        self.button.pack()

    def add_definition(self):
        definition = self.entry.get()
        if definition:
            add_definition("Множество", definition)
            self.entry.delete(0, "end")
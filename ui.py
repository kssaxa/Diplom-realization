import customtkinter
from knowledge_editor import KnowledgeEditor
from data_editor import DataEditor
from solver import Solver


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #self.title("Редактор знаний")
        #self.geometry("1200x800")
        #self.configure(fg_color="#ffffff")

        self.knowledge_editor = KnowledgeEditor(self)
        self.data_editor = DataEditor(self)
        self.solver = Solver(self)

        self.knowledge_editor.pack(padx=20, pady=10)
        self.data_editor.pack(padx=20, pady=10)
        self.solver.pack(padx=20, pady=10)

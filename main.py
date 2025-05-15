import customtkinter
from knowledge_editor import KnowledgeEditor
from data_editor import DataEditor
from solver import Solver
from database import init_db, init_db_data_editor


init_db()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Редактор знаний")
        self.geometry("1200x800")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")
        self.configure(fg_color="#ffffff")

        self.create_left_frame()

        self.knowledge_editor = KnowledgeEditor(self)
        self.data_editor = DataEditor(self)
        self.solver = Solver(self)

        self.show_knowledge_editor()

    def create_left_frame(self):
        
        self.frame_left = customtkinter.CTkFrame(self, fg_color="#fbf2fb", width=220)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)

        self.btn_knowledge = customtkinter.CTkButton(
            self.frame_left,
            text="Редактор знаний",
            command=self.show_knowledge_editor,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.btn_knowledge.pack(padx=20, pady=10)

        self.btn_data = customtkinter.CTkButton(
            self.frame_left,
            text="Редактор данных",
            command=self.show_data_editor,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.btn_data.pack(padx=20, pady=10)

        self.btn_solver = customtkinter.CTkButton(
            self.frame_left,
            text="Решатель задач",
            command=self.show_solver,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.btn_solver.pack(padx=20, pady=10)

    def show_knowledge_editor(self):
        self.data_editor.hide()
        self.solver.hide()
        self.knowledge_editor.show()

    def show_data_editor(self):
        self.knowledge_editor.hide()
        self.solver.hide()
        self.data_editor.show()

    def show_solver(self):
        self.knowledge_editor.hide()
        self.data_editor.hide()
        self.solver.show()


if __name__ == "__main__":
    init_db_data_editor()

    app = App()
    app.mainloop()

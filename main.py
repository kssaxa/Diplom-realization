import customtkinter
from knowledge_editor import KnowledgeEditor
from data_editor import DataEditor
from solver import Solver
from database import init_db, init_db_data_editor


init_db()

class App(customtkinter.CTk):
    def __init__(self, role="user", username="user"):
        super().__init__()
        self.role = role
        self.username = username
        self.title(f"Редактор знаний - {username} ({role})")
        self.geometry("1200x800")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")
        self.configure(fg_color="#ffffff")

        self.create_left_frame()

        # Инициализируем переменные для редакторов (создаем их только при необходимости)
        self.knowledge_editor = None
        self.data_editor = None
        self.solver = None

        # Показываем редактор знаний по умолчанию
        self.show_knowledge_editor()

    def create_left_frame(self):
        
        self.frame_left = customtkinter.CTkFrame(self, fg_color="#fbf2fb", width=220)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)

        # Информация о пользователе
        self.user_info = customtkinter.CTkLabel(
            self.frame_left,
            text=f"👤 {self.username}\n🔑 {self.role}",
            font=("Arial", 12, "bold"),
            text_color="#FF007F"
        )
        self.user_info.pack(padx=20, pady=(20, 10))

        self.btn_knowledge = customtkinter.CTkButton(
            self.frame_left,
            text="Редактор знаний",
            command=self.show_knowledge_editor,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.btn_knowledge.pack(padx=20, pady=10)

        # Если пользователь не админ, показываем предупреждение для редактора знаний
        if self.role != "admin":
            self.knowledge_warning = customtkinter.CTkLabel(
                self.frame_left,
                text="⚠️ Только просмотр",
                font=("Arial", 10),
                text_color="orange"
            )
            self.knowledge_warning.pack(padx=20, pady=(0, 10))

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

        # Кнопка выхода
        self.btn_logout = customtkinter.CTkButton(
            self.frame_left,
            text="Выйти",
            command=self.logout,
            fg_color="#FF6B6B",
            text_color="white"
        )
        self.btn_logout.pack(padx=20, pady=(40, 10))

    def logout(self):
        self.destroy()
        from auth import AuthScreen
        auth = AuthScreen()
        auth.mainloop()

    def show_knowledge_editor(self):
        # Создаем редактор знаний только при первом обращении
        if self.knowledge_editor is None:
            if self.role == "admin":
                self.knowledge_editor = KnowledgeEditor(self)
            else:
                self.knowledge_editor = KnowledgeEditor(self, readonly=True)
        
        # Скрываем другие редакторы
        if self.data_editor:
            self.data_editor.hide()
        if self.solver:
            self.solver.hide()
        
        # Показываем редактор знаний
        self.knowledge_editor.show()

    def show_data_editor(self):
        # Создаем редактор данных только при первом обращении
        if self.data_editor is None:
            self.data_editor = DataEditor(self)
        
        # Скрываем другие редакторы
        if self.knowledge_editor:
            self.knowledge_editor.hide()
        if self.solver:
            self.solver.hide()
        
        # Показываем редактор данных
        self.data_editor.show()

    def show_solver(self):
        # Создаем решатель задач только при первом обращении
        if self.solver is None:
            self.solver = Solver(self)
        
        # Скрываем другие редакторы
        if self.knowledge_editor:
            self.knowledge_editor.hide()
        if self.data_editor:
            self.data_editor.hide()
        
        # Показываем решатель задач
        self.solver.show()


if __name__ == "__main__":
    init_db_data_editor()

    # Запускаем окно авторизации вместо прямого создания приложения
    from auth import AuthScreen
    auth = AuthScreen()
    auth.mainloop()
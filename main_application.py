#!/usr/bin/env python3
"""
Главное окно приложения с системой ролей
"""

import customtkinter as ctk
from auth_system import AuthSystem
from login_window import LoginWindow
from knowledge_editor import KnowledgeEditor
from data_editor import DataEditor
from solver import Solver
import os

class MainApplication:
    def __init__(self):
        self.auth_system = AuthSystem()
        self.current_user = None
        
        # Сначала показываем окно входа
        self.show_login()
        
        if not self.auth_system.is_authenticated():
            print("❌ Вход не выполнен. Приложение завершается.")
            return
        
        # Создаем главное окно
        self.create_main_window()
    
    def show_login(self):
        """Показывает окно входа"""
        login_window = LoginWindow()
        success, user_data = login_window.run()
        
        if success:
            self.current_user = user_data
            print(f"✅ Вход выполнен: {user_data['username']} ({user_data['role']})")
        else:
            print("❌ Вход не выполнен")
    
    def create_main_window(self):
        """Создает главное окно приложения"""
        self.window = ctk.CTk()
        self.window.title("Система управления знаниями")
        self.window.geometry("1200x800")
        
        # Центрируем окно
        self.center_window()
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Запускаем главный цикл
        self.window.mainloop()
    
    def center_window(self):
        """Центрирует окно на экране"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        # Главный контейнер
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Верхняя панель с информацией о пользователе
        self.create_header(main_frame)
        
        # Создаем вкладки
        self.create_tabs(main_frame)
    
    def create_header(self, parent):
        """Создает заголовок с информацией о пользователе"""
        header_frame = ctk.CTkFrame(parent)
        header_frame.pack(fill="x", padx=10, pady=(10, 5))
        
        # Информация о пользователе
        user_info = f"👤 {self.current_user['username']} ({self.current_user['role']})"
        user_label = ctk.CTkLabel(
            header_frame, 
            text=user_info,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        user_label.pack(side="left", padx=20, pady=10)
        
        # Кнопка выхода
        logout_button = ctk.CTkButton(
            header_frame,
            text="Выйти",
            command=self.logout,
            width=100
        )
        logout_button.pack(side="right", padx=20, pady=10)
    
    def create_tabs(self, parent):
        """Создает вкладки приложения"""
        # Создаем notebook для вкладок
        self.tabview = ctk.CTkTabview(parent)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Инициализируем переменные для редакторов
        self.data_editor = None
        self.knowledge_editor = None
        self.task_solver = None
        self.data_viewer = None
        
        # Вкладка "Редактор данных" (доступна всем)
        self.data_tab = self.tabview.add("📊 Редактор данных")
        self.tabview.tab("📊 Редактор данных").bind("<Button-1>", lambda e: self.on_data_tab_click())
        
        # Вкладка "Генерация интерфейсов" (доступна всем)
        self.interface_tab = self.tabview.add("🌐 Генерация интерфейсов")
        self.tabview.tab("🌐 Генерация интерфейсов").bind("<Button-1>", lambda e: self.on_interface_tab_click())
        
        # Вкладка "Редактор знаний" (только для админа)
        if self.auth_system.can_access_knowledge_editor():
            self.knowledge_tab = self.tabview.add("🧠 Редактор знаний")
            self.tabview.tab("🧠 Редактор знаний").bind("<Button-1>", lambda e: self.on_knowledge_tab_click())
        
        # Вкладка "Просмотр данных" (доступна всем, но только для просмотра)
        self.view_tab = self.tabview.add("👁️ Просмотр данных")
        self.tabview.tab("👁️ Просмотр данных").bind("<Button-1>", lambda e: self.on_view_tab_click())
    
    def on_data_tab_click(self):
        """Обработчик клика по вкладке редактора данных"""
        if self.data_editor is None:
            self.create_data_editor_tab()
    
    def on_interface_tab_click(self):
        """Обработчик клика по вкладке генерации интерфейсов"""
        if self.task_solver is None:
            self.create_interface_generator_tab()
    
    def on_knowledge_tab_click(self):
        """Обработчик клика по вкладке редактора знаний"""
        if self.knowledge_editor is None:
            self.create_knowledge_editor_tab()
    
    def on_view_tab_click(self):
        """Обработчик клика по вкладке просмотра данных"""
        if self.data_viewer is None:
            self.create_data_viewer_tab()
    
    def create_data_editor_tab(self):
        """Создает вкладку редактора данных"""
        # Создаем редактор данных
        # Обычные пользователи могут редактировать данные, админы тоже
        self.data_editor = DataEditor(self.data_tab, readonly=False)
    
    def create_interface_generator_tab(self):
        """Создает вкладку генерации интерфейсов"""
        # Создаем решатель задач (который содержит генератор интерфейсов)
        self.task_solver = Solver(self.interface_tab)
    
    def create_knowledge_editor_tab(self):
        """Создает вкладку редактора знаний"""
        # Создаем редактор знаний
        self.knowledge_editor = KnowledgeEditor(self.knowledge_tab)
    
    def create_data_viewer_tab(self):
        """Создает вкладку просмотра данных"""
        # Создаем редактор данных в режиме только просмотра
        self.data_viewer = DataEditor(self.view_tab, readonly=True)
        
        # Показываем предупреждение о режиме просмотра
        self.show_readonly_warning(self.view_tab)
    
    def show_readonly_warning(self, parent):
        """Показывает предупреждение о режиме только просмотра"""
        warning_frame = ctk.CTkFrame(parent)
        warning_frame.pack(fill="x", padx=10, pady=5)
        
        warning_label = ctk.CTkLabel(
            warning_frame,
            text="⚠️ Режим просмотра: изменения недоступны",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="orange"
        )
        warning_label.pack(pady=10)
    
    def logout(self):
        """Выполняет выход пользователя"""
        self.auth_system.logout()
        self.window.destroy()
        
        # Перезапускаем приложение
        self.__init__()

def main():
    """Главная функция"""
    print("🚀 Запуск системы управления знаниями")
    print("=" * 50)
    
    # Проверяем наличие необходимых файлов
    required_files = [
        "knowledge_editor.py",
        "data_editor.py", 
        "solver.py",
        "html_generator.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Отсутствуют необходимые файлы: {missing_files}")
        return
    
    print("✅ Все необходимые файлы найдены")
    
    # Запускаем приложение
    app = MainApplication()

if __name__ == "__main__":
    main() 
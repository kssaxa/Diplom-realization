#!/usr/bin/env python3
"""
Окно входа в систему
"""

import customtkinter as ctk
from auth_system import AuthSystem

class LoginWindow:
    def __init__(self):
        self.auth_system = AuthSystem()
        self.login_successful = False
        self.user_data = None
        
        # Настройка окна
        self.window = ctk.CTk()
        self.window.title("Вход в систему")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # Центрируем окно
        self.center_window()
        
        # Создаем интерфейс
        self.create_widgets()
        
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
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Заголовок
        title_label = ctk.CTkLabel(
            main_frame, 
            text="Вход в систему", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(20, 30))
        
        # Форма входа
        form_frame = ctk.CTkFrame(main_frame)
        form_frame.pack(fill="x", padx=20, pady=10)
        
        # Поле имени пользователя
        username_label = ctk.CTkLabel(form_frame, text="Имя пользователя:")
        username_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.username_entry = ctk.CTkEntry(
            form_frame, 
            placeholder_text="Введите имя пользователя",
            width=300
        )
        self.username_entry.pack(padx=10, pady=(0, 15))
        
        # Поле пароля
        password_label = ctk.CTkLabel(form_frame, text="Пароль:")
        password_label.pack(anchor="w", padx=10, pady=(0, 5))
        
        self.password_entry = ctk.CTkEntry(
            form_frame, 
            placeholder_text="Введите пароль",
            show="*",
            width=300
        )
        self.password_entry.pack(padx=10, pady=(0, 20))
        
        # Кнопка входа
        self.login_button = ctk.CTkButton(
            form_frame,
            text="Войти",
            command=self.login,
            width=200,
            height=40
        )
        self.login_button.pack(pady=(0, 20))
        
        # Кнопка Enter для быстрого входа
        self.window.bind('<Return>', lambda event: self.login())
        
        # Информация о пользователях
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(fill="x", padx=20, pady=10)
        
        info_label = ctk.CTkLabel(
            info_frame, 
            text="Доступные пользователи:\n👤 Администратор: admin / admn\n👤 Пользователь: user / user",
            font=ctk.CTkFont(size=12)
        )
        info_label.pack(pady=10)
        
        # Статус
        self.status_label = ctk.CTkLabel(
            main_frame, 
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=10)
    
    def login(self):
        """Выполняет вход пользователя"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            self.show_status("❌ Введите имя пользователя и пароль", "error")
            return
        
        # Выполняем вход
        if self.auth_system.login(username, password):
            self.user_data = self.auth_system.get_current_user()
            self.login_successful = True
            self.show_status("✅ Вход выполнен успешно!", "success")
            
            # Закрываем окно через небольшую задержку
            self.window.after(1000, self.window.destroy)
        else:
            self.show_status("❌ Неверное имя пользователя или пароль", "error")
    
    def show_status(self, message, status_type="info"):
        """Показывает статусное сообщение"""
        if status_type == "error":
            self.status_label.configure(text=message, text_color="red")
        elif status_type == "success":
            self.status_label.configure(text=message, text_color="green")
        else:
            self.status_label.configure(text=message, text_color="white")
    
    def run(self):
        """Запускает окно входа"""
        self.window.mainloop()
        return self.login_successful, self.user_data

def main():
    """Тестовая функция"""
    login_window = LoginWindow()
    success, user_data = login_window.run()
    
    if success:
        print(f"✅ Вход выполнен: {user_data}")
    else:
        print("❌ Вход не выполнен")

if __name__ == "__main__":
    main() 
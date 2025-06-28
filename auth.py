import customtkinter
import sqlite3

class AuthScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.geometry("400x300")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")
        self.configure(fg_color="#ffffff")

        # Создаем центральный фрейм
        self.frame = customtkinter.CTkFrame(self, fg_color="#fbf2fb")
        self.frame.pack(expand=True, padx=20, pady=20)

        # Заголовок
        self.label = customtkinter.CTkLabel(
            self.frame,
            text="Вход в систему",
            font=("Arial", 20, "bold"),
            text_color="#FF007F"
        )
        self.label.pack(pady=20)

        # Поле для логина
        self.login_entry = customtkinter.CTkEntry(
            self.frame,
            placeholder_text="Введите логин",
            width=200,
            height=35
        )
        self.login_entry.pack(pady=10)

        # Поле для пароля
        self.password_entry = customtkinter.CTkEntry(
            self.frame,
            placeholder_text="Введите пароль",
            show="*",
            width=200,
            height=35
        )
        self.password_entry.pack(pady=10)

        # Кнопка входа
        self.login_button = customtkinter.CTkButton(
            self.frame,
            text="Войти",
            command=self.login,
            fg_color="#FFD1DC",
            text_color="#FF007F",
            width=200,
            height=35
        )
        self.login_button.pack(pady=20)

        # Метка для сообщений об ошибках
        self.error_label = customtkinter.CTkLabel(
            self.frame,
            text="",
            text_color="red"
        )
        self.error_label.pack(pady=10)

    def login(self):
        username = self.login_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.error_label.configure(text="Введите логин и пароль")
            return

        # Здесь можно добавить проверку логина и пароля через БД
        if self.check_credentials(username, password):
            self.destroy()  # Закрываем окно авторизации
            from main import App  # Импортируем главное окно
            app = App()
            app.mainloop()
        else:
            self.error_label.configure(text="Неверный логин или пароль")

    def check_credentials(self, username, password):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()
        return user is not None

if __name__ == "__main__":
    auth = AuthScreen()
    auth.mainloop() 
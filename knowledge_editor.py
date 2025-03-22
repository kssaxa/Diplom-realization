import customtkinter
from database import add_set, get_sets

class KnowledgeEditor(customtkinter.CTkFrame):
     """Класс приложения"""

    def __init__(self):
        """Инициализация объектов интерфейса"""
        super().__init__()

        self.title("Редактор знаний")
        self.geometry("1200x800")

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.configure(fg_color="#ffffff")

        # Создание фреймов
        self.frame_left = customtkinter.CTkFrame(self, fg_color="#fbf2fb", width=220)
        self.frame_middle = customtkinter.CTkFrame(self, fg_color="#fbf2fb")
        self.frame_right = customtkinter.CTkFrame(self, fg_color="#fbf2fb", width=400)

        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)
        self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
        self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        # Элементы для левого фрейма
        self.knowledge_editor = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=[
                "Название множеств",
                "Определение множеств",
                "Интерфейсные элементы",
                "Свойства интерфейсных элементов",
                "Область значений свойств",
                "Определение свойств элемента",
                "Альтернатива для множества",
                "Группа элементов",
            ],
            command=self.optionmenu_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.knowledge_editor.pack(padx=20, pady=10)
        self.knowledge_editor.set("Редактор знаний")

        self.button_data_editor = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=[
                "Онтологии",
                "Термины онтологии",
                "Сорта онтологии",
                "Экранные формы",
                "Определение экранной формы",
            ],
            command=self.optionmenu_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.button_data_editor.pack(padx=20, pady=10)
        self.button_data_editor.set("Редактор данных")

        self.button_solver = customtkinter.CTkButton(
            self.frame_left,
            text="Решатель задач",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.button_solver.pack(padx=20, pady=10)

        self.name_of_sets = customtkinter.CTkButton(
            self.frame_middle,
            text="Название множеств",
            command=self.show_sets_interface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.definition_of_sets = customtkinter.CTkButton(
            self.frame_middle,
            text="Определение множеств",
            command=self.show_definitions_interface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.interface_elements = customtkinter.CTkButton(
            self.frame_middle,
            text="Интерфейсные элементы",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.properties_of_elements = customtkinter.CTkButton(
            self.frame_middle,
            text="Свойства интерфейсных элементов",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.property_range = customtkinter.CTkButton(
            self.frame_middle,
            text="Область значений свойств",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.defining_element_properties = customtkinter.CTkButton(
            self.frame_middle,
            text="Определение свойств элемента",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.alternatives_for_sets = customtkinter.CTkButton(
            self.frame_middle,
            text="Альтернатива для множества",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.group_of_elements = customtkinter.CTkButton(
            self.frame_middle,
            text="Группа элементов",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.name_of_sets.grid(row=0, column=0, padx=10, pady=10)
        self.definition_of_sets.grid(row=0, column=1, padx=10, pady=10)
        self.interface_elements.grid(row=0, column=2, padx=10, pady=10)
        self.properties_of_elements.grid(row=0, column=3, padx=10, pady=10)
        self.property_range.grid(row=1, column=0, padx=10, pady=10)
        self.defining_element_properties.grid(row=1, column=1, padx=10, pady=10)
        self.alternatives_for_sets.grid(row=1, column=2, padx=10, pady=10)
        self.group_of_elements.grid(row=1, column=3, padx=10, pady=10)

    def clear_right_frame(self):
        """Очищает правый фрейм перед загрузкой нового интерфейса"""
        for widget in self.frame_right.winfo_children():
            widget.destroy()

    def show_sets_interface(self, choice="Название множеств"):
        """Отображает элементы для управления таблицей 'Название множеств'"""
        self.clear_right_frame()

        # Заголовок
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        # Поле ввода + кнопка
        self.entry = customtkinter.CTkEntry(
            self.frame_right, placeholder_text="Введите название множества", width=280
        )
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button_add = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_set
        )
        self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Таблица
        self.tree = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Название", text="Название множества")
        self.tree.column("ID", width=50)
        self.tree.column("Название", width=250)

        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_sets()

    def show_definitions_interface(self):
        """Отображает элементы для управления таблицей 'Определение множеств'"""
        self.clear_right_frame()

        # Заголовок
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text="Определение множеств", font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        # Выпадающий список
        self.sets_list = customtkinter.CTkOptionMenu(
            self.frame_right, values=self.get_sets_list()
        )
        self.sets_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Поле ввода
        self.entry_definition = customtkinter.CTkEntry(
            self.frame_right,
            placeholder_text="Введите обозначение множества",
            width=280,
        )
        self.entry_definition.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Кнопка "Добавить"
        self.button_add_definition = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_definition
        )
        self.button_add_definition.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Таблица для отображения данных
        self.tree_definitions = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Множество", "Определение"),
            show="headings",
        )
        self.tree_definitions.heading("ID", text="ID")
        self.tree_definitions.heading("Множество", text="Множество")
        self.tree_definitions.heading("Определение", text="Определение")
        self.tree_definitions.column("ID", width=50)
        self.tree_definitions.column("Множество", width=150)
        self.tree_definitions.column("Определение", width=250)

        self.tree_definitions.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        # Загрузка данных
        self.load_definitions()

    def add_set(self):
        """Добавляет множество в базу данных"""
        name = self.entry.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO sets (name) VALUES (?)", (name,))
                conn.commit()
                self.entry.delete(0, "end")
                self.load_sets()
            except sqlite3.IntegrityError:
                print("Такое множество уже существует")
            conn.close()

    def add_definition(self):
        """Добавляет определение множества в базу данных"""
        set_name = self.sets_list.get()
        definition = self.entry_definition.get()

        if set_name and definition:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO definitions (set_name, definition) VALUES (?, ?)",
                    (set_name, definition),
                )
                conn.commit()
                self.entry_definition.delete(0, "end")
                self.load_definitions()
            except sqlite3.IntegrityError:
                print("Такое определение уже существует")
            conn.close()

    def load_sets(self):
        """Загружает данные в таблицу"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sets")
        rows = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)

    def load_definitions(self):
        """Загружает определения множеств в таблицу"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM definitions")
        rows = cursor.fetchall()
        conn.close()

        self.tree_definitions.delete(*self.tree_definitions.get_children())
        for row in rows:
            self.tree_definitions.insert("", "end", values=row)

    def get_sets_list(self):
        """Возвращает список названий множеств из базы"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sets")
        sets = [row[0] for row in cursor.fetchall()]
        conn.close()
        return sets

    def optionmenu_callback(self, choice):
        """Вызывает нужный интерфейс при выборе из списка"""
        if choice == "Определение множеств":
            self.show_definitions_interface()
        if choice == "Название множеств":
            self.show_sets_interface(choice)

    def button_callback(self):
        """Пример обработчика кнопки"""
        print("Кнопка работает")


def init_db():
    """Создаёт базу данных и таблицы, если их нет"""
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()

    # Таблица с множествами
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )

    # Таблица с определениями множеств
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_name TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_name) REFERENCES sets (name) ON DELETE CASCADE
        )"""
    )
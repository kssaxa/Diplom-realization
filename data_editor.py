import sqlite3
from tkinter import ttk
import customtkinter


class DataEditor:
    def __init__(self, master):
        self.master = master
        self.visible = False

        # Создание фреймов
        # self.frame_left = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=220)
        self.frame_middle = customtkinter.CTkFrame(master, fg_color="#fbf2fb")
        self.frame_right = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=400)

        # self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)
        self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
        self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        # По умолчанию скрываем
        self.hide()

        self.ontologies = customtkinter.CTkButton(
            self.frame_middle,
            text="Онтологии",
            command=self.show_ontology_interface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.ontology_terms = customtkinter.CTkButton(
            self.frame_middle,
            text="Термины онтологии",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.ontology_sorts = customtkinter.CTkButton(
            self.frame_middle,
            text="Сорта онтологии",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.window_forms = customtkinter.CTkButton(
            self.frame_middle,
            text="Экранные формы",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.definition_window_forms = customtkinter.CTkButton(
            self.frame_middle,
            text="Определение экранной формы",
            command=self.button_callback,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )

        
        self.ontologies.grid(row=0, column=0, padx=10, pady=10)
        self.ontology_terms.grid(row=0, column=1, padx=10, pady=10)
        self.ontology_sorts.grid(row=0, column=2, padx=10, pady=10)
        self.window_forms.grid(row=0, column=3, padx=10, pady=10)
        self.definition_window_forms.grid(row=0, column=4, padx=10, pady=10)

    def show(self):
        """Показывает все фреймы редактора данных"""
        if not self.visible:
            # self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)
            self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
            self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

            self.master.grid_rowconfigure(1, weight=1)
            self.master.grid_columnconfigure(1, weight=1)
            self.frame_right.grid_rowconfigure(2, weight=1)
            self.frame_right.grid_columnconfigure(0, weight=1)

            self.visible = True

    def hide(self):
        """Скрывает все фреймы редактора данных"""
        if self.visible:
            # self.frame_left.grid_remove()
            self.frame_middle.grid_remove()
            self.frame_right.grid_remove()
            self.visible = False

    def clear_right_frame(self):
        for widget in self.frame_right.winfo_children():
            widget.destroy()

    def show_ontology_interface(self, choice="Онтологии"):

        self.clear_right_frame()

        
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        self.entry = customtkinter.CTkEntry(
            self.frame_right, placeholder_text="Введите название онтологии", width=280
        )
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button_add = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_ontology
        )
        self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        
        self.tree = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Название", text="Название онтологии")
        self.tree.column("ID", width=50)
        self.tree.column("Название", width=250)

        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_ontology()

    def load_ontology(self):
        name = self.entry.get()
        if name:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO ontologies (name) VALUES (?)", (name,))
                conn.commit()
                self.entry.delete(0, "end")
                self.load_sets()
            except sqlite3.IntegrityError:
                print("Такое онтология уже существует")
            conn.close()

    def add_ontology(self):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ontologies")
        rows = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)

    def button_callback(self):
        """Пример обработчика кнопки"""
        print("Кнопка работает")

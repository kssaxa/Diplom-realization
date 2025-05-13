import sqlite3
from tkinter import ttk
import customtkinter


class DataEditor:
    def button_callback(self):

        print("Кнопка работает")

    def __init__(self, master):
        self.master = master
        self.visible = False

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
            command=self.show_ontology_terms_interface ,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.ontology_sorts = customtkinter.CTkButton(
            self.frame_middle,
            text="Сорта онтологии",
            command=self.show_ontology_sorts_interface,
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

        self.load_ontology_data()

    def add_ontology(self):
        name = self.entry.get()
        if name:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO ontologies (name) VALUES (?)", (name,))
                conn.commit()
                self.entry.delete(0, "end")
                self.load_ontology_data()
            except sqlite3.IntegrityError:
                print("Такое онтология уже существует")
            conn.close()

    def load_ontology_data(self):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ontologies")
        rows = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)

    def show_ontology_terms_interface(self):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text="Термины онтологии", font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        self.ontology_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_ontology_list(),
            command=self.update_terms_list
        )
        self.ontology_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

       
        ontologies = self.get_ontology_list()
        if ontologies:
            self.ontology_list.set(ontologies[0])
            initial_terms = self.get_terms_for_ontology(ontologies[0])
        else:
            initial_terms = ["Нет онтологий"]

        self.term_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=initial_terms,
            command=self.on_term_selected
        )
        self.term_list.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.button_add_term = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_ontology_term
        )
        self.button_add_term.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        self.tree_terms = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Онтология", "Термин"),
            show="headings",
        )
        self.tree_terms.heading("ID", text="ID")
        self.tree_terms.heading("Онтология", text="Онтология")
        self.tree_terms.heading("Термин", text="Термин")
        self.tree_terms.column("ID", width=50)
        self.tree_terms.column("Онтология", width=150)
        self.tree_terms.column("Термин", width=250)

        self.tree_terms.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_ontology_terms()

    def add_ontology_term(self):

        ontology = self.ontology_list.get()
        term = self.term_list.get()

        if ontology and term:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO ontology_terms (ontology_name, term) VALUES (?, ?)",
                    (ontology, term),
                )
                conn.commit()
                self.term_list.delete(0, "end")
                self.load_ontology_terms()
            except sqlite3.IntegrityError:
                print("Такой термин уже существует")
            conn.close()

    def load_ontology_terms(self):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ontology_terms")
        rows = cursor.fetchall()
        conn.close()
        self.tree_terms.delete(*self.tree_terms.get_children())
        for row in rows:
            self.tree_terms.insert("", "end", values=row)

    def get_ontology_list(self):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM ontologies")
        ontologies = [row[0] for row in cursor.fetchall()]
        conn.close()
        return ontologies

    def show_ontology_sorts_interface(self):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text="Сорта онтологии", font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w"
        )

        self.ontology_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_ontology_list(),
            command=self.update_terms_list
        )
        self.ontology_list.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        ontologies = self.get_ontology_list()
        if ontologies:
            self.ontology_list.set(ontologies[0])
            initial_terms = self.get_terms_for_ontology(ontologies[0])
        else:
            initial_terms = ["Нет онтологий"]

        self.term_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=initial_terms,
            command=self.on_term_selected
        )
        self.term_list.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.sort_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_set_names(),
            command=self.on_sort_selected
        )
        self.sort_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.button_add_sort = customtkinter.CTkButton(
            self.frame_right,
            text="Добавить",
            command=self.add_ontology_sort
        )
        self.button_add_sort.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

        self.tree_sorts = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Онтология", "Термин", "Сорт"),
            show="headings",
        )
        self.tree_sorts.heading("ID", text="ID")
        self.tree_sorts.heading("Онтология", text="Онтология")
        self.tree_sorts.heading("Термин", text="Термин")
        self.tree_sorts.heading("Сорт", text="Сорт")
        self.tree_sorts.column("ID", width=50)
        self.tree_sorts.column("Онтология", width=150)
        self.tree_sorts.column("Термин", width=150)
        self.tree_sorts.column("Сорт", width=150)

        self.tree_sorts.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(3, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_ontology_sorts()

    def update_terms_list(self, selected_ontology):
        terms = self.get_terms_for_ontology(selected_ontology)
        self.term_list.configure(values=terms)
        if terms:
            self.term_list.set(terms[0])

    def get_terms_for_ontology(self, ontology_name):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT term FROM ontology_terms WHERE ontology_name = ?", (ontology_name,))
        terms = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not terms:
            return ["Нет терминов"]
        return terms

    def on_term_selected(self, selected_term):
        
        if selected_term != "Нет терминов":
           
            pass

    def get_set_names(self):
        conn = sqlite3.connect("ontology.db")  
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name FROM set_names")  
            set_names = [row[0] for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            set_names = ["Нет доступных множеств"]
        conn.close()

        if not set_names:
            return ["Нет доступных множеств"]
        return set_names

    def on_sort_selected(self, selected_sort):
        if selected_sort != "Нет доступных множеств":
            
            pass

    def add_ontology_sort(self):
        ontology = self.ontology_list.get()
        term = self.term_list.get()
        sort = self.sort_list.get()

        if ontology and term and sort and term != "Нет терминов" and sort != "Нет доступных множеств":
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO ontology_sorts (ontology_name, term, sort) VALUES (?, ?, ?)",
                    (ontology, term, sort),
                )
                conn.commit()
                self.load_ontology_sorts()
            except sqlite3.IntegrityError:
                print("Такой сорт уже существует")
            conn.close()

    def load_ontology_sorts(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ontology_sorts")
        rows = cursor.fetchall()
        conn.close()

        self.tree_sorts.delete(*self.tree_sorts.get_children())
        for row in rows:
            self.tree_sorts.insert("", "end", values=row)
import sqlite3
from tkinter import ttk
import customtkinter


class KnowledgeEditor:
    def __init__(self, master):
        self.master = master
        self.visible = False

       
        #self.frame_left = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=220)
        self.frame_middle = customtkinter.CTkFrame(master, fg_color="#fbf2fb")
        self.frame_right = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=400)

       # self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)
        self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
        self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        
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
            command=self.show_interface_elements_intarface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.properties_of_elements = customtkinter.CTkButton(
            self.frame_middle,
            text="Свойства интерфейсных элементов",
            command=self.show_properties_of_elements,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.property_range = customtkinter.CTkButton(
            self.frame_middle,
            text="Область значений свойств",
            command=self.show_property_range,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.defining_element_properties = customtkinter.CTkButton(
            self.frame_middle,
            text="Определение свойств элемента",
            command=self.show_defining_element_properties,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.alternatives_for_sets = customtkinter.CTkButton(
            self.frame_middle,
            text="Альтернатива для множества",
            command=self.show_alternatives_interface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.group_of_elements = customtkinter.CTkButton(
            self.frame_middle,
            text="Группа элементов",
            command=self.show_group_elements_interface,
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

    def show(self):
        """Показывает все фреймы редактора знаний"""
        if not self.visible:
            #self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)
            self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
            self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
            
            self.master.grid_rowconfigure(1, weight=1)
            self.master.grid_columnconfigure(1, weight=1)
            self.frame_right.grid_rowconfigure(2, weight=1)
            self.frame_right.grid_columnconfigure(0, weight=1)
            
            self.visible = True

    def hide(self):
        """Скрывает все фреймы редактора знаний"""
        if self.visible:
            #self.frame_left.grid_remove()
            self.frame_middle.grid_remove()
            self.frame_right.grid_remove()
            self.visible = False

    def switch_to_data_editor(self, choice):
        """переключатель на редактор данных"""
        self.master.data_editor.show()
        self.hide()

    def switch_to_solver(self):
        """переключатель на решатель задач"""
        self.master.solver.show()
        self.hide()


    def clear_right_frame(self):
        """Очищает правый фрейм перед загрузкой нового интерфейса"""
        for widget in self.frame_right.winfo_children():
            widget.destroy()

    def show_sets_interface(self, choice="Название множеств"):
        """Отображает элементы для управления таблицей 'Название множеств'"""
        self.clear_right_frame()

    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        
        self.entry = customtkinter.CTkEntry(
            self.frame_right, placeholder_text="Введите название множества", width=280
        )
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button_add = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_set
        )
        self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        
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

       
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text="Определение множеств", font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        
        self.sets_list = customtkinter.CTkOptionMenu(
            self.frame_right, values=self.get_sets_list()
        )
        self.sets_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        
        self.entry_definition = customtkinter.CTkEntry(
            self.frame_right,
            placeholder_text="Введите обозначение множества",
            width=280,
        )
        self.entry_definition.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

       
        self.button_add_definition = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_definition
        )
        self.button_add_definition.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        
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

    
        self.load_definitions()

    def show_interface_elements_intarface(self, choice="Название множеств"):
        self.clear_right_frame()

    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        self.entry_interface_elements = customtkinter.CTkEntry(
            self.frame_right, placeholder_text="Введите название элемента", width=280
        )
        self.entry_interface_elements.grid(
            row=1, column=0, padx=10, pady=10, sticky="ew"
        )

        self.button_add = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_interface_elements
        )
        self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.tree_interface_elements = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree_interface_elements.heading("ID", text="ID")
        self.tree_interface_elements.heading(
            "Название", text="Название интерфесного эелемента"
        )
        self.tree_interface_elements.column("ID", width=50)
        self.tree_interface_elements.column("Название", width=250)

        self.tree_interface_elements.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
        )
        self.tree_interface_elements.grid_rowconfigure(2, weight=1)
        self.tree_interface_elements.grid_columnconfigure(0, weight=1)

        self.load_interface_elements()

    def show_properties_of_elements(self, choice="Свойства интерфейсных элементов"):
        self.clear_right_frame()

    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        self.entry_properties_of_elements = customtkinter.CTkEntry(
            self.frame_right,
            placeholder_text="Введите свойство интрефейсного элемента",
            width=280,
        )
        self.entry_properties_of_elements.grid(
            row=1, column=0, padx=10, pady=10, sticky="ew"
        )

        self.button_add = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_properties_of_elements
        )
        self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.tree_properties_of_elements = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree_properties_of_elements.heading("ID", text="ID")
        self.tree_properties_of_elements.heading(
            "Название", text="Название интерфесного эелемента"
        )
        self.tree_properties_of_elements.column("ID", width=50)
        self.tree_properties_of_elements.column("Название", width=250)

        self.tree_properties_of_elements.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
        )
        self.tree_properties_of_elements.grid_rowconfigure(2, weight=1)
        self.tree_properties_of_elements.grid_columnconfigure(0, weight=1)

        self.load_properties_of_elements()

    def show_property_range(self, choice="Область значений свойств"):

        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right,
            text="Область значений свойств",
            font=("Arial", 18, "bold"),
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        self.properties_list = customtkinter.CTkOptionMenu(
            self.frame_right, values=self.get_properties_list()
        )
        self.properties_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.entry_property_range = customtkinter.CTkEntry(
            self.frame_right,
            placeholder_text="Введите значение из допустимой области",
            width=280,
        )
        self.entry_property_range.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
       
        self.button_add_property_range = customtkinter.CTkButton(
            self.frame_right, text="Добавить", command=self.add_property_range
        )
        self.button_add_property_range.grid(
            row=1, column=2, padx=10, pady=10, sticky="ew"
        )

        self.tree_property_range = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Свойство", "Область занчения"),
            show="headings",
        )
        self.tree_property_range.heading("ID", text="ID")
        self.tree_property_range.heading("Свойство", text="Свойство")
        self.tree_property_range.heading("Область занчения", text="Область занчения")
        self.tree_property_range.column("ID", width=50)
        self.tree_property_range.column("Свойство", width=150)
        self.tree_property_range.column("Область занчения", width=250)

        self.tree_property_range.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        
        self.load_property_range()

    def show_defining_element_properties(self, choice="Определение свойств элемента"):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right,
            text="Определение свойств элемента",
            font=("Arial", 18, "bold"),
        )
        self.label_title.grid(
            row=0, column=0, columnspan=4, padx=5, pady=5, sticky="w"
        )

       
        self.element_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_element_list(),
            width=200
        )
        self.element_list.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

        
        self.properties_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_properties_list(),
            command=self.update_property_values,
            width=200
        )
        self.properties_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

    
        self.property_values_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=["Выберите свойство"],
            width=200
        )
        self.property_values_list.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        
        self.button_add_property = customtkinter.CTkButton(
            self.frame_right,
            text="Добавить",
            command=self.add_element_property,
            width=100
        )
        self.button_add_property.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

        self.tree_element_properties = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Элемент", "Свойство", "Значение"),
            show="headings"
        )
        self.tree_element_properties.heading("ID", text="ID")
        self.tree_element_properties.heading("Элемент", text="Элемент")
        self.tree_element_properties.heading("Свойство", text="Свойство")
        self.tree_element_properties.heading("Значение", text="Значение")
        self.tree_element_properties.column("ID", width=50)
        self.tree_element_properties.column("Элемент", width=150)
        self.tree_element_properties.column("Свойство", width=150)
        self.tree_element_properties.column("Значение", width=150)

        self.tree_element_properties.grid(
            row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        for i in range(4):
            self.frame_right.grid_columnconfigure(i, weight=1)

        self.load_element_properties()

    def update_property_values(self, selected_property):
        """Обновляет список значений при выборе свойства"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ranges 
            FROM property_range 
            WHERE property = ?
        """, (selected_property,))
        values = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not values:
            values = ["Нет доступных значений"]
        
        self.property_values_list.configure(values=values)
        self.property_values_list.set(values[0])

    def add_element_property(self):
        """Добавляет свойство для элемента"""
        element = self.element_list.get()
        property = self.properties_list.get()
        value = self.property_values_list.get()

        print(f"Добавление свойства:")
        print(f"Элемент: {element}")
        print(f"Свойство: {property}")
        print(f"Значение: {value}")

        if element != "Нет элементов" and property != "Нет свойств" and value != "Нет доступных значений":
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
             
                cursor.execute("SELECT id FROM interface_elements WHERE name = ?", (element,))
                element_id_result = cursor.fetchone()
                print(f"ID элемента: {element_id_result}")
                
                cursor.execute("SELECT id FROM properties_of_elements WHERE name = ?", (property,))
                property_id_result = cursor.fetchone()
                print(f"ID свойства: {property_id_result}")

                if element_id_result is None or property_id_result is None:
                    print("Ошибка: не найден ID элемента или свойства")
                    return

                element_id = element_id_result[0]
                property_id = property_id_result[0]

                cursor.execute("""
                    INSERT INTO element_properties_definition 
                    (element_id, property_id, property_value) 
                    VALUES (?, ?, ?)
                """, (element_id, property_id, value))
                
                conn.commit()
                print("Запись успешно добавлена")
                self.load_element_properties()
            except sqlite3.IntegrityError as e:
                print(f"Ошибка при добавлении: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
            finally:
                conn.close()

    def load_element_properties(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                epd.id, 
                ie.name as element_name, 
                pe.name as property_name, 
                epd.property_value
            FROM element_properties_definition epd
            JOIN interface_elements ie ON epd.element_id = ie.id
            JOIN properties_of_elements pe ON epd.property_id = pe.id
            ORDER BY ie.name, pe.name
        """)
        rows = cursor.fetchall()
        conn.close()


        self.tree_element_properties.delete(*self.tree_element_properties.get_children())
     
        for row in rows:
            self.tree_element_properties.insert("", "end", values=row)

       

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

    def add_interface_elements(self):
        name = self.entry_interface_elements.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO interface_elements (name) VALUES (?)", (name,)
                )
                conn.commit()
                self.entry_interface_elements.delete(0, "end")
                self.load_interface_elements()
            except sqlite3.IntegrityError:
                print("Такой элемент уже существует")
            conn.close()

    def add_properties_of_elements(self):
        name = self.entry_properties_of_elements.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO properties_of_elements (name) VALUES (?)", (name,)
                )
                conn.commit()
                self.entry_properties_of_elements.delete(0, "end")
                self.load_properties_of_elements()
            except sqlite3.IntegrityError:
                print("Такой элемент уже существует")
            conn.close()

    def add_property_range(self):
        property = self.properties_list.get()
        ranges = self.entry_property_range.get()

        if property and ranges:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO property_range (property, ranges) VALUES (?, ?)",
                    (property, ranges),
                )
                conn.commit()
                self.entry_property_range.delete(0, "end")
                self.load_property_range()
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

    def load_interface_elements(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM interface_elements")
        rows = cursor.fetchall()
        conn.close()

        self.tree_interface_elements.delete(
            *self.tree_interface_elements.get_children()
        )
        for row in rows:
            self.tree_interface_elements.insert("", "end", values=row)

    def load_properties_of_elements(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM properties_of_elements")
        rows = cursor.fetchall()
        conn.close()

        self.tree_properties_of_elements.delete(
            *self.tree_properties_of_elements.get_children()
        )
        for row in rows:
            self.tree_properties_of_elements.insert("", "end", values=row)

    def load_property_range(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM property_range")
        rows = cursor.fetchall()
        conn.close()

        self.tree_property_range.delete(*self.tree_property_range.get_children())
        for row in rows:
            self.tree_property_range.insert("", "end", values=row)

    def get_sets_list(self):
        """Возвращает список названий множеств из базы"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sets")
        sets = [row[0] for row in cursor.fetchall()]
        conn.close()
        return sets

    def get_properties_list(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM properties_of_elements")
        sets = [row[0] for row in cursor.fetchall()]
        conn.close()
        return sets

    def get_element_list(self):
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM interface_elements")
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

    def show_alternatives_interface(self, choice="Альтернатива для множества"):
        """Отображает элементы для управления альтернативами множеств"""
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w"
        )

     
        self.entry_alternative = customtkinter.CTkEntry(
            self.frame_right,
            placeholder_text="Введите название альтернативы",
            width=200
        )
        self.entry_alternative.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

        self.sets_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_set_names_from_definitions(),
            width=200
        )
        self.sets_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

        self.button_add_alternative = customtkinter.CTkButton(
            self.frame_right,
            text="Добавить",
            command=self.add_alternative,
            width=100
        )
        self.button_add_alternative.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        
        self.tree_alternatives = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Альтернатива", "Множество"),
            show="headings"
        )
        self.tree_alternatives.heading("ID", text="ID")
        self.tree_alternatives.heading("Альтернатива", text="Название альтернативы")
        self.tree_alternatives.heading("Множество", text="Название множества")
        self.tree_alternatives.column("ID", width=50)
        self.tree_alternatives.column("Альтернатива", width=200)
        self.tree_alternatives.column("Множество", width=200)

        self.tree_alternatives.grid(
            row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)

        self.load_alternatives()

    def get_set_names_from_definitions(self):
        """Получает список названий множеств из таблицы definitions"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT DISTINCT set_name FROM definitions WHERE set_name IS NOT NULL AND set_name != ''")
            set_names = [row[0] for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            set_names = ["Нет доступных множеств"]
        conn.close()

        if not set_names:
            return ["Нет доступных множеств"]
        return set_names

    def add_alternative(self):
        """Добавляет новую альтернативу в базу данных"""
        alternative_name = self.entry_alternative.get()
        set_name = self.sets_list.get()

        if alternative_name and set_name and set_name != "Нет доступных множеств":
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO alternatives (alternative_name, set_name) VALUES (?, ?)",
                    (alternative_name, set_name),
                )
                conn.commit()
                self.entry_alternative.delete(0, "end")
                self.load_alternatives()
            except sqlite3.IntegrityError:
                print("Такая альтернатива уже существует")
            conn.close()

    def load_alternatives(self):
        """Загружает список альтернатив из базы данных"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alternatives")
        rows = cursor.fetchall()
        conn.close()

        self.tree_alternatives.delete(*self.tree_alternatives.get_children())
        for row in rows:
            self.tree_alternatives.insert("", "end", values=row)

    def show_group_elements_interface(self, choice="Группа элементов"):
        """Отображает интерфейс для управления группами элементов"""
        self.clear_right_frame()

        
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w"
        )

        
        self.alternatives_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_alternatives_list(),
            width=200
        )
        self.alternatives_list.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

     
        self.element_properties_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_element_properties_list(),
            width=200
        )
        self.element_properties_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

        
        self.button_add_group = customtkinter.CTkButton(
            self.frame_right,
            text="Добавить",
            command=self.add_element_to_group,
            width=100
        )
        self.button_add_group.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        
        self.tree_groups = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Альтернатива", "Элемент", "Свойство"),
            show="headings"
        )
        self.tree_groups.heading("ID", text="ID")
        self.tree_groups.heading("Альтернатива", text="Альтернатива")
        self.tree_groups.heading("Элемент", text="Элемент")
        self.tree_groups.heading("Свойство", text="Свойство")
        self.tree_groups.column("ID", width=50)
        self.tree_groups.column("Альтернатива", width=150)
        self.tree_groups.column("Элемент", width=150)
        self.tree_groups.column("Свойство", width=150)

        self.tree_groups.grid(
            row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)

        self.load_groups()

    def get_alternatives_list(self):
        """Получает список альтернатив из базы данных"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT alternative_name FROM alternatives")
        alternatives = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not alternatives:
            return ["Нет альтернатив"]
        return alternatives

    def get_element_properties_list(self):
        """Получает список элементов с их свойствами"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ui_elements || ' - ' || property_element 
            FROM defining_element_properties
        """)
        elements = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not elements:
            return ["Нет элементов"]
        return elements

    def add_element_to_group(self):
        """Добавляет элемент в группу"""
        alternative = self.alternatives_list.get()
        element_property = self.element_properties_list.get()

        if alternative != "Нет альтернатив" and element_property != "Нет элементов":
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
               
                cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", (alternative,))
                alternative_id = cursor.fetchone()[0]

                
                element, property = element_property.split(" - ")
                cursor.execute(
                    "SELECT id FROM defining_element_properties WHERE ui_elements = ? AND property_element = ?",
                    (element, property)
                )
                element_property_id = cursor.fetchone()[0]

               
                cursor.execute(
                    "INSERT INTO alternative_elements (alternative_id, element_property_id) VALUES (?, ?)",
                    (alternative_id, element_property_id)
                )
                conn.commit()
                self.load_groups()
            except sqlite3.IntegrityError:
                print("Такая связь уже существует")
            finally:
                conn.close()

    def load_groups(self):
        """Загружает группы элементов"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ae.id, a.alternative_name, dep.ui_elements, dep.property_element
            FROM alternative_elements ae
            JOIN alternatives a ON ae.alternative_id = a.id
            JOIN defining_element_properties dep ON ae.element_property_id = dep.id
        """)
        rows = cursor.fetchall()
        conn.close()

        self.tree_groups.delete(*self.tree_groups.get_children())
        for row in rows:
            self.tree_groups.insert("", "end", values=row)
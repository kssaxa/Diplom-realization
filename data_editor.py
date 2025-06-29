import sqlite3
from tkinter import ttk
import customtkinter


class DataEditor:
    def button_callback(self):

        print("Кнопка работает")

    def __init__(self, master, readonly=False):
        self.master = master
        self.visible = False
        self.readonly = readonly  # Режим только просмотра

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
            command=self.show_screen_forms_interface,
            fg_color="#FFD1DC",
            text_color="#FF007F",
        )
        self.definition_window_forms = customtkinter.CTkButton(
            self.frame_middle,
            text="Определение экранной формы",
            command=self.show_screen_form_definitions_interface,
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

        # Показываем элементы ввода только если не режим просмотра
        if not self.readonly:
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

        # Позиционируем таблицу в зависимости от режима
        if self.readonly:
            self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        else:
            self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.frame_right.grid_rowconfigure(2 if not self.readonly else 1, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_ontology_data()

    def add_ontology(self):
        if self.readonly:
            return
            
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
            row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w"
        )

        # Выпадающий список для выбора онтологии
        self.ontology_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_ontology_list(),
            command=self.update_terms_list
        )
        self.ontology_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Показываем элементы ввода только если не режим просмотра
        if not self.readonly:
            # Поле ввода для термина (вместо выпадающего списка)
            self.term_entry = customtkinter.CTkEntry(
                self.frame_right,
                placeholder_text="Введите термин онтологии",
                width=200
            )
            self.term_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

            # Кнопка добавления
            self.button_add_term = customtkinter.CTkButton(
                self.frame_right, text="Добавить", command=self.add_ontology_term
            )
            self.button_add_term.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Таблица для отображения терминов
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
        self.frame_right.grid_columnconfigure(1, weight=1)

        # Устанавливаем первую онтологию по умолчанию
        ontologies = self.get_ontology_list()
        if ontologies:
            self.ontology_list.set(ontologies[0])

        self.load_ontology_terms()

    def add_ontology_term(self):
        """Добавляет термин онтологии"""
        if self.readonly:
            return
            
        ontology = self.ontology_list.get()
        term = self.term_entry.get().strip()  # Получаем текст из поля ввода

        if ontology and term:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO ontology_terms (ontology_name, term) VALUES (?, ?)",
                    (ontology, term),
                )
                conn.commit()
                self.term_entry.delete(0, "end")  # Очищаем поле ввода
                self.load_ontology_terms()
            except sqlite3.IntegrityError:
                print("Такой термин уже существует")
            conn.close()

    def update_terms_list(self, selected_ontology):
        """Обновляет список терминов при выборе онтологии"""
        # Теперь этот метод не нужен, так как термины вводятся вручную
        # Но оставляем для совместимости
        pass

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
            row=0, column=0, columnspan=4, padx=5, pady=5, sticky="w"
        )

        self.ontology_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_ontology_list(),
            command=self.update_terms_list,
            width=150
        )
        self.ontology_list.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

        ontologies = self.get_ontology_list()
        if ontologies:
            self.ontology_list.set(ontologies[0])
            initial_terms = self.get_terms_for_ontology(ontologies[0])
        else:
            initial_terms = ["Нет онтологий"]

        self.term_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=initial_terms,
            command=self.on_term_selected,
            width=150
        )
        self.term_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

        self.sort_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_set_names(),
            command=self.on_sort_selected,
            width=150
        )
        self.sort_list.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        # Показываем кнопку добавления только если не режим просмотра
        if not self.readonly:
            self.button_add_sort = customtkinter.CTkButton(
                self.frame_right,
                text="Добавить",
                command=self.add_ontology_sort,
                width=100
            )
            self.button_add_sort.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

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

        # Позиционируем таблицу в зависимости от режима
        if self.readonly:
            self.tree_sorts.grid(
                row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(1, weight=1)
        else:
            self.tree_sorts.grid(
                row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(2, weight=1)
            
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_ontology_sorts()

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
            cursor.execute("SELECT DISTINCT set_name FROM definitions WHERE set_name IS NOT NULL AND set_name != ''")  
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
        if self.readonly:
            return
            
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

    def get_ontology_terms_list(self):
        """Получает список терминов онтологии для экранных форм"""
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ot.ontology_name || ' - ' || ot.term
            FROM ontology_terms ot
            ORDER BY ot.ontology_name, ot.term
        """)
        terms = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not terms:
            return ["Нет терминов онтологии"]
        return terms

    def show_screen_forms_interface(self, choice="Экранные формы"):
        """Отображает интерфейс для управления экранными формами"""
        self.clear_right_frame()

        # Заголовок
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=4, padx=5, pady=5, sticky="w"
        )

        # Показываем элементы управления только если не режим просмотра
        if not self.readonly:
            # Поле ввода названия экранной формы
            self.entry_screen_form = customtkinter.CTkEntry(
                self.frame_right,
                placeholder_text="Введите название экранной формы",
                width=250
            )
            self.entry_screen_form.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

            # Выпадающий список терминов онтологии
            self.ontology_terms_list = customtkinter.CTkOptionMenu(
                self.frame_right,
                values=self.get_ontology_terms_list(),
                width=300
            )
            self.ontology_terms_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

            # Кнопка добавления
            self.button_add_screen_form = customtkinter.CTkButton(
                self.frame_right,
                text="Добавить",
                command=self.add_screen_form,
                width=100
            )
            self.button_add_screen_form.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

            # Кнопка удаления
            self.button_delete_screen_form = customtkinter.CTkButton(
                self.frame_right,
                text="Удалить",
                command=self.delete_screen_form,
                width=100,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete_screen_form.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

        # Таблица экранных форм
        self.tree_screen_forms = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Название", "Термин онтологии"),
            show="headings"
        )
        self.tree_screen_forms.heading("ID", text="ID")
        self.tree_screen_forms.heading("Название", text="Название экранной формы")
        self.tree_screen_forms.heading("Термин онтологии", text="Термин онтологии")
        self.tree_screen_forms.column("ID", width=50)
        self.tree_screen_forms.column("Название", width=200)
        self.tree_screen_forms.column("Термин онтологии", width=250)
        
        # Позиционируем таблицу в зависимости от режима
        if self.readonly:
            self.tree_screen_forms.grid(
                row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(1, weight=1)
        else:
            self.tree_screen_forms.grid(
                row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(2, weight=1)
            
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)

        self.load_screen_forms()

    def add_screen_form(self):
        """Добавляет экранную форму и автоматически создает альтернативу"""
        if self.readonly:
            return
            
        form_name = self.entry_screen_form.get()
        ontology_term = self.ontology_terms_list.get()

        if form_name and ontology_term and ontology_term != "Нет терминов онтологии":
            # Добавляем экранную форму в data.db
            conn_data = sqlite3.connect("data.db")
            cursor_data = conn_data.cursor()
            try:
                cursor_data.execute(
                    "INSERT INTO screen_forms (form_name, ontology_term) VALUES (?, ?)",
                    (form_name, ontology_term)
                )
                conn_data.commit()
                print(f"✅ Экранная форма '{form_name}' добавлена в data.db")
            except sqlite3.IntegrityError:
                print("Такая экранная форма уже существует")
                conn_data.close()
                return
            finally:
                conn_data.close()
            
            # Автоматически создаем альтернативу в ontology.db
            conn_ontology = sqlite3.connect("ontology.db")
            cursor_ontology = conn_ontology.cursor()
            try:
                # Создаем альтернативу
                alternative_name = f"Альтернатива для {form_name}"
                cursor_ontology.execute("""
                    INSERT OR IGNORE INTO alternatives (alternative_name, set_name) 
                    VALUES (?, ?)
                """, (alternative_name, form_name))
                
                # Получаем ID созданной альтернативы
                cursor_ontology.execute("SELECT id FROM alternatives WHERE alternative_name = ?", (alternative_name,))
                alternative_id = cursor_ontology.fetchone()[0]
                
                print(f"✅ Альтернатива '{alternative_name}' создана в ontology.db с ID: {alternative_id}")
                
                # Добавляем базовые элементы интерфейса к альтернативе
                cursor_ontology.execute("""
                    SELECT epd.id, ie.name, poe.name, epd.property_value
                    FROM element_properties_definition epd
                    JOIN interface_elements ie ON epd.element_id = ie.id
                    JOIN properties_of_elements poe ON epd.property_id = poe.id
                    WHERE ie.name IN ('Заголовок', 'Поле ввода', 'Кнопка', 'Список', 'Подсказка')
                    ORDER BY ie.name, poe.name
                """)
                
                definitions = cursor_ontology.fetchall()
                
                # Добавляем элементы в альтернативу
                for def_id, elem_name, prop_name, prop_value in definitions:
                    cursor_ontology.execute("""
                        INSERT OR IGNORE INTO alternative_elements 
                        (alternative_id, element_property_id) VALUES (?, ?)
                    """, (alternative_id, def_id))
                
                conn_ontology.commit()
                print(f"✅ Добавлено {len(definitions)} элементов интерфейса к альтернативе")
                
            except Exception as e:
                print(f"Ошибка при создании альтернативы: {e}")
            finally:
                conn_ontology.close()
            
            # Очищаем поле ввода и обновляем список
            self.entry_screen_form.delete(0, "end")
            self.load_screen_forms()
            print(f"🎉 Экранная форма '{form_name}' полностью настроена!")

    def load_screen_forms(self):
        """Загружает данные экранных форм"""
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, form_name, ontology_term FROM screen_forms ORDER BY form_name")
        rows = cursor.fetchall()
        conn.close()

        self.tree_screen_forms.delete(*self.tree_screen_forms.get_children())
        for row in rows:
            self.tree_screen_forms.insert("", "end", values=row)

    def delete_screen_form(self):
        """Удаляет экранную форму и соответствующую альтернативу"""
        if self.readonly:
            return
            
        selected_item = self.tree_screen_forms.selection()
        if selected_item:
            item_values = self.tree_screen_forms.item(selected_item)['values']
            if len(item_values) >= 2:
                item_id = item_values[0]
                form_name = item_values[1]
                
                # Удаляем экранную форму из data.db
                conn_data = sqlite3.connect("data.db")
                cursor_data = conn_data.cursor()
                try:
                    cursor_data.execute("DELETE FROM screen_forms WHERE id = ?", (item_id,))
                    conn_data.commit()
                    print(f"✅ Экранная форма '{form_name}' удалена из data.db")
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении экранной формы")
                    conn_data.close()
                    return
                finally:
                    conn_data.close()
                
                # Удаляем соответствующую альтернативу из ontology.db
                conn_ontology = sqlite3.connect("ontology.db")
                cursor_ontology = conn_ontology.cursor()
                try:
                    # Находим альтернативу по set_name
                    cursor_ontology.execute("SELECT id FROM alternatives WHERE set_name = ?", (form_name,))
                    alt_row = cursor_ontology.fetchone()
                    
                    if alt_row:
                        alt_id = alt_row[0]
                        # Удаляем элементы альтернативы
                        cursor_ontology.execute("DELETE FROM alternative_elements WHERE alternative_id = ?", (alt_id,))
                        # Удаляем саму альтернативу
                        cursor_ontology.execute("DELETE FROM alternatives WHERE id = ?", (alt_id,))
                        conn_ontology.commit()
                        print(f"✅ Альтернатива для '{form_name}' удалена из ontology.db")
                    else:
                        print(f"⚠️ Альтернатива для '{form_name}' не найдена в ontology.db")
                        
                except Exception as e:
                    print(f"Ошибка при удалении альтернативы: {e}")
                finally:
                    conn_ontology.close()
                
                self.load_screen_forms()

    def get_screen_forms_list(self):
        """Получает список экранных форм"""
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT form_name FROM screen_forms ORDER BY form_name")
        forms = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not forms:
            return ["Нет экранных форм"]
        return forms

    def get_alternatives_list(self):
        """Получает список альтернатив из ontology.db"""
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT alternative_name FROM alternatives ORDER BY alternative_name")
        alternatives = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not alternatives:
            return ["Нет альтернатив"]
        return alternatives

    def show_screen_form_definitions_interface(self, choice="Определение экранной формы"):
        """Отображает интерфейс для управления определениями экранных форм"""
        self.clear_right_frame()

        # Заголовок
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=4, padx=5, pady=5, sticky="w"
        )

        # Выпадающий список экранных форм
        self.screen_forms_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_screen_forms_list(),
            width=250
        )
        self.screen_forms_list.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

        # Выпадающий список альтернатив
        self.alternatives_list = customtkinter.CTkOptionMenu(
            self.frame_right,
            values=self.get_alternatives_list(),
            width=250
        )
        self.alternatives_list.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

        # Кнопка добавления
        self.button_add_screen_form_definition = customtkinter.CTkButton(
            self.frame_right,
            text="Добавить",
            command=self.add_screen_form_definition,
            width=100
        )
        self.button_add_screen_form_definition.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        # Кнопка удаления
        self.button_delete_screen_form_definition = customtkinter.CTkButton(
            self.frame_right,
            text="Удалить",
            command=self.delete_screen_form_definition,
            width=100,
            fg_color="#FF6B6B",
            text_color="white"
        )
        self.button_delete_screen_form_definition.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

        # Таблица определений экранных форм
        self.tree_screen_form_definitions = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Экранная форма", "Альтернатива"),
            show="headings"
        )
        self.tree_screen_form_definitions.heading("ID", text="ID")
        self.tree_screen_form_definitions.heading("Экранная форма", text="Экранная форма")
        self.tree_screen_form_definitions.heading("Альтернатива", text="Альтернатива")
        self.tree_screen_form_definitions.column("ID", width=50)
        self.tree_screen_form_definitions.column("Экранная форма", width=200)
        self.tree_screen_form_definitions.column("Альтернатива", width=200)
        self.tree_screen_form_definitions.grid(
            row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
        )
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)

        self.load_screen_form_definitions()

    def add_screen_form_definition(self):
        """Добавляет определение экранной формы"""
        screen_form_name = self.screen_forms_list.get()
        alternative_name = self.alternatives_list.get()

        print(f"Попытка добавления определения экранной формы:")
        print(f"  Экранная форма: '{screen_form_name}'")
        print(f"  Альтернатива: '{alternative_name}'")

        if screen_form_name and alternative_name and screen_form_name != "Нет экранных форм" and alternative_name != "Нет альтернатив":
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            try:
                print(f"  Выполняю INSERT в таблицу screen_form_definitions...")
                cursor.execute(
                    "INSERT INTO screen_form_definitions (screen_form_name, alternative_name) VALUES (?, ?)",
                    (screen_form_name, alternative_name)
                )
                conn.commit()
                print(f"  Запись успешно добавлена!")
                self.load_screen_form_definitions()
            except sqlite3.IntegrityError as e:
                print(f"  Ошибка IntegrityError: {e}")
                print("Такое определение уже существует")
            except Exception as e:
                print(f"  Неожиданная ошибка: {e}")
            finally:
                conn.close()
        else:
            print(f"  Проверка не пройдена:")
            print(f"    screen_form_name пустое: {not screen_form_name}")
            print(f"    alternative_name пустое: {not alternative_name}")
            print(f"    screen_form_name == 'Нет экранных форм': {screen_form_name == 'Нет экранных форм'}")
            print(f"    alternative_name == 'Нет альтернатив': {alternative_name == 'Нет альтернатив'}")

    def load_screen_form_definitions(self):
        """Загружает данные определений экранных форм"""
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, screen_form_name, alternative_name FROM screen_form_definitions ORDER BY screen_form_name")
        rows = cursor.fetchall()
        conn.close()

        self.tree_screen_form_definitions.delete(*self.tree_screen_form_definitions.get_children())
        for row in rows:
            self.tree_screen_form_definitions.insert("", "end", values=row)

    def delete_screen_form_definition(self):
        """Удаляет определение экранной формы"""
        selected_item = self.tree_screen_form_definitions.selection()
        if selected_item:
            item_values = self.tree_screen_form_definitions.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                conn = sqlite3.connect("data.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM screen_form_definitions WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_screen_form_definitions()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении определения экранной формы")
                finally:
                    conn.close()
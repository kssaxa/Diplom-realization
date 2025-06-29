import customtkinter
import sqlite3
from tkinter import ttk, messagebox
import os
import webbrowser
from datetime import datetime
from html_generator import HTMLInterfaceGenerator

class Solver:
    def __init__(self, master):
        self.master = master
        self.visible = False
        self.selected_screen_form = None  # Добавляем переменную для хранения ID выбранной формы
        
        # Создаем фреймы
        self.frame_middle = customtkinter.CTkFrame(master, fg_color="#fbf2fb")
        self.frame_right = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=400)
        
        # Инициализируем интерфейс
        self.create_interface()
        
        self.hide()
    
    def create_interface(self):
        """Создает интерфейс решателя задач"""
        
        # Заголовок
        self.label_title = customtkinter.CTkLabel(
            self.frame_middle,
            text="Решатель задач - Анализ экранных форм",
            font=("Arial", 18, "bold"),
            text_color="#FF007F"
        )
        self.label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # Выпадающий список экранных форм
        self.label_screen_form = customtkinter.CTkLabel(
            self.frame_middle,
            text="Выберите экранную форму для анализа:",
            font=("Arial", 12, "bold")
        )
        self.label_screen_form.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.screen_form_select = customtkinter.CTkOptionMenu(
            self.frame_middle,
            values=self.get_screen_forms_list(),
            command=self.on_screen_form_selected,
            width=300
        )
        self.screen_form_select.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Информация об экранной форме
        self.frame_info = customtkinter.CTkFrame(self.frame_middle, fg_color="#ffffff")
        self.frame_info.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.label_form_info = customtkinter.CTkLabel(
            self.frame_info,
            text="📋 Информация об экранной форме",
            font=("Arial", 14, "bold"),
            text_color="#FF007F"
        )
        self.label_form_info.pack(pady=5)
        
        self.label_form_name = customtkinter.CTkLabel(
            self.frame_info,
            text="Название: ",
            font=("Arial", 12)
        )
        self.label_form_name.pack(pady=2)
        
        self.label_ontology_term = customtkinter.CTkLabel(
            self.frame_info,
            text="Сорт онтологии: ",
            font=("Arial", 12)
        )
        self.label_ontology_term.pack(pady=2)
        
        # Информация об альтернативе (одна альтернатива на форму)
        self.label_alternative = customtkinter.CTkLabel(
            self.frame_middle,
            text="🔄 Альтернатива для данной экранной формы:",
            font=("Arial", 14, "bold"),
            text_color="#FF007F"
        )
        self.label_alternative.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # Фрейм для информации об альтернативе
        self.frame_alternative_info = customtkinter.CTkFrame(self.frame_middle, fg_color="#ffffff")
        self.frame_alternative_info.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        self.label_alt_name = customtkinter.CTkLabel(
            self.frame_alternative_info,
            text="Название альтернативы: ",
            font=("Arial", 12)
        )
        self.label_alt_name.pack(pady=2)
        
        self.label_alt_set = customtkinter.CTkLabel(
            self.frame_alternative_info,
            text="Связанное множество: ",
            font=("Arial", 12)
        )
        self.label_alt_set.pack(pady=2)
        
        # Кнопка генерации HTML интерфейса
        self.button_generate = customtkinter.CTkButton(
            self.frame_middle,
            text="🚀 Сгенерировать HTML интерфейс",
            command=self.generate_html_interface,
            fg_color="#FF6B6B",
            text_color="white",
            height=40
        )
        self.button_generate.grid(row=5, column=0, columnspan=2, padx=10, pady=15, sticky="ew")
        
        # Настройка весов для фрейма middle
        self.frame_middle.grid_columnconfigure(1, weight=1)
        
        # Правый фрейм для отображения элементов альтернативы
        self.label_elements = customtkinter.CTkLabel(
            self.frame_right,
            text="🎨 Элементы альтернативы:",
            font=("Arial", 14, "bold"),
            text_color="#FF007F"
        )
        self.label_elements.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Информация о выбранной альтернативе
        self.label_selected_alt = customtkinter.CTkLabel(
            self.frame_right,
            text="Выберите экранную форму для просмотра элементов альтернативы",
            font=("Arial", 10),
            text_color="#666666"
        )
        self.label_selected_alt.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Таблица элементов альтернативы
        self.tree_elements = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Элемент", "Свойство", "Значение"),
            show="headings",
            height=15
        )
        self.tree_elements.heading("ID", text="ID")
        self.tree_elements.heading("Элемент", text="Название элемента")
        self.tree_elements.heading("Свойство", text="Свойство")
        self.tree_elements.heading("Значение", text="Значение")
        self.tree_elements.column("ID", width=50)
        self.tree_elements.column("Элемент", width=120)
        self.tree_elements.column("Свойство", width=120)
        self.tree_elements.column("Значение", width=120)
        self.tree_elements.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        
        # Настройка весов для правого фрейма
        self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        
        # Кнопка обновления данных
        self.button_refresh = customtkinter.CTkButton(
            self.frame_right,
            text="🔄 Обновить данные",
            command=self.refresh_data,
            fg_color="#FFD1DC",
            text_color="#FF007F"
        )
        self.button_refresh.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
    def get_screen_forms_list(self):
        """Получает список экранных форм из data.db"""
        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT sf.id, sf.form_name, sf.ontology_term
                FROM screen_forms sf
                ORDER BY sf.form_name
            """)
            forms_data = cursor.fetchall()
            conn.close()
            
            if not forms_data:
                return ["Нет экранных форм"]
            
            # Создаем словарь для хранения соответствия названий и ID
            self.forms_dict = {f"{row[1]} ({row[2]})": row[0] for row in forms_data}
            return list(self.forms_dict.keys())
            
        except Exception as e:
            print(f"Ошибка при получении списка экранных форм: {e}")
            return ["Нет экранных форм"]
    
    def on_screen_form_selected(self, choice):
        """Обработчик выбора экранной формы"""
        if choice == "Нет экранных форм":
            self.clear_form_info()
            self.selected_screen_form = None
            return
        
        # Получаем ID выбранной формы
        self.selected_screen_form = self.forms_dict.get(choice)
        if self.selected_screen_form:
            self.load_form_info(choice)
            self.load_alternative_for_form(choice)
    
    def load_form_info(self, form_choice):
        """Загружает информацию об экранной форме из data.db"""
        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            
            # Получаем ID формы из выбора
            form_id = self.forms_dict.get(form_choice)
            if not form_id:
                return
            
            cursor.execute("""
                SELECT sf.form_name, sf.ontology_term
                FROM screen_forms sf
                WHERE sf.id = ?
            """, (form_id,))
            
            row = cursor.fetchone()
            conn.close()
            
            if row:
                form_name, ontology_term = row
                self.label_form_name.configure(text=f"Название: {form_name}")
                self.label_ontology_term.configure(text=f"Сорт онтологии: {ontology_term}")
            else:
                self.label_form_name.configure(text="Название: Не найдено")
                self.label_ontology_term.configure(text="Сорт онтологии: Не найден")
                
        except Exception as e:
            print(f"Ошибка при загрузке информации о форме: {e}")
            self.label_form_name.configure(text="Название: Ошибка загрузки")
            self.label_ontology_term.configure(text="Сорт онтологии: Ошибка загрузки")
    
    def load_alternative_for_form(self, form_choice):
        """Загружает альтернативу для экранной формы"""
        try:
            # Очищаем таблицу элементов
            self.tree_elements.delete(*self.tree_elements.get_children())
            
            # Получаем ID формы из выбора
            form_id = self.forms_dict.get(form_choice)
            if not form_id:
                return
            
            # Получаем название формы из data.db
            conn_data = sqlite3.connect("data.db")
            cursor_data = conn_data.cursor()
            cursor_data.execute("SELECT form_name FROM screen_forms WHERE id = ?", (form_id,))
            form_name_row = cursor_data.fetchone()
            conn_data.close()
            
            if not form_name_row:
                return
            
            form_name = form_name_row[0]
            
            # Получаем альтернативу из ontology.db
            conn_ontology = sqlite3.connect("ontology.db")
            cursor_ontology = conn_ontology.cursor()
            
            cursor_ontology.execute("""
                SELECT a.id, a.alternative_name, a.set_name
                FROM alternatives a
                WHERE a.set_name = ?
            """, (form_name,))
            
            alternative = cursor_ontology.fetchone()
            if not alternative:
                self.label_alt_name.configure(text="Название альтернативы: Не найдено")
                self.label_alt_set.configure(text="Связанное множество: Не найдено")
                self.label_selected_alt.configure(text="Альтернатива не найдена для данной экранной формы")
                conn_ontology.close()
                return
            
            alt_id, alt_name, set_name = alternative
            
            # Обновляем информацию об альтернативе
            self.label_alt_name.configure(text=f"Название альтернативы: {alt_name}")
            self.label_alt_set.configure(text=f"Связанное множество: {set_name}")
            
            # Обновляем информацию о выбранной альтернативе
            self.label_selected_alt.configure(
                text=f"Альтернатива: {alt_name} (Множество: {set_name})"
            )
            
            # Загружаем элементы для данной альтернативы из ontology.db
            cursor_ontology.execute("""
                SELECT ae.id, ie.name, poe.name, epd.property_value
                FROM alternative_elements ae
                JOIN element_properties_definition epd ON ae.element_property_id = epd.id
                JOIN interface_elements ie ON epd.element_id = ie.id
                JOIN properties_of_elements poe ON epd.property_id = poe.id
                WHERE ae.alternative_id = ?
                ORDER BY ie.name, poe.name
            """, (alt_id,))
            
            rows = cursor_ontology.fetchall()
            conn_ontology.close()
            
            for row in rows:
                self.tree_elements.insert("", "end", values=row)
                
            print(f"Загружено {len(rows)} элементов для альтернативы '{alt_name}'")
                
        except Exception as e:
            print(f"Ошибка при загрузке альтернативы: {e}")
            self.label_selected_alt.configure(text="Ошибка при загрузке данных альтернативы")
    
    def clear_form_info(self):
        """Очищает информацию о форме"""
        self.label_form_name.configure(text="Название: ")
        self.label_ontology_term.configure(text="Сорт онтологии: ")
        self.label_alt_name.configure(text="Название альтернативы: ")
        self.label_alt_set.configure(text="Связанное множество: ")
        self.tree_elements.delete(*self.tree_elements.get_children())
        self.label_selected_alt.configure(text="Выберите экранную форму для просмотра элементов альтернативы")
    
    def refresh_data(self):
        """Обновляет данные"""
        # Обновляем список экранных форм
        self.screen_form_select.configure(values=self.get_screen_forms_list())
        
        # Если есть выбранная форма, обновляем её данные
        current_form = self.screen_form_select.get()
        if current_form and current_form != "Нет экранных форм":
            self.load_form_info(current_form)
            self.load_alternative_for_form(current_form)
    
    def show(self):
        if not self.visible:
            self.frame_middle.grid(row=0, column=1, sticky="new", padx=10, pady=10)
            self.frame_right.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
            
            self.master.grid_rowconfigure(1, weight=1)
            self.master.grid_columnconfigure(1, weight=1)
            self.frame_right.grid_rowconfigure(2, weight=1)
            self.frame_right.grid_columnconfigure(0, weight=1)
            
            # Обновляем данные при показе
            self.refresh_data()
            
            self.visible = True
    
    def hide(self):
        if self.visible:
            self.frame_middle.grid_remove()
            self.frame_right.grid_remove()
            self.visible = False

    def generate_html_interface(self):
        """Генерирует HTML интерфейс для выбранной экранной формы"""
        if not self.selected_screen_form:
            messagebox.showwarning("Предупреждение", "Сначала выберите экранную форму!")
            return
        
        try:
            # Создаем генератор HTML
            generator = HTMLInterfaceGenerator()
            
            # Генерируем HTML
            html_content, error = generator.generate_html(self.selected_screen_form)
            
            if error:
                messagebox.showerror("Ошибка", f"Ошибка генерации HTML: {error}")
                return
            
            # Сохраняем файл
            filename = generator.save_html_file(html_content, self.selected_screen_form)
            
            # Показываем диалог с результатом
            self.show_generation_dialog(filename, html_content)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при генерации HTML: {str(e)}")
    
    def show_generation_dialog(self, filepath, html_content):
        """Показывает диалог с опциями после генерации"""
        dialog = customtkinter.CTkToplevel(self.master)
        dialog.title("HTML интерфейс сгенерирован")
        dialog.geometry("400x300")
        dialog.configure(fg_color="#ffffff")
        
        # Центрируем диалог
        dialog.transient(self.master)
        dialog.grab_set()
        
        # Заголовок
        title_label = customtkinter.CTkLabel(
            dialog,
            text="🎉 HTML интерфейс успешно сгенерирован!",
            font=("Arial", 16, "bold"),
            text_color="#FF007F"
        )
        title_label.pack(pady=20)
        
        # Информация о файле
        filename = os.path.basename(filepath)
        info_label = customtkinter.CTkLabel(
            dialog,
            text=f"Файл: {filename}",
            font=("Arial", 12),
            text_color="#333333"
        )
        info_label.pack(pady=10)
        
        # Кнопки
        button_frame = customtkinter.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=20)
        
        # Кнопка просмотра в браузере
        view_button = customtkinter.CTkButton(
            button_frame,
            text="🌐 Открыть в браузере",
            command=lambda: self.open_in_browser(filepath),
            fg_color="#4CAF50",
            text_color="white",
            width=150
        )
        view_button.pack(pady=5)
        
        # Кнопка открытия папки
        folder_button = customtkinter.CTkButton(
            button_frame,
            text="📁 Открыть папку",
            command=lambda: self.open_folder(filepath),
            fg_color="#2196F3",
            text_color="white",
            width=150
        )
        folder_button.pack(pady=5)
        
        # Кнопка закрытия
        close_button = customtkinter.CTkButton(
            button_frame,
            text="❌ Закрыть",
            command=dialog.destroy,
            fg_color="#FF6B6B",
            text_color="white",
            width=150
        )
        close_button.pack(pady=5)
    
    def open_in_browser(self, filepath):
        """Открывает HTML файл в браузере"""
        try:
            webbrowser.open(f'file://{os.path.abspath(filepath)}')
        except Exception as e:
            print(f"Ошибка при открытии в браузере: {e}")
    
    def open_folder(self, filepath):
        """Открывает папку с файлом"""
        try:
            folder_path = os.path.dirname(os.path.abspath(filepath))
            if os.name == 'nt':  # Windows
                os.startfile(folder_path)
            else:  # Linux/Mac
                os.system(f'xdg-open "{folder_path}"')
        except Exception as e:
            print(f"Ошибка при открытии папки: {e}")
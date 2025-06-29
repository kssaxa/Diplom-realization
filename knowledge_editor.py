import sqlite3
from tkinter import ttk
import customtkinter


class KnowledgeEditor:
    def __init__(self, master, readonly=False):
        self.master = master
        self.visible = False
        self.readonly = readonly  # Режим только просмотра

       
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
       
        if self.visible:
            #self.frame_left.grid_remove()
            self.frame_middle.grid_remove()
            self.frame_right.grid_remove()
            self.visible = False

    def switch_to_data_editor(self, choice):
       
        self.master.data_editor.show()
        self.hide()

    def switch_to_solver(self):
   
        self.master.solver.show()
        self.hide()


    def clear_right_frame(self):

        for widget in self.frame_right.winfo_children():
            widget.destroy()

    def show_sets_interface(self, choice="Название множеств"):
     
        self.clear_right_frame()

    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        # Показываем элементы редактирования только если не режим просмотра
        if not self.readonly:
            self.entry = customtkinter.CTkEntry(
                self.frame_right, placeholder_text="Введите название множества", width=280
            )
            self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

            self.button_add = customtkinter.CTkButton(
                self.frame_right, text="Добавить", command=self.add_set
            )
            self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

            # Кнопка удаления
            self.button_delete = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_set,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Таблица
        self.tree = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Название", text="Название множества")
        self.tree.column("ID", width=50)
        self.tree.column("Название", width=250)

        # Позиционируем таблицу в зависимости от режима
        if self.readonly:
            self.tree.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(1, weight=1)
        else:
            self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
            
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_sets()

    def show_definitions_interface(self):
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

        if not self.readonly:
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

            self.button_delete_definition = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_definition,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete_definition.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

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

        if self.readonly:
            self.tree_definitions.grid(
                row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_definitions.grid(
                row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew"
            )
            self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_definitions()

    def show_interface_elements_intarface(self, choice="Название множеств"):
        self.clear_right_frame()
    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text="Интерфейсные элементы", font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        if not self.readonly:
            self.entry_interface_elements = customtkinter.CTkEntry(
                self.frame_right,
                placeholder_text="Введите название интерфейсного элемента",
                width=280,
            )
            self.entry_interface_elements.grid(
                row=1, column=0, padx=10, pady=10, sticky="ew"
            )

            self.button_add = customtkinter.CTkButton(
                self.frame_right, text="Добавить", command=self.add_interface_elements
            )
            self.button_add.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

            self.button_delete = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_interface_element,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.tree_interface_elements = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree_interface_elements.heading("ID", text="ID")
        self.tree_interface_elements.heading("Название", text="Название интерфейсного элемента")
        self.tree_interface_elements.column("ID", width=50)
        self.tree_interface_elements.column("Название", width=250)

        if self.readonly:
            self.tree_interface_elements.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_interface_elements.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_interface_elements()

    def show_properties_of_elements(self, choice="Свойства интерфейсных элементов"):
        self.clear_right_frame()
    
        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        if not self.readonly:
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

            self.button_delete = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_property,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.tree_properties_of_elements = ttk.Treeview(
            self.frame_right, columns=("ID", "Название"), show="headings"
        )
        self.tree_properties_of_elements.heading("ID", text="ID")
        self.tree_properties_of_elements.heading(
            "Название", text="Название интерфесного эелемента"
        )
        self.tree_properties_of_elements.column("ID", width=50)
        self.tree_properties_of_elements.column("Название", width=250)

        if self.readonly:
            self.tree_properties_of_elements.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_properties_of_elements.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_properties_of_elements()

    def show_property_range(self, choice="Область значений свойств"):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        if not self.readonly:
            self.properties_list = customtkinter.CTkOptionMenu(
                self.frame_right,
                values=self.get_properties_list(),
                width=200
            )
            self.properties_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

            self.entry_property_range = customtkinter.CTkEntry(
                self.frame_right,
                placeholder_text="Введите значение свойства",
                width=200
            )
            self.entry_property_range.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
           
            self.button_add = customtkinter.CTkButton(
                self.frame_right, text="Добавить", command=self.add_property_range
            )
            self.button_add.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

            self.button_delete = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_property_range,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

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

        if self.readonly:
            self.tree_property_range.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_property_range.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
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

        if not self.readonly:
            self.button_add_property = customtkinter.CTkButton(
                self.frame_right,
                text="Добавить",
                command=self.add_element_property,
                width=100
            )
            self.button_add_property.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

            self.button_delete_property = customtkinter.CTkButton(
                self.frame_right,
                text="Удалить",
                command=self.delete_element_property,
                width=100,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete_property.grid(row=1, column=4, padx=2, pady=5, sticky="ew")

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

        if self.readonly:
            self.tree_element_properties.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_element_properties.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        self.frame_right.grid_rowconfigure(2, weight=1)
        for i in range(5):
            self.frame_right.grid_columnconfigure(i, weight=1)

        self.load_element_properties()

    def show_alternatives_interface(self, choice="Альтернатива для множества"):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w"
        )

        if not self.readonly:
            self.sets_list_alt = customtkinter.CTkOptionMenu(
                self.frame_right,
                values=self.get_set_names_from_definitions(),
                width=200
            )
            self.sets_list_alt.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

            self.entry_alternative = customtkinter.CTkEntry(
                self.frame_right,
                placeholder_text="Введите название альтернативы",
                width=200
            )
            self.entry_alternative.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

            self.button_add_alt = customtkinter.CTkButton(
                self.frame_right, text="Добавить", command=self.add_alternative
            )
            self.button_add_alt.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

            self.button_delete_alt = customtkinter.CTkButton(
                self.frame_right, 
                text="Удалить", 
                command=self.delete_alternative,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete_alt.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

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

        if self.readonly:
            self.tree_alternatives.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        else:
            self.tree_alternatives.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
            self.frame_right.grid_rowconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        self.load_alternatives()

    def show_group_elements_interface(self, choice="Группа элементов"):
        self.clear_right_frame()

        self.label_title = customtkinter.CTkLabel(
            self.frame_right, text=choice, font=("Arial", 18, "bold")
        )
        self.label_title.grid(
            row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w"
        )

        self.info_label = customtkinter.CTkLabel(
            self.frame_right,
            text="Выберите альтернативу и элемент с определенными свойствами, затем добавьте в группу",
            font=("Arial", 10),
            text_color="#666666"
        )
        self.info_label.grid(
            row=1, column=0, columnspan=3, padx=5, pady=2, sticky="w"
        )

        if not self.readonly:
            self.alt_select_group = customtkinter.CTkOptionMenu(
                self.frame_right,
                values=self.get_alternatives_list(),
                width=200
            )
            self.alt_select_group.grid(row=2, column=0, padx=2, pady=5, sticky="ew")

            self.elem_prop_select_group = customtkinter.CTkOptionMenu(
                self.frame_right,
                values=self.get_element_properties_list(),
                width=300
            )
            self.elem_prop_select_group.grid(row=2, column=1, padx=2, pady=5, sticky="ew")

            self.button_add_elem_to_group = customtkinter.CTkButton(
                self.frame_right,
                text="Добавить элемент",
                command=self.add_element_to_group_alternative,
                width=150
            )
            self.button_add_elem_to_group.grid(row=2, column=2, padx=2, pady=(5, 2), sticky="ew")

        self.tree_group_elements = ttk.Treeview(
            self.frame_right,
            columns=("ID", "Элемент", "Свойство", "Значение"),
            show="headings"
        )
        self.tree_group_elements.heading("ID", text="ID")
        self.tree_group_elements.heading("Элемент", text="Элемент")
        self.tree_group_elements.heading("Свойство", text="Свойство")
        self.tree_group_elements.heading("Значение", text="Значение")
        self.tree_group_elements.column("ID", width=50)
        self.tree_group_elements.column("Элемент", width=120)
        self.tree_group_elements.column("Свойство", width=120)
        self.tree_group_elements.column("Значение", width=120)
        if self.readonly:
            self.tree_group_elements.grid(row=3, column=0, columnspan=3, padx=5, pady=(2, 2), sticky="nsew")
            self.frame_right.grid_rowconfigure(3, weight=1)
        else:
            self.tree_group_elements.grid(row=3, column=0, columnspan=3, padx=5, pady=(2, 2), sticky="nsew")
            self.frame_right.grid_rowconfigure(3, weight=1)

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)

        if not self.readonly:
            self.button_delete_elem_from_group = customtkinter.CTkButton(
                self.frame_right,
                text="Удалить выбранный элемент",
                command=self.delete_element_from_group_alternative,
                width=200,
                fg_color="#FF6B6B",
                text_color="white"
            )
            self.button_delete_elem_from_group.grid(row=4, column=1, padx=2, pady=(2, 5), sticky="ew")

        def on_alt_select_group_callback(choice):
            if not self.readonly:
                self.load_group_elements(choice)
        if not self.readonly:
            self.alt_select_group.configure(command=on_alt_select_group_callback)
        alt_list = self.get_alternatives_list()
        if alt_list and alt_list[0] != "Нет альтернатив" and not self.readonly:
            self.load_group_elements(alt_list[0])

    def add_set(self):
        if self.readonly:
            return
    
        name = self.entry.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO definitions (set_name) VALUES (?)", (name,))
                conn.commit()
                self.entry.delete(0, "end")
                self.load_sets()
            except sqlite3.IntegrityError:
                print("Такое множество уже существует")
            conn.close()

    def add_definition(self):
        if self.readonly:
            return
        
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
        if self.readonly:
            return
            
        name = self.entry_interface_elements.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO interface_elements (name) VALUES (?)", (name,))
                conn.commit()
                self.entry_interface_elements.delete(0, "end")
                self.load_interface_elements()
            except sqlite3.IntegrityError:
                print("Такой элемент уже существует")
            conn.close()

    def add_properties_of_elements(self):
        if self.readonly:
            return
            
        name = self.entry_properties_of_elements.get()
        if name:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO properties_of_elements (name) VALUES (?)", (name,))
                conn.commit()
                self.entry_properties_of_elements.delete(0, "end")
                self.load_properties_of_elements()
            except sqlite3.IntegrityError:
                print("Такое свойство уже существует")
            conn.close()

    def add_property_range(self):
        if self.readonly:
            return

        property_name = self.properties_list.get()
        value = self.entry_property_range.get()
        if property_name and value:
            conn = sqlite3.connect("ontology.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO property_value_range (property_name, value) VALUES (?, ?)",
                    (property_name, value),
                )
                conn.commit()
                self.entry_property_range.delete(0, "end")
                self.load_property_range()
            except sqlite3.IntegrityError:
                print("Такое значение уже существует")
            conn.close()

    def load_sets(self):
 
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sets")
        rows = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)

    def load_definitions(self):
   
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
    
        if choice == "Определение множеств":
            self.show_definitions_interface()
        if choice == "Название множеств":
            self.show_sets_interface(choice)

    def button_callback(self):

        print("Кнопка работает")

    def add_alternative(self):
       
        alternative_name = self.entry_alternative.get()
        set_name = self.sets_list_alt.get()

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
       
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alternatives")
        rows = cursor.fetchall()
        conn.close()

        self.tree_alternatives.delete(*self.tree_alternatives.get_children())
        for row in rows:
            self.tree_alternatives.insert("", "end", values=row)

    def add_element_to_group_alternative(self):
        """Добавляет элемент к альтернативе (перенесенный функционал из интерфейса альтернатив)"""
        alt_name = self.alt_select_group.get()
        elem_prop = self.elem_prop_select_group.get()
        
        print(f"Попытка добавления связи:")
        print(f"  Альтернатива: '{alt_name}'")
        print(f"  Элемент-свойство: '{elem_prop}'")
        
        if alt_name == "Нет альтернатив" or elem_prop == "Нет элементов с определенными свойствами":
            print("  Ошибка: выбраны недопустимые значения")
            return
            
        # Получаем id альтернативы
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", (alt_name,))
            alt_row = cursor.fetchone()
            if not alt_row:
                print(f"  Ошибка: альтернатива '{alt_name}' не найдена в БД")
                return
            alt_id = alt_row[0]
            print(f"  ID альтернативы: {alt_id}")
            
            # Получаем id element_properties_definition
            parts = elem_prop.split(" - ")
            if len(parts) != 3:
                print(f"  Ошибка: неправильный формат элемента-свойства: '{elem_prop}'")
                return
                
            element_name, property_name, property_value = parts
            print(f"  Разбор элемента-свойства:")
            print(f"    Элемент: '{element_name}'")
            print(f"    Свойство: '{property_name}'")
            print(f"    Значение: '{property_value}'")
            
            cursor.execute("""
                SELECT epd.id FROM element_properties_definition epd
                JOIN interface_elements ie ON epd.element_id = ie.id
                JOIN properties_of_elements poe ON epd.property_id = poe.id
                WHERE ie.name = ? AND poe.name = ? AND epd.property_value = ?
            """, (element_name, property_name, property_value))
            epd_row = cursor.fetchone()
            
            if not epd_row:
                print(f"  Ошибка: элемент-свойство не найден в БД")
                # Проверим, что существует
                cursor.execute("SELECT name FROM interface_elements WHERE name = ?", (element_name,))
                if not cursor.fetchone():
                    print(f"    Элемент '{element_name}' не существует")
                cursor.execute("SELECT name FROM properties_of_elements WHERE name = ?", (property_name,))
                if not cursor.fetchone():
                    print(f"    Свойство '{property_name}' не существует")
                return
                
            epd_id = epd_row[0]
            print(f"  ID элемента-свойства: {epd_id}")
            
            # Добавляем связь
            cursor.execute(
                "INSERT INTO alternative_elements (alternative_id, element_property_id) VALUES (?, ?)",
                (alt_id, epd_id)
            )
            conn.commit()
            print(f"  Связь успешно добавлена!")
            
        except sqlite3.IntegrityError as e:
            print(f"  Ошибка целостности: {e}")
            print("  Такая связь уже существует")
        except Exception as e:
            print(f"  Неожиданная ошибка: {e}")
            conn.rollback()
        finally:
            conn.close()
            
        self.load_group_elements(alt_name)

    def load_group_elements(self, alt_name):
        """Загружает элементы для выбранной альтернативы (перенесенный функционал из интерфейса альтернатив)"""
        self.tree_group_elements.delete(*self.tree_group_elements.get_children())
        conn = sqlite3.connect("ontology.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", (alt_name,))
        alt_row = cursor.fetchone()
        if not alt_row:
            conn.close()
            return
        alt_id = alt_row[0]
        cursor.execute("""
            SELECT ae.id, ie.name, poe.name, epd.property_value
            FROM alternative_elements ae
            JOIN element_properties_definition epd ON ae.element_property_id = epd.id
            JOIN interface_elements ie ON epd.element_id = ie.id
            JOIN properties_of_elements poe ON epd.property_id = poe.id
            WHERE ae.alternative_id = ?
        """, (alt_id,))
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            self.tree_group_elements.insert("", "end", values=row)

    def delete_element_from_group_alternative(self):
        """Удаляет элемент из альтернативы (перенесенный функционал из интерфейса альтернатив)"""
        selected_item = self.tree_group_elements.selection()
        if selected_item:
            item_values = self.tree_group_elements.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                alt_name = self.alt_select_group.get()
                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM alternative_elements WHERE id = ?", (item_id,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении элемента из альтернативы")
                finally:
                    conn.close()
                self.load_group_elements(alt_name)

    def get_alternatives_list(self):
        """Получает список альтернатив"""
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
            SELECT ie.name || ' - ' || poe.name || ' - ' || epd.property_value
            FROM element_properties_definition epd
            JOIN interface_elements ie ON epd.element_id = ie.id
            JOIN properties_of_elements poe ON epd.property_id = poe.id
        """)
        elements = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not elements:
            return ["Нет элементов с определенными свойствами"]
        return elements

    def delete_set(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                name = item_values[1]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM sets WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_sets()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении множества")
                finally:
                    conn.close()

    def delete_definition(self):
        selected_item = self.tree_definitions.selection()
        if selected_item:
            item_values = self.tree_definitions.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                set_name = item_values[1]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM definitions WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_definitions()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении определения")
                finally:
                    conn.close()

    def delete_interface_element(self):
        selected_item = self.tree_interface_elements.selection()
        if selected_item:
            item_values = self.tree_interface_elements.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                name = item_values[1]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM interface_elements WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_interface_elements()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении элемента")
                finally:
                    conn.close()

    def delete_property(self):
        selected_item = self.tree_properties_of_elements.selection()
        if selected_item:
            item_values = self.tree_properties_of_elements.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                name = item_values[1]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM properties_of_elements WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_properties_of_elements()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении свойства")
                finally:
                    conn.close()

    def delete_property_range(self):
        selected_item = self.tree_property_range.selection()
        if selected_item:
            item_values = self.tree_property_range.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                property = item_values[1]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM property_range WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_property_range()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении определения")
                finally:
                    conn.close()

    def delete_element_property(self):
        selected_item = self.tree_element_properties.selection()
        if selected_item:
            item_values = self.tree_element_properties.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                element = item_values[1]
                property = item_values[2]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM element_properties_definition WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_element_properties()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении свойства")
                finally:
                    conn.close()

    def delete_alternative(self):
        selected_item = self.tree_alternatives.selection()
        if selected_item:
            item_values = self.tree_alternatives.item(selected_item)['values']
            if len(item_values) >= 1:
                item_id = item_values[0]
                alternative = item_values[1]
                set_name = item_values[2]

                conn = sqlite3.connect("ontology.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM alternatives WHERE id = ?", (item_id,))
                    conn.commit()
                    self.load_alternatives()
                except sqlite3.IntegrityError:
                    print("Ошибка при удалении альтернативы")
                finally:
                    conn.close()

    def update_property_values(self, selected_property):
      
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
  
        element = self.element_list.get()
        property = self.properties_list.get()
        value = self.property_values_list.get()

     

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

    def get_set_names_from_definitions(self):
        """Получает список названий множеств из определений"""
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
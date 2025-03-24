import customtkinter

class DataEditor:
    def __init__(self, master):
        self.master = master
        self.visible = False
        
        # Создание фреймов
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

        # По умолчанию скрываем
        self.hide()
    

        self.ontologies = customtkinter.CTkButton(
            self.frame_middle,
            text="Онтологии",
            command=self.button_callback,
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
     
       

        # Размещение кнопок в сетке (точно как в оригинале)
        self.ontologies.grid(row=0, column=0, padx=10, pady=10)
        self.ontology_terms.grid(row=0, column=1, padx=10, pady=10)
        self.ontology_sorts.grid(row=0, column=2, padx=10, pady=10)
        self.window_forms.grid(row=0, column=3, padx=10, pady=10)
        self.definition_window_forms.grid(row=0, column=4, padx=10, pady=10)
        


        
    def show(self):
        """Показывает все фреймы редактора данных"""
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
        """Скрывает все фреймы редактора данных"""
        if self.visible:
            #self.frame_left.grid_remove()
            self.frame_middle.grid_remove()
            self.frame_right.grid_remove()
            self.visible = False

    def button_callback(self):
        """Пример обработчика кнопки"""
        print("Кнопка работает")
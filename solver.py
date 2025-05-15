import customtkinter

class Solver:
    def __init__(self, master):
        self.master = master
        self.visible = False
        
      
        #self.frame_left = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=220)
        self.frame_middle = customtkinter.CTkFrame(master, fg_color="#fbf2fb")
        self.frame_right = customtkinter.CTkFrame(master, fg_color="#fbf2fb", width=400)
       
        self.hide()
    
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
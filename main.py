import customtkinter

class Calc(customtkinter.CTk):

    __btn = [
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", "/"],
        [".", "0", "=", "*"]
    ]

    __pressed_buttons = []

    def __init__(self):
        super().__init__()

        self.title("my app")
        self.grid_columnconfigure((0, 1), weight=0)

        self.input_label = customtkinter.CTkLabel(self, text="", font=("Arial", 18))
        self.input_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="e")

        #Add C button
        button = customtkinter.CTkButton(self, text="C", command=lambda btn_txt="C": self.button_callback(btn_txt), width=50, height=50)
        button.grid(row=0, column=0, columnspan=1, pady=2, padx=2)
        

        for i, row in enumerate(self.__btn):
            for j, text in enumerate(row):
                button = customtkinter.CTkButton(self, text=text, command=lambda btn_txt=text: self.button_callback(btn_txt), width=50, height=50)
                button.grid(row=i+1, column=j, pady=2, padx=2)
        
    def button_callback(self, btn_txt):
        #window size
        #print(self.winfo_width()) 
        #print(self.winfo_height())
        if btn_txt != "=" and btn_txt != "C":
            self.append_button(btn_txt)
        elif btn_txt == "C":
            self.clear_after_c(btn_txt)
        else:
            self.evaluate_expression()

    def append_button(self, btn_txt):
        self.__pressed_buttons.append(btn_txt)
        self.update_input_label()

    def evaluate_expression(self):
        try:
            str_expr = "".join(self.__pressed_buttons)
            result = eval(str_expr)
            self.input_label.configure(text=f"{result}")
        except Exception as e:
            self.input_label.configure(text=f"Error: {e}")

    def update_input_label(self):
        self.input_label.configure(text=" ".join(self.__pressed_buttons))

    def clear_after_c(self, btn_txt):
        self.__pressed_buttons.clear()
        self.input_label.configure(text="".join(self.__pressed_buttons))



app = Calc()
app.mainloop()

#################### TO DO ####################
#
# 1. make it responsive!
# 2. add more options
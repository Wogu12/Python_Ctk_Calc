import customtkinter
from calculations import Calculation

class CalcWindow(customtkinter.CTk):
    _btn = [
        ["(", ")", "\u221A", "x\u00B2"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", "/"],
        [".", "0", "=", "*"],
    ]
    _window_width: float
    _window_height: float 

    _pressed_buttons = []

    def __init__(self, calculation_obj):
        super().__init__()

        self.calculation_obj = calculation_obj

        self._window_width = self.winfo_width()
        self._window_height = self.winfo_height()

        self.title("CTk Calculator")

        self.input_label = customtkinter.CTkLabel(self, text="", font=("Arial", 18))
        self.input_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="e")

        self.bind("<Key>", self.key_pressed)

        button = customtkinter.CTkButton(
            self,
            text="C",
            command=lambda btn_txt="C": self.button_callback(btn_txt),
            width=(self._window_width / 4),
            height=(self._window_height / 4),
        )
        button.grid(row=0, column=0, columnspan=1, pady=2, padx=2, sticky="nesw")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i, row in enumerate(self._btn):
            for j, text in enumerate(row):
                button = customtkinter.CTkButton(
                    self,
                    text=text,
                    command=lambda btn_txt=text: self.button_callback(btn_txt),
                    width=(self._window_width / 4),
                    height=(self._window_height / 4),
                )
                button.grid(row=i + 1, column=j, pady=2, padx=2, sticky="nesw")
                self.grid_rowconfigure(i + 1, weight=1)
                self.grid_columnconfigure(j, weight=1)

    def button_callback(self, btn_txt):
        match btn_txt:
            case "=":
                self.handle_std_equation(self._pressed_buttons)
            case "\r":
                self.handle_std_equation(self._pressed_buttons)
            case "\b":
                self.remove_last_char()
            case "\u221A":
                self.handle_sqrt_equation(self._pressed_buttons)
            case "x\u00B2":
                self.handle_square_equation(self._pressed_buttons)
            case "C":
                self.clear_input()
            case _:
                self.append_button(btn_txt)

    def append_button(self, btn_txt):
        self._pressed_buttons.append(btn_txt)
        self.update_input_label()

    def input_is_clear(self):
        return True if not self._pressed_buttons else False        

    def leave_only_output(self, result):
        self.write_in_input(result)
        self._pressed_buttons.clear()
        self._pressed_buttons.append(str(result))

    def update_input_label(self):
        self.input_label.configure(text=self.calculation_obj.arr_to_str(self._pressed_buttons))

    def clear_input(self):
        self._pressed_buttons.clear()
        self.update_input_label()

    def key_pressed(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/.\r\b":
            self.button_callback(key)

    def remove_last_char(self):
        self._pressed_buttons.pop()
        self.update_input_label()

    def write_in_input(self, var):
        if isinstance(var, (int, float)):
            self.input_label.configure(text=f"{var}")
        else:
            self.input_label.configure(text=var)

    def handler_helper(self, calc_func, *args):
        if not self.input_is_clear():
            result = calc_func(*args)  
            self.leave_only_output(result)
        else:
            self.clear_input()
    
    def handle_std_equation(self, eq):
        self.handler_helper(self.calculation_obj.standard_calculations, eq)

    def handle_sqrt_equation(self, radicant):
        self.handler_helper(self.calculation_obj.sqrt_calculations, radicant)

    def handle_square_equation(self, num):
        self.handler_helper(self.calculation_obj.square_calculations, num)

def main():
    calculation_obj = Calculation()
    app = CalcWindow(calculation_obj)
    app.mainloop()

if __name__ == "__main__":
    main()

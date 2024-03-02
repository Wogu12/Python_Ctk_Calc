import customtkinter
from math import sqrt

class CalcWindow(customtkinter.CTk):
    

    _btn = [
        ["(", ")", "\u221A", "x²"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", "/"],
        [".", "0", "=", "*"]
    ]

    _pressed_buttons = []

    def __init__(self):
        super().__init__()

        _window_width = self.winfo_width()
        _window_height = self.winfo_height()

        self.title("CTk Calculator")

        self.input_label = customtkinter.CTkLabel(self, text="", font=("Arial", 18))
        self.input_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="e")
        
        self.bind('<Key>', self.key_pressed)

        button = customtkinter.CTkButton(self, text="C", command=self.clear_input, width=(_window_width/4), height=(_window_height/4))
        button.grid(row=0, column=0, columnspan=1, pady=2, padx=2, sticky="nesw")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

        for i, row in enumerate(self._btn):
            for j, text in enumerate(row):
                button = customtkinter.CTkButton(self, text=text, command=lambda btn_txt=text: self.button_callback(btn_txt), width=(_window_width/4), height=(_window_height/4))
                button.grid(row=i+1, column=j, pady=2, padx=2, sticky="nesw")
                self.grid_rowconfigure(i+1, weight=1)
                self.grid_columnconfigure(j, weight=1)
        
    def button_callback(self, btn_txt):
        btn_action = {
            "=": self.evaluate_expression,
            "\r": self.evaluate_expression,
            "\b": self.remove_last_char,
            "\u221A": self.sqrt_btn,
            "x²": self.power_btn
        }

        if btn_txt in btn_action:
            btn_action[btn_txt]()
        else:
            self.append_button(btn_txt)

    def append_button(self, btn_txt):
        self._pressed_buttons.append(btn_txt)
        self.update_input_label()

    def input_is_clear(self):
        return True if not self._pressed_buttons else False

    def evaluate_expression(self):
        if not self.input_is_clear():
            try:
                if self.check_equation():
                    result = eval(self.arr_to_str())
                    result = self.is_even(result)
                    self.write_in_input(result)
                    self._pressed_buttons = list(str(result))
                    
            except ZeroDivisionError:
                er_msg = "Error: Divide by zero"
                self.write_in_input(er_msg)
            except SyntaxError:
                er_msg = "Error: Invalid syntax"
                self.write_in_input(er_msg)
            except Exception as e:
                er_msg = f"Error: {e}"
                self.write_in_input(er_msg)
        else:
            self.clear_input()

    def check_equation(self):
        return False if self._pressed_buttons[-1] in "+-*/." else True

    def update_input_label(self):
        self.input_label.configure(text=self.arr_to_str())

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

    def arr_to_str(self):
        str_expr = "".join(self._pressed_buttons)
        return str_expr
    
    def write_in_input(self, var):
        if isinstance(var, (int,float)):
            self.input_label.configure(text=f"{var}")
        else:
            self.input_label.configure(text=var)

    def sqrt_btn(self):
        try:
            result = eval(self.arr_to_str())
            
            sqrt_result = sqrt(result)
            sqrt_result = round(sqrt_result, 10)
            sqrt_result = self.is_even(sqrt_result)
            self.write_in_input(sqrt_result)
            self._pressed_buttons.clear()
            self._pressed_buttons.append(str(sqrt_result))
            
        except Exception as e:
            er_msg = "Error: "+e
            self.write_in_input(er_msg)

    def power_btn(self):
        try:
            result = eval(self.arr_to_str())

            var_scnd_power = result**2
            var_scnd_power = round(var_scnd_power, 10)
            var_scnd_power = self.is_even(var_scnd_power)
            self.write_in_input(var_scnd_power)
            self._pressed_buttons.clear()
            self._pressed_buttons.append(str(var_scnd_power))

        except Exception as e:
            er_msg = "Error: "+e
            self.write_in_input(er_msg)

    def is_even(self, result):
        try:
            num_int = int(result)
            float_num = float(result)
            return str(num_int) if num_int == float_num else result
        except ValueError:
            er_msg = "Invalid input"
            self.write_in_input(er_msg)
            return result


if __name__=="__main__":
    app = CalcWindow()
    app.mainloop()

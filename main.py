import customtkinter
from math import sqrt

class Calc(customtkinter.CTk):
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

        button = customtkinter.CTkButton(self, text="C", command=lambda btn_txt="C": self.button_callback(btn_txt), width=(_window_width/4), height=(_window_height/4))
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
        if btn_txt != "=" and btn_txt != "\r" and btn_txt != "C" and btn_txt != "\b" and btn_txt != "\u221A" and btn_txt != "x²":
            self.append_button(btn_txt)
        elif btn_txt == "C":
            self.clear_input() 
        elif btn_txt == "\b":
            self.remove_last_char()
        elif btn_txt == "\u221A":
            self.sqrt_btn()
        elif btn_txt == "x²":
            self.power_btn()
        else:
            self.evaluate_expression()

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
                self.input_label.configure(text="Error: Divide by zero")
            except SyntaxError:
                self.input_label.configure(text="Error: Invalid syntax")
            except Exception as e:
                self.input_label.configure(text=f"Error: {e}")
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
        self.input_label.configure(text=f"{var}")

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
            self.input_label.configure(text=f"Error: {e}")

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
            self.input_label.configure(text=f"Error: {e}")

    def is_even(self, result):
        try:
            num_int = int(result)
            float_num = float(result)
            return str(num_int) if num_int == float_num else result
        except ValueError:
            self.input_label.configure(text="Invalid input")
            return result


if __name__=="__main__":
    app = Calc()
    app.mainloop()

#################### TO DO ####################
#
# 1. make it responsive! - DONE
# 2. add keyboard input - DONE
# 3. prevent wrong inputs - DONE
# 4. add backspace option - DONE
# 5. change eval() to something else
# 5. add more options
#
################################################
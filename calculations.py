from math import sqrt
import re

class Calculation:

    def standard_calculations(self, equation):
        try:
            if Calculation.check_equation(equation):
                result = round(eval(Calculation.arr_to_str(equation)), 10)
                result = Calculation.is_even(result)
                return result
        except ZeroDivisionError:
            er_msg = "Error: Divide by zero"
            return er_msg
        except SyntaxError:
            er_msg = "Error: Invalid syntax"
            return er_msg
        except Exception as e:
            er_msg = f"Error: {e}"
            return er_msg
        
    def sqrt_calculations(self, equation):
        try:
            result = eval(Calculation.arr_to_str(equation))

            sqrt_result = sqrt(result)
            sqrt_result = round(sqrt_result, 10)
            
            sqrt_result = Calculation.is_even(sqrt_result)
            return sqrt_result

        except Exception as e:
            er_msg = f"Error: {e}"
            return er_msg
        
    def square_calculations(self, equation):
        try:
            result = Calculation.arr_to_str(equation)
            result = re.findall(r'\d+\.\d+|\d+|\D', result)
            if len(result) == 3:
                var_scnd_power = float(result[2])**2
                var_scnd_power = round(var_scnd_power, 10)
                var_scnd_power = Calculation.is_even(var_scnd_power)

                result[2] = str(var_scnd_power)
                result = ''.join(result)
                
                final_res = self.standard_calculations(result)
                return final_res
            elif len(result) == 2:
                return "Error: wrong input"
            elif len(result) == 1:
                var_scnd_power = float(result[0])**2
                var_scnd_power = round(var_scnd_power, 10)
                var_scnd_power = Calculation.is_even(var_scnd_power)
            
                return(var_scnd_power)
        except Exception as e:
            er_msg = f"Error: {e}"
            return(er_msg)

    @staticmethod
    def check_equation(equation) -> bool:
        return False if equation[-1] in "+-*/." else True
    
    @staticmethod
    def arr_to_str(arr) -> str:
        return ''.join(arr)
    
    @staticmethod
    def is_even(result):
        try:
            num_int = int(result)
            float_num = float(result)
            return str(num_int) if num_int == float_num else result
        except ValueError:
            er_msg = "Invalid input"
            return er_msg

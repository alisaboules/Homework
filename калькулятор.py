import math  
import re  
from collections import deque  
  
# Приоритеты операций  
precedence = {  
    '+': 2,  
    '-': 2,  
    '*': 3,  
    '/': 3,  
    '^': 4,  
    'sin': 5,  
    'cos': 5,  
    'sqrt': 5  
}  
  
# Функции  
functions = {  
    'sin': math.sin,  
    'cos': math.cos,  
    'sqrt': math.sqrt  
}  
  
# Константы  
constants = {  
    'pi': math.pi,  
    'e': math.e  
}  
  
def evaluate_expression(expression):  
    def apply_operator(operators, values):  
        operator = operators.pop()  
        right = values.pop()  
          
        if operator in functions:  
            values.append(functions[operator](right))  
        else:  
            left = values.pop()  
            if operator == '+': values.append(left + right)  
            elif operator == '-': values.append(left - right)  
            elif operator == '*': values.append(left * right)  
            elif operator == '/': values.append(left / right)  
            elif operator == '^': values.append(left ** right)  
  
    def greater_precedence(op1, op2):  
        return precedence[op1] > precedence[op2]  
  
    def to_postfix(expression):  
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/^()]|[a-zA-Z]+', expression)  
        operators = []  
        output = []  
        i = 0  
          
        while i < len(tokens):  
            token = tokens[i]  
              
            if token.isdigit() or re.match(r'\d+\.\d+', token):  
                output.append(float(token))  
            elif token in constants:  
                output.append(constants[token])  
            elif token in functions:  
                operators.append(token)  
            elif token == '(':  
                operators.append(token)  
            elif token == ')':  
                while operators and operators[-1] != '(':  
                    output.append(operators.pop())  
                operators.pop()  # Убрать '('  
                  
                # Если перед скобкой была функция  
                if operators and operators[-1] in functions:  
                    output.append(operators.pop())  
            else:  # Оператор  
                while (operators and operators[-1] != '(' and  
                       greater_precedence(operators[-1], token)):  
                    output.append(operators.pop())  
                operators.append(token)  
            i += 1  
          
        while operators:  
            output.append(operators.pop())  
              
        return output  
  
    postfix = to_postfix(expression)  
    values = deque() 
      
    for token in postfix:  
        if isinstance(token, float):  
            values.append(token)  
        else:  
            apply_operator([token], values)  
              
    return values.pop()  
  
def main():  
    number = input("Введите математическое выражение: ") 
    result =  f"\nРезультаты конвертации: {evaluate_expression(number)}"  
    print(result)
      
     
    
if __name__ == "__main__":  
    main()  


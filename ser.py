def detect_base(number_str):  
    """Определяет систему счисления по префиксу числа"""  
    number_str = number_str.lower()  
    if number_str.startswith('0b'):  
        return 2  
    elif number_str.startswith('0o'):  
        return 8  
    elif number_str.startswith('0x'):  
        return 16  
    else:  
        return 10  
  
def convert_number(number_str):  
    """Конвертирует число во все системы счисления"""  
    # Удаляем префиксы для корректного преобразования  
    clean_number = number_str.lower().replace('0b', '').replace('0o', '').replace('0x', '')  
      
    # Определяем исходную систему  
    base = detect_base(number_str)  
    # Переводим в десятичную СС
    decimal_value = int(clean_number, base)  
      
    # Формируем результат конвертации  
    result = {  
        "Исходное число": number_str,  
        "Двоичная": bin(decimal_value),  
        "Восьмеричная": oct(decimal_value),  
        "Десятичная": decimal_value,  
        "Шестнадцатеричная": hex(decimal_value)  
    }  
      
    return result  
  
def main():  
    number = input("Введите число (с префиксом 0b для двоичной/0o для восьмиричной/0x для шестнадцатиричной или без для десятиричной): ")  
    conversion_result = convert_number(number)  
      
    print("\nРезультаты конвертации:")  
    for system, value in conversion_result.items():  
        print(f"{system}: {value}")  
  
if __name__ == "__main__":  
    main()  
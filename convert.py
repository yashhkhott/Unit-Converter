# assignment: programming assignment 3
# author: Yash Khot
# date: 2/19/24
# file: convert.py is a program that emulates a simple SI unit conversion calculator that can convert Fahrenheit into Celsius, miles to kilometers (km), and pounds into kilograms (kg).
# input: User input for conversion type (F, P, M) and respective units.
# output: Conversion result.

def format(num, precision=2):
    formatted_num = round(num, precision)
    formatted_str = str(formatted_num)
    if '.' in formatted_str:
        formatted_str = formatted_str.rstrip('0').rstrip('.')
    return formatted_str

def isfloat(token):
    if token.startswith('-'):
        token = token[1:]
    if token.count('.') == 1:
        left, right = token.split('.')
        return left.isdigit() and right.isdigit()
    return token.isdigit()

def fahrenheit_celsius():
    while True:
        fahrenheit = input("Please enter a temperature in Fahrenheit: ")
        if isfloat(fahrenheit):
            fahrenheit = float(fahrenheit)
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{format(fahrenheit)} Fahrenheit corresponds to {format(celsius)} Celsius.")
            break
        else:
            print("You did not enter a number.")

def miles_km():
    """
    Converts distance from miles to kilometers.
    """
    while True:
        miles = input("Please enter miles: ")
        if isfloat(miles):
            miles = float(miles)
            km = miles * 1.609344
            print(f"{format(miles)} miles corresponds to {format(km)} km.")
            break
        else:
            print("You did not enter a number.")

def pounds_kg():
    while True:
        pounds = input("Please enter pounds: ")
        if isfloat(pounds):
            pounds = float(pounds)
            kg = pounds * 0.45359237
            print(f"{format(pounds)} pounds corresponds to {format(kg)} kg.")
            break
        else:
            print("You did not enter a number.")


print("Welcome to the SI Unit Converter!")
while True:
    print("Please choose one of the following conversions:")
    print("Fahrenheit to Celsius - F")
    print("Pounds to kg - P")
    print("Miles to km - M")
    choice = input().upper()
        
    if choice == 'F':
        fahrenheit_celsius()
    elif choice == 'P':
        pounds_kg()
    elif choice == 'M':
        miles_km()
    else:
        print("You did not choose correctly.")
        continue
        
    response = input("Do you want to continue? [Y/N]: ").upper()
    if response != 'Y':
        print("Goodbye!")
        break


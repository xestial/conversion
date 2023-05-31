import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Temperature Converter Functions

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Other Converter Functions

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    prev_value = 0

    for char in reversed(roman_numeral):
        if char not in roman_dict:
            return None
        if roman_dict[char] < prev_value:
            decimal_num -= roman_dict[char]
        else:
            decimal_num += roman_dict[char]
        prev_value = roman_dict[char]

    return decimal_num

# GUI

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit = combobox_units.get()
        converted_temperature = None

        if unit == 'Fahrenheit to Celsius':
            converted_temperature = fahrenheit_to_celsius(temperature)
        elif unit == 'Celsius to Fahrenheit':
            converted_temperature = celsius_to_fahrenheit(temperature)

        messagebox.showinfo("Temperature Conversion", f"{temperature} {unit.split(' to ')[0]} is equal to {converted_temperature:.2f} {unit.split(' to ')[1]}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid temperature.")

def convert_measurement():
    try:
        value = float(entry_measurement.get())
        unit = combobox_units.get()
        converted_value = None

        if unit == 'Miles to Kilometers':
            converted_value = miles_to_kilometers(value)
        elif unit == 'Kilometers to Miles':
            converted_value = kilometers_to_miles(value)
        elif unit == 'Pounds to Kilograms':
            converted_value = pounds_to_kilograms(value)
        elif unit == 'Kilograms to Pounds':
            converted_value = kilograms_to_pounds(value)
        elif unit == 'Roman to Decimal':
            converted_value = roman_to_decimal(value)

        messagebox.showinfo("Measurement Conversion", f"{value} {unit.split(' to ')[0]} is equal to {converted_value:.2f} {unit.split(' to ')[1]}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid measurement.")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Temperature Conversion Frame
frame_temperature = tk.LabelFrame(window, text="Temperature Conversion", padx=10, pady=10)
frame_temperature.pack(padx=10, pady=10)

# Temperature Conversion Widgets
label_temperature = tk.Label(frame_temperature, text="Temperature:")
label_temperature.grid(row=0, column=0, sticky=tk.E)

entry_temperature = tk.Entry(frame_temperature)
entry_temperature.grid(row=0, column=1)

combobox_units = tk.ttk.Combobox(frame_temperature, values=['Fahrenheit to Celsius', 'Celsius to Fahrenheit'])
combobox_units.grid(row=0, column=2)

button_convert_temperature = tk.Button(frame_temperature, text="Convert", command=convert_temperature)
button_convert_temperature.grid(row=0, column=3)

# Measurement Conversion Frame
frame_measurement = tk.LabelFrame(window, text="Measurement Conversion", padx=10, pady=10)
frame_measurement.pack(padx=10, pady=10)

# Measurement Conversion Widgets
label_measurement = tk.Label(frame_measurement, text="Measurement:")
label_measurement.grid(row=0, column=0, sticky=tk.E)

entry_measurement = tk.Entry(frame_measurement)
entry_measurement.grid(row=0, column=1)

combobox_units = tk.ttk.Combobox(frame_measurement, values=['Miles to Kilometers', 'Kilometers to Miles',
                                                            'Pounds to Kilograms', 'Kilograms to Pounds',
                                                            'Roman to Decimal'])
combobox_units.grid(row=0, column=2)

button_convert_measurement = tk.Button(frame_measurement, text="Convert", command=convert_measurement)
button_convert_measurement.grid(row=0, column=3)

# Start the main loop
window.mainloop()

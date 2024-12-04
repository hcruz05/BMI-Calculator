#tkinter for GUI
import tkinter as tk
from tkinter import messagebox

#BMI calculator using class
class BMICalculator:
    def __init__(self, weight, height, system):
        self.weight = weight
        self.height = height
        self.system = system

    #method to calculate BMI for US or metric
    def calculate_bmi(self):
        if self.system == "US":
            BMI = (self.weight / (self.height * self.height)) * 703
        elif self.system == "Metric":
            #converts to metric units first
            height_in_meters = self.height / 100
            BMI = self.weight / (height_in_meters ** 2)
        return round(BMI, 2)

    #method to determine BMI category from results
    def bmi_category(self, BMI):
        if BMI < 18.5:
            return "Underweight"
        elif 18.5 <= BMI < 25:
            return "Normal"
        elif 25 <= BMI < 30:
            return "Overweight"
        else:
            return "Obesity"

#function to display bmi results on GUI
def display_bmi_results():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        system = system_var.get()

        if system == "US":
            calculator = BMICalculator(weight, height, "US")
        else:
            calculator = BMICalculator(weight, height, "Metric")

        BMI = calculator.calculate_bmi()
        category = calculator.bmi_category(BMI)

        result_label.config(text=f"Your BMI is: {BMI}\nYou fall under the category: {category}")
    #error occurs if user enter invalid number
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

#opens window
root = tk.Tk()
root.title("BMI Calculator")

#label for weight and input
tk.Label(root, text="Enter your weight:").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

#label for height and input
tk.Label(root, text="Enter your height:").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

#label for choosing a system
tk.Label(root, text="Choose System:").grid(row=2, column=0, padx=10, pady=10)
system_var = tk.StringVar()
#defaults to US
system_var.set("US")
#bullet for US
us_radio = tk.Radiobutton(root, text="US Standard (Pounds & Inches)", variable=system_var, value="US")
us_radio.grid(row=2, column=1, padx=10, pady=10)
#bullet for metric
metric_radio = tk.Radiobutton(root, text="Metric (Kilograms & Centimeters)", variable=system_var, value="Metric")
metric_radio.grid(row=3, column=1, padx=10, pady=10)

#button to calculate BMI, "enter/command" runs user's inputs through calculator and displays results
calculate_button = tk.Button(root, text="Calculate BMI", command=display_bmi_results)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#label to show results
result_label = tk.Label(root, text="Your BMI and category will appear here.", font=("Helvetica", 12))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#runs program
root.mainloop()
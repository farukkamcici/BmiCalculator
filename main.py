from tkinter import *


def calculate_bmi():
    try:
        weight_str = weight_entry.get()
        height_str = height_entry.get()

        if not weight_str or not height_str:
            raise ValueError("Please enter values for both weight and height.")

        if not weight_str.isdigit() or not height_str.isdigit():
            raise ValueError("Weight and height must be numbers.")

        weight = float(weight_str)
        height = float(height_str) / 100

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than zero.")

        bmi = weight / (height ** 2)
        category = bmi_category(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f} | Category: {category}")

    except ValueError as e:
        result_label.config(text=str(e), fg="red")


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal range"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese class 1"
    elif bmi < 40:
        return "Obese class 2"
    else:
        return "Obese class 3"


window = Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.config(padx=15, pady=15)

weight_label = Label(text="Enter your weight (kg):", font=("bold", 12))
weight_label.pack()

weight_entry = Entry(width=10)
weight_entry.pack()

height_label = Label(text="Enter your height (cm):", font=("bold", 12))
height_label.pack()

height_entry = Entry(width=10)
height_entry.pack()

calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

result_label = Label(text="", font=("bold", 12))
result_label.pack()

window.mainloop()

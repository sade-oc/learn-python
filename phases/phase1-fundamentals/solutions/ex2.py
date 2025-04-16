#Task 1 
def temperature_conversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Task 2
def math_operations(num1, num2):
    mod = num1 % num2
    floor = num1 // num2
    power = num1 ** num2
    return mod, floor, power


print(temperature_conversion(16))
print(math_operations(10, 2))


#Stretch Task
def BMI_calculator(height, weight):
    BMI = weight / (height ** 2) # BMI formula
    
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 24.9:
        return "Normal weight"
    elif 25 <= BMI < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
print("Your BMI is: ", BMI_calculator(1.75, 70))
#f-string
print(f"Your BMI is: {BMI_calculator(1.75, 70)}")
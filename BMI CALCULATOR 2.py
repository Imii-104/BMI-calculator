
print("Welcome to the BMI Calculator.")
weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")
height_in_float = float(height)
height_in_exponents = height_in_float**2
weight_in_float= float(weight)
BMI = weight_in_float/height_in_exponents
rounded_BMI = round(BMI, 1)

print(f"Your BMI is: {rounded_BMI}")

# Conditions for BMI range
if rounded_BMI < 18.5:
    print("Your BMI is within the underweight range.")
elif rounded_BMI <= 24.9:
    print("Your BMI is within the healthy range.")
elif rounded_BMI <= 29.9:
    print("Your BMI is within the overweight range.")
elif rounded_BMI <= 34.9:
    print("Your BMI indicates class I obesity.")
elif rounded_BMI <= 39.9:
    print("Your BMI indicates class II obesity.")
elif rounded_BMI >= 40:
    print("Your BMI indicates class III obesity.")
    
        


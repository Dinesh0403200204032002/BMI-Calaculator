def calculate_bmi(weight, height):
    # Calculate BMI using the formula
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    # Determine the BMI category
    if bmi < 16:
        return "Severe Thinness"
    elif 16 <= bmi < 17:
        return "Moderate Thinness"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

def main():
    # Get user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Get BMI category
    category = bmi_category(bmi)
    
    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to m
    bmi = weight / (height_m ** 2)
    return bmi

# Function to plot BMI in a pie chart
def plot_bmi(bmi):
    # Define categories and respective ranges
    categories = ['Underweight', 'Normal', 'Overweight', 'Obesity']
    values = [18.5, 25, 30, 40]  # BMI ranges
    colors = ['green', 'yellow', 'orange', 'red']
    
    # Find the category for the calculated BMI
    if bmi < 18.5:
        category_index = 0
    elif bmi < 25:
        category_index = 1
    elif bmi < 30:
        category_index = 2
    else:
        category_index = 3

    # Create the pie chart
    plt.figure(figsize=(7, 7))
    plt.pie([bmi] + [values[category_index] - bmi] + [100-bmi if category_index < 3 else 0], 
             labels=[f'BMI = {bmi:.1f}', f'Gap to next category', 'Others'],
             colors=[colors[category_index]] + ['lightgrey', 'darkgrey'],
             startangle=90, counterclock=False)
    
    # Add arrow
    plt.annotate('', xy=(0.3, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='black', lw=2))

    plt.title('BMI Categories')
    plt.show()

# Main Function
def main():
    weight = int(input("ENTER THE WEIGHT:"))  # Kg
    height = int(input("ENTER THE HEIGHT"))  # Cm

    bmi = calculate_bmi(weight, height)
    print(f'Calculated BMI: {bmi:.1f}')
    plot_bmi(bmi)

if __name__ == '__main__':
    main()

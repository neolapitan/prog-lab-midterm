class GetBMI():
    def findbmi(**kwargs):
        weight = kwargs['weight']
        height = kwargs['height']
        return kwargs['weight']/(kwargs['height']/100)**2

    def bmiclassify(bmi):
        if bmi <= 18.5:
            print("Underweight.")
        elif bmi >= 18.5  and bmi <= 24.9:
            print("Normal.")
        elif bmi >= 25  and bmi <= 29.9:
            print("Overweight.")
        elif bmi >= 30  and bmi <= 34.9:
            print("Obese Class 1.")
        elif bmi >= 35 and bmi >= 39.9:
            print("Obese Class 2.")
        else:
            print("Obese Class 3.")

    if __name__ == "__main__":
        try: 
            weight = int(input("Enter weight (kg):"))
            height = int(input("Enter height in (cm): "))
            bmi = findbmi(height = height, weight = weight)
            print(f"BMI: {bmi:.2f}")
            bmiclassify(bmi)
        except ValueError:
            print("Error. Invalid Input.")


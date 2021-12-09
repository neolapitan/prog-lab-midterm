import sys
#bmi function
def bmi(**kwargs):
    weight = kwargs['weight']
    height = kwargs['height']
    return kwargs['weight']/(kwargs['height']/100)**2

#main function
if __name__ == "__main__":
    try:
        weight = int(input("Enter weight (kg):"))
        height = int(input("Enter height in (cm): "))
        result = bmi(height = height, weight = weight)
        
        #condition
        if result < 18.5:
            print(f"Your Body Mass Index is {result}. This is considered UNDERWEIGHT.")
        elif result >= 18.5 and result <=24.9:
            print(f"Your Body Mass Index is {result}. This is considered NORMAL.")
        elif result >= 25.0 and result <=29.9:
            print(f" Your Body Mass Index is {result}. This is considered OVERWEIGHT.")
        elif result >= 30.0 and result <=34.9:
            print(f"Your Body Mass Index is {result}. This is considered OBESE CLASS I.")
        elif result >= 35.0 and result <=39.9:
            print(f"Your Body Mass Index is {result}. This is considered OBESE CLASS II.")
        else:
            print(f"Your Body Mass Index is {result}. This is considered OBESE CLASS III.")
    except ValueError:
        print("Error. Invalid Input")
        sys.exit(0)

    

class Calculator:
    def acquireValues(self):
        operator = None
        while operator not in ['1', '2']:
            operator = input("Choose Operator \n (1) Add (2) Subtract: ")
            
        myList = input('Enter Series of Numbers Separated by Comma: ').split(',')
        list_of_numbers = []

        for value in myList:
            try:
                temp = float(value)
                list_of_numbers.append(temp)
            except:
                print('Cannot add this value. Could not convert string to float ', value)
                continue       
        return [list_of_numbers, operator]

    def addition(self, val):
        total = 0
        for count in val:
            total += count
        return total

    def subtraction(self, val):
        total = val[0]
        for count in val[1:]:
            total -= count
        return total
 

if __name__ == "__main__":
    def main():
        calculator = Calculator()
        acquire = calculator.acquireValues()
        arrayValues = acquire[0]
        operator = acquire[1]

        if operator == '1':
            print(calculator.addition(arrayValues))
        elif operator == '2':
            print(calculator.subtraction(arrayValues))
        else:
            print("Invalid input")

        run_it_back = input('Try again? [Y/y] - Yes, [Press Any Key] - No: ')
        if run_it_back == 'Y' or run_it_back == 'y':
            main()
        else:
            exit()

    main()
        


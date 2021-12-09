try:
    #asks the user to input rows
    quan = int(input("Input number of rows: "))
    #nested for loop: outer loop -> count the rows, inner loop -> display the numbers
    for rows in range(1, quan+1):
        for num in range(1, rows+1):
            print(num)
        print("\n")
except ValueError:
    print("Error. Enter numbers only.")
    exit()
def numbers():
    try:
        storage = list(map(int, input("Enter Numbers to You Wish to Multiply: ").split('x')))
        return storage
    except ValueError:
        print("Error. Invalid Input.")
        quit()

def multiply(val):
    try:
        total = 1
        for count in val:
            total *= count
        return total
    except TypeError:
        print("Error. Invalid Input.")
        quit()

if __name__ == '__main__':     

    lst = numbers()
    tot_prod = multiply(lst)
    print(f"Total: {tot_prod}")




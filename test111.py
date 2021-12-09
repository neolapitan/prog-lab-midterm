# def add(val1, val2):
#     return val1+val2

# def sub(val1, val2):
#     return val1-val2

def add(*args):
    return args[0] + args[1] + args[2]
   
def sub(**kwargs):
    val1 = kwargs['val1']
    val2 = kwargs['val2']
    val3 = kwargs['val3']
    return val1-val2-val3

#main func
if __name__ == "__main__":

    #print(f"Sum is {add(1,2)}")
    #print("Sum is " + str(add(1,2)))
    #print(f"Diff is {sub(1,2)}")
    
    diff = sub(val1=1, val2=2, val3=3)
    print(f"the difference is {diff}")
    print(f"the sum is {add(1,2,3)}")


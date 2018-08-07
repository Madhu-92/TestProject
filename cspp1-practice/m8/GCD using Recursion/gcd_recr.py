'''
Exercise: GCDRecr
'''
# Write a Python function, gcdRecur(a, b),
# that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcdrecur(var_a, var_b):
    '''
    a, b: positive integers 
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    var_r = var_a % var_b
    var_a = var_b
    var_b = var_r
    if var_r == 0:
        return var_a
    return gcdrecur(var_a, var_b)

def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()

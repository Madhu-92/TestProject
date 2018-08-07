'''
Exercise: GCDIter
'''
# Write a Python function, gcdIter(a, b),
# that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcditer(var_x, var_y):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if var_x > var_y:
        smaller = var_y
    else:
        smaller = var_x
    for i in range(1, smaller + 1):
        if((var_x % i == 0) and (var_y % i == 0)):
            gcd = i
    return gcd

def main():
    ''' main function'''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()

'''
square
'''
# Write a Python function, square, that takes in one number and returns the square of that number.
# This function takes in one number and returns one number.

def square(var_x):
    '''
    x: int or float.
    '''
    # Your code here
    return var_x**2
def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))
main()

'''
Exercise: eval quadratic
'''
# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.
def eval_quadratic(var_a, var_b, var_c, var_x):
    return var_a*(var_x**2)+var_b*var_x+var_c
def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for var_x in range(len(data)):
        temp = str(data[var_x]).split('.')
        if temp[1] == '0':
            data[var_x] = int(float(str(data[var_x])))
        else:
            data[var_x] = data[var_x]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))
main()

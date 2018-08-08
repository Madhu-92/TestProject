'''
Assignment-2 - Paying Debt off in a Year
'''
def payingdebtoffinayear(balance, air):
    #defining pay function
    bal = balance
    pay = 0
    while True:
        i = 12
        bal = balance
        while i != 0:
            ubal = bal - pay
            bal = ubal + ((air / 12.0) * ubal)
            i -= 1
        if bal > 0:
            pay += 10
        else:
            break
    return pay

def main():
    ''' main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(payingdebtoffinayear(data[0], data[1])))
if __name__ == "__main__":
    main()

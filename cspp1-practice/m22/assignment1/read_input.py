'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    b = ""
    a = int(input())
    for i in range(a):
        b += str(input()) + '\n'
        i += 1
    print(b)


if __name__ == '__main__':
    main()

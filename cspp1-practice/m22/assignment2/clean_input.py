'''
Write a function to clean up a given string by removing
the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''clean function'''
    input_string = string
    var_a = re.compile("[a-zA-Z0-9]")
    input_string = var_a.sub('', input_string)
    return input_string

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

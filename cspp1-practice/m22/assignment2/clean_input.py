'''
Write a function to clean up a given string by removing
the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''clean function'''
    var_a = string
    regex = re.compile("[^a-zA-Z0-9]")
    var_a = regex.sub('', var_a)
    return var_a

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

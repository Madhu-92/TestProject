"""
Vowel count
"""
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
def main():
    var_a = input()
    count = 0
    for char in var_a:
        if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
            count+= 1
    print(count)
main()

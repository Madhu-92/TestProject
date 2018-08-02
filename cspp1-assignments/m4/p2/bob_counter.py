'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
    var_a=input()
    var_b=None
    count=0
    for i in range(len(var_a)):
        if i <= (len(var_a)-3):
                var_b = var_a[i:i+3]
                if var_b == "bob":
                        count += 1
    print("Number of times bob occurs" + str(count)) 
main()

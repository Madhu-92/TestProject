varA = input("Enter the input for A: ")
varB = input("Enter the input for B: ")
if type(varA) == type(str) or type(varB) == type(str):
    print("string involved")
elif varA>varB:
    print("bigger")
elif varA<varB:
    print("small")
else:
    print("equal")


'''
Exercise : Odd Tuples
'''
#Write a python function oddTuples(aTup) 
#that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  

def oddTuples(atup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return atup[::2]
def main():
    '''main function'''
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (int(data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()

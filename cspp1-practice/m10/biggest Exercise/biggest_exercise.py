#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    '''y=0
    for x in aDict:
        y += len(aDict[x])
    return max(y)'''
    b = 0
    c = []
    # Your Code Here
    for a in aDict:
        if len(aDict[a]) >= b:
            b = len(aDict[a])
            c = a
    return c

def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))


if __name__== "__main__":
    main()
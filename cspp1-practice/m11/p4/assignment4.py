'''
Exercise: Assignment-4
'''
#We are now ready to begin writing the code that interacts with the player.
#We'll be implementing the playHand function.
#This function allows the user to play out a single hand.
#First, though, you'll need to implement the helper calculateHandlen function,
#which can be done in under five lines of code.


def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    sumof_values_in_hand = 0
    for letters_hand in hand:
        sumof_values_in_hand += hand[letters_hand]
    return sumof_values_in_hand

def main():
    '''main function'''
    n = input()
    adict = {}
    for i in range(int(n)):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    print(calculatehandlen(adict))

if __name__ == "__main__":
    main()

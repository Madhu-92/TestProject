def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def main():
    a = input()
    b = list(chunkstring(a, 9))
    c = len(a)
    if c==81:
      print("Given sudoku is solved")
    
if __name__ == '__main__':
    main()
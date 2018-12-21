def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def main():
    a = input()
    b = list(chunkstring(a, 9))
    try:
      print(len(a))
    except:
      print("An exception occurred")
    
if __name__ == '__main__':
    main()
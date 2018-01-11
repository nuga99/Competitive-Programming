from sys import stdin, stdout 

def main():
 
    # input via readline method
    n = stdin.readline()
 
    # array input similar method
    arr = [int(x) for x in stdin.readline().split()]
    stdout.write(str(summation))
 
# call the main method
if __name__ == "__main__":
    main()    

#Russell Deady
#Fibonacci sequence function in python for practice with recursion
#Last edited on 11/28/21

def Fibonacci(n):
    if (n <= 1):
        return n 
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def main():
    fibNumber = 0
    
    print("Fibonacci Sequence Calculator")
    print("Compute the fibonacci sequence to how many terms?")
    input(fibNumber)

    if (fibNumber < 0):
        print("You must enter a positive integer")
    else:
        print("The Fibonacci sequence is...")
        for i in range(fibNumber):
            print(Fibonacci(i))

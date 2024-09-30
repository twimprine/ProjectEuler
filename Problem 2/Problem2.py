result = 0
counter = 0
endNumber = 4000000

fibA = 1
fibB = 1

def getFib(fibA, fibB):
    return fibA + fibB

def nextFib():
    global fibA, fibB
    nextFib = getFib(fibA, fibB)
    fibA = fibB  # Move fibA to fibB's position
    fibB = nextFib  # Update fibB to the next Fibonacci value
    return fibB

while fibB < endNumber:
    newFib = nextFib()
    print('FibA: ', fibA)
    print('FibB: ', fibB)
    print('Next Fib: ', newFib)
    
    if (newFib % 2) == 0:
        result += newFib  # Add only even Fibonacci numbers
    
    print('Counter: ', counter)
    counter += 1

print('Solution: ', result)

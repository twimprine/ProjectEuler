maxNum = 1000
num = 0
result = 0

while num < maxNum:
    if (num % 3) == 0:
        result += num
    elif (num % 5) == 0:
        result += num
    num += 1
    
print('Solution: ', result)
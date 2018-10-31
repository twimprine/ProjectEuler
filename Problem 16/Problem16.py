# First lets figure out this crazy number...
product = 2**1000

# I'm a fan of initializing variables - I even do it in my sleep... 
numSum = 0

# Cast the product into a string then iterate over each character
for number in str(product):
    # Don't forget to cast it back into a number
    numSum = numSum + int(number)

print(numSum)
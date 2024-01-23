# Function to calculate the exponent of a base raised to the power of exp
# function exponent(base, exp):
    # Initialize result to 1 (base case for any exponent raised to 0)
    
    # Loop through the range of exp
        # Multiply result by the base
    
    # Return the final result

def exponent(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    print(f'{base} raised to the power of {exp} is: {result}')

exponent(2, 5) # 2 raised to the power of 5 is: 32
exponent(5, 4) # 5 raised to the power of 4 is: 625

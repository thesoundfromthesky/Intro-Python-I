# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
def powerOf():
    val = 2
    result = 2
    while True:
        result = result * val
        if result == 65536:
            return result
    
print(powerOf())
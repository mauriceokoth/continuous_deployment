# python program to complete sum of series
# 1! + 2! + 3! + ... + N!  

#Function to return sum
# of 1!, 2! upto N!
def findFactSum(N):
    
    # Initializing the variables
    f = 1
    Sum = 0

    # Calculate the factorial and sum
    # in the loop
    for i in range(1, N + 1):
        f = f * i
        Sum += f

    # Return sum as the final result.
    return Sum

# Driver Code
if __name__ == "__main__":
    N = 5

    #Function call
    print(findFactSum(N))

    # contributed by rakeshsahni
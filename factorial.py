import time   

#final_list = []    

def factorial(n):
    time.sleep(.1)
    result = 1  
    for i in range (1,n+1): 
        result *= i
    return result     

def sum_factorial():
    final_list = [] 
    for i in range(1, 50):
        final_list.append(factorial(i))
    result=sum(final_list)
    print("Final SUM = {}".format(result))
    return result 

if __name__ == "__main__":
    sum_factorial()  

# Outputs this
#Final SUM = 620960027832821612639424806694551108812720525606160920420940314
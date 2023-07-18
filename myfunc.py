# Assume this code is in a file called myfunc.py 

def f1(): 

    x = 1 

    y = 2 

    return x + y 

 

# This part is in a file called pytest_test.py 

#-from myfuncs import f1 
from myfunc import f1
 
def test_myfunc(): 


    #assert myfunc() == 4
    assert f1() == 3
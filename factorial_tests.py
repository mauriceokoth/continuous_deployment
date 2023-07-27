from factorial import *

class TestClass:
    
    
    def test_2(self):
        
        assert findFactSum(1) == 1

    def test_3(self):

        N = 5

        
        assert findFactSum(N) == 153

        #assert len(final_list) == 50
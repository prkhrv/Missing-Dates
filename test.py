import unittest

from main import solution



class Test(unittest.TestCase):
    inp_1 = {'2019-01-01':100,'2019-01-04':115}
    inp_2 = {'2019-01-10':10,'2019-01-11':20,'2019-01-13':10}

    des_out_1 = {'2019-01-01':100,'2019-01-02':105,'2019-01-03':110,'2019-01-04':115}
    des_out_2 = {'2019-01-10':10,'2019-01-11':20,'2019-01-12':15,'2019-01-13':10}
    

    def test_0_case1(self):
        print("Start test 1\n")
        out_1 = solution(self.inp_1)
        print("\nDesired output\n")
        print(self.des_out_1)
        print("\nActual output\n")
        print(out_1)
        self.assertEqual(out_1,self.des_out_1)

        print("\nFinish test 1\n")
    
    def test_1_case2(self):
        print("Start test 2\n")
        out_2 = solution(self.inp_2)

        print("\nDesired output\n")
        print(self.des_out_2)
        print("\nActual output\n")
        print(out_2)
        self.assertEqual(out_2,self.des_out_2)

        print("\nFinish test 2\n")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()



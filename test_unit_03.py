import unittest
from parameterized import parameterized


# 加法操作
def add(x, y):
    z = x + y
    return z


# 最原始的用例执行方法
# print(add(3,4) == 7)
# print(add(3,4) == 8)
# print(add(1.2,4.5) == 5.7)

'''
断言：两个值进行比较
测试断言：预期结果和实际结果进行比较

'''


class TestDemoAdd1(unittest.TestCase):  # 继承unittest类，类名Test开头
    #
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("=======执行setUpClass方法=======")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("=======执行tearDownClass方法=======")
    #
    # def setUp(self) -> None:
    #     print("=======执行setUp方法========")
    #
    # def tearDown(self) -> None:
    #     print("=======tearDown方法========")
    # @parameterized.expand([(7, 3, 4), (4, 0, 4), (1, 3, 4), (7.7, 3.7, 4)])
    # def test_add(self, c, a, b):
    #     res = add(a, b)
    #     self.assertEqual(c, res)


    data = [(7, 3, 4), (4, 0, 4), (7, 3, 2), (7.7, 3.7, 4)]

    @parameterized.expand(data)
    def test_add(self, c, a, b):
        res = add(a, b)
        self.assertEqual(c, res)


    # def test_add01(self):  # 每个方法是一条用例，用例以test开头
    #     print("=====运行01用例======")
    #     res1 = add(3, 4)
    #     self.assertEqual(7,res1))  # asserEqual断言 比较两个值是否相等
    #
    # def test_add02(self):
    #     print("=====运行02用例======")
    #     res2 = add(0, 1)
    #     self.assertEqual(1,res2)
    #
    # def test_add03(self):
    #     print("=====运行03用例======")
    #     res3 = add(-1,3)
    #     self.assertEqual(5.4, add(2,res3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd1('test_add01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()

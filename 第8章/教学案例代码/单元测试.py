import unittest


class HelloWorldTestCase(unittest.TestCase):
    """测试类必须继承自TestCase, 要测试的函数也必须以test开头"""
    
    def setUp(self):
        """每执行一个测试函数之前，都会首先调用这个setUp()方法"""
        print('setUp() method will run first!\n')
    
    
    def test_hello_world(self):
        a = 100
        self.assertEqual(100, a)

    def test_nihao(self):
        a = 10
        self.assertEqual(100, a)

    def test_shijie(self):
        a = 10
        self.assertEqual(100, a)

    def hello_world(self):
        """这个函数不是test开头的，所以将不会被当做测试函数"""
        a = 100
        self.assertEqual(100, a)

# 调用main()会自动进行测试工作
unittest.main()
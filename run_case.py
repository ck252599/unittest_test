import unittest

# 生产一个套件对象
suite = unittest.TestLoader().discover('.', pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(suite)

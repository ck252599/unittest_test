import unittest

# 导入htmlttestrunner
from HTMLTestRunner import HTMLTestRunner

# 定义一个测试报告文件
report_file = 'test_report.html'

# 创建套件
suite = unittest.TestLoader().discover('.', pattern='test*.py')

# 生成一个runner
with open(report_file, 'wb') as  f:
    runner = HTMLTestRunner(f, title='测试报告', description='v1.2测试报告')
    runner.run(suite)

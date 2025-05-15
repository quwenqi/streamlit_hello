# setup.py
from setuptools import setup, Extension

# 定义要编译的C扩展模块
module = Extension('my_calculator', sources=['my_calculator.py'])

# 配置setup函数
setup(
    name='MyCalculator',
    version='1.0',
    description='A simple calculator library',
    ext_modules=[module]
)

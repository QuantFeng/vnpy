# encoding: UTF-8

'''
动态载入所有的策略类
'''

import os
import importlib
import traceback

# 用来保存策略类的字典
STRATEGY_CLASS = {}
import inspect
def get_current_function_name():
    return inspect.stack()[1][3]

#----------------------------------------------------------------------
def loadStrategyModule(moduleName):
    """使用importlib动态载入模块"""
    print "%s.%s" % (__name__,  get_current_function_name())
    try:
        module = importlib.import_module(moduleName)
        
        # 遍历模块下的对象，只有名称中包含'Strategy'的才是策略类
        for k in dir(module):
            if 'Strategy' in k:
                v = module.__getattribute__(k)
                STRATEGY_CLASS[k] = v
    except:
        print '-' * 20
        print ('Failed to import strategy file %s:' %moduleName)
        traceback.print_exc()    


# 遍历strategy目录下的文件
path = os.path.abspath(os.path.dirname(__file__))
# print 'ctaStrategy.__init__ path',  path
for root, subdirs, files in os.walk(path):
    print 'Strategy files', files
    for name in files:
        # 只有文件名中包含strategy且非.pyc的文件，才是策略文件
        if 'strategy' in name and '.pyc' not in name:
            # 模块名称需要模块路径前缀
            moduleName = 'vnpy.trader.app.ctaStrategy.strategy.' + name.replace('.py', '')
            # print 'loadStrategyModule:', moduleName
            loadStrategyModule(moduleName)


# 遍历工作目录下的文件，（我觉得没必要）
workingPath = os.getcwd()
# print 'ctaStrategy.__init__ workingPath',  workingPath
for root, subdirs, files in os.walk(workingPath):
    print 'workingPath files', files
    for name in files:

        # 只有文件名中包含strategy且非.pyc的文件，才是策略文件
        if 'strategy' in name and '.pyc' not in name:
            # 模块名称无需前缀
            moduleName = name.replace('.py', '')
            # print 'loadStrategyModule:', moduleName
            # 这行会出错，因为该目录下无策略
            # loadStrategyModule(moduleName)

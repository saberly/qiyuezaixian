# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:34:42 2017

@author: ice-fire

收集参数有两种打包的方式：一种是以元组的形式打包，另一种则是以字典的形式打包
"""
#==============================================================================
# #以元组的形式打包
# def test(*params):
#     print("有 %d 个参数" %len(params))
#     print("第二个参数是：",params[1])
#     return 0
# 
# test(1,2,3,4,5,6,7,8)
# print("###############")
# a = [1,2,3,4,5,6,7,8]
# #test(a)  #直接将列表名a作为实参将会出错
# print("###############")
# test(*a)
#==============================================================================

#以字典的形式打包
def test(**params):
    print("有 %d 个参数" % len(params))
    print("它们分别是：", params)
# 当参数带两个星号时，传递给函数的任意个key = value实参会被打包进一个字典中
test(a = 1, b = 2, c = 3, d = 4, e = 5)
b = {"one":1, "two":2, "three":3}
test(**b)#解包
    
    
    
    
    
    
    
    
    
    
    
    
    






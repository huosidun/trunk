# coding: utf-8
'''
Created on 2011-12-2

@author: Lv9
'''
import sys;

#所有对象都有引用计数。无论是给一个对象分配一个新名称 还是将其放入一个容器(如列表、元组、字典)中时 该对象的引用计数就会增加 某个对象的引用计数为0时 这个对象就会被销毁
i = 37;
a = 37;#创建一个值为37的对象
b = a;#增加37的引用计数
c = [];
c.append(a);#增加37的引用计数

print("Reference count of the number 37:", sys.getrefcount(a));

#使用del语句或者引用超出作用域(本地变量 本地引用)、或者被重新赋值时,对象的引用计数就会减少 例如:
del a;#减少37的引用计数
del c[0];#减少37的引用计数
b = 42;#减少37的引用计数
print("Reference count of the number 37:", sys.getrefcount(i));#将del用在某个变量名称上之后 这个变量名称将不能再使用

a = [];
b = [];

a.append(b);
b.append(a);

del a;#del语句将会减少a和b的引用次数,并销毁用于引用底层对象的名称。然而为每个对象包含一个对其他对象的引用 所以引用计数不会归0 对象也不会被销毁
del b;#从而导致内存泄露 为了解决这个问题 解释器会定期执行一个循环检测器 搜索不可访问对象的循环并删除它们 循环算法定期运行 因为解释器在执行过程中会分配越来越多的内存 使用gc模块中的函数可以准确调整和控制该算法的行为

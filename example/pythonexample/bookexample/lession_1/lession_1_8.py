# coding: utf-8
'''
Created on 2011-11-29

@author: Lv9
'''
s = set([3, 5, 9, 10, 'o']);#创建一个数值集合
t = set("Hello");#创建一个唯一字符的集合(注意是字符不是字符串) 

print(s);#集合是无序的 无法通过数字进行索引
print(t);#集合中的元素不能重复

#集合支持一系列标准操作,包括并集、交集、差集、对称差集 比如

s.add('o');#添加一项
s.update([2, 4, 7, 8]);#添加多项

a = t | s; #t和s的并集
b = t & s; #t和s的交集
c = t - s; #求差集(项在t中却不在s中)
d = t ^ s; #求对称差集(项在t中或s中,但不会同时出现在二者中))

print(a);
print(b);
print(c);
print(d);

t.remove('H');#删除一项 PS.如果集合中不存在这个项则会出异常..

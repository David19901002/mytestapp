print ("你好")
import time #引入time模块

import random

print(chr(90))              #将数字转换成对应的ASCII
print(ord('A'))             #将ASCII换成对应的数字

l1 = []                     #生成6位随机验证码
for i in range(6):
    r = random.randrange(0,5)
    if r == 2 or r ==4:
        num = random.randrange(0,10)
        l1.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        l1.append(c)
ret = ''.join(l1)            #将列表中个元素以空格为分隔符组合成一个字符串     
print(ret)

s = 'print("hello world")'
r = compile(s, '<string>', 'exec')      #将字符串编译成python代码
exec(r)                                 #执行python代码

s = '8 * 8'
r = eval(s)                             #执行表达式，有返回值
print(r)
r =divmod(33, 5)            #求商及余数
print(r)

s = 'abc'                   #生成hash值，长度固定
print(hash(s))
s = 'abc'
r = isinstance(s, str)      #验证s是否为str的实例，对返回True
print(r)
r = isinstance(s, dict)     #验证s是否为dict的实例，
print(r)
l1 = [10, 20, 30, 40]
r1 = filter(lambda a: a > 10, l1)       #返回值为True，将返回值加入元素
print(list(r1))
r2 = map(lambda a: a + 100, l1)         #将返回值添加到结果中
print(list(r2))

s1 = '萌萌哒'
print(len(s1))                          #计算字符串长度
b1 = bytes(s1, encoding='gbk')          #以gbk格式计算字节长度
print(len(b1))
b2 = bytes(s1, encoding='utf-8')        #以utf-8格式计算字节长度
print(len(b2))

l = [11, 22, 33]
print(max(l))                           #找最大值
print(min(l))                           #找最小值
print(sum(l))                           #求和

r = round(1.7)          #4舍5入
print(r)
r = round(1.4)
print(r)

l1 = ['A', 423, 452356]
l2 = ['C', 423, 31561]
l3 = ['E', 423, 452356]
r = zip(l1, l2, l3)     #对应合并
t = list(r)[0]
ret = ''.join(t)
print(t)
print(ret)









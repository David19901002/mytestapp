#100以内的质数
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

#方法二
import math

def func_get_prime(n):
  return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,n+1))

#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
num = list(func_get_prime(100))   
print(num)


#过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
 
tmplist = filter(is_sqr, range(1, 101))
newlist = list(tmplist)
print(newlist)           



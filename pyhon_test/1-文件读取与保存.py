import pdb  #设置断点
import sys
import time

line1 = "line 1: "
line2 = "line 2: "
line3 = "line 3: "
print ("I'm going to write these to the file.")
target =open("多行写入.txt","w+")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")



f =open("F:\\python_test\\demo.txt","r+")
#print (f.read())
pdb.set_trace()  #设置断点
f1 =f.readlines()
for x in f1:
  print(x)
#w表示写,a+表示附加，r表示读
f.write("\r\n%d"%4)
f.close()
pdb.set_trace()  #设置断点
f =open("a.txt","w+")
for i in range(10):
  f.write("%d\r\n"%(i+1))
f.close()



            



import time;
import support;
ticks=time.time()
print("当前时间戳为：%r"%ticks);

def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


def add(a,b):
    return a+b;

c=add(1,2);
print(c);

# 现在可以调用模块里包含的函数了
support.print_func("Runoob");

try:
    fh = open("testfile", "r")#w
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
fh.close()


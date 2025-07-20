

python的输入总共有3中形式，分别为input()、sys.stdin.readline()、sys.stdin.readlines()，不管是哪种方法，都可以对任何形式的输入进行处理。


前两种一次只能读取一行，后面的可以直接读取多行（感觉用于文件之类的会好很多），3种的返回值均为string类型的。

也就是说，即使你输入的数据是int类型的，他也会把得到的数字转化为字符串。这就需要我们自己对数据进行处理得到我们想要的数据基本类型。
数据的处理通常依赖于strip()方法和split()方法。

strip():去掉字符串首尾的指定字符，默认为换行符和空格。

split():以某个字串或者字符拆分已有的字符串，默认情况以空格拆分。




PS C:\Users\hujun\Documents\GitHub\letcode0> & D:/python/python.exe c:/Users/hujun/Documents/GitHub/letcode0/Input/input2.py
3 4
n=3,m=4
1 2 3 4 
4 5 6 7 
7 8 9 10
[[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

方式1：

单行注释：shift + #（在代码的最前面输入，非选中代码进行注释）

多行注释：同单行一样在每一行的前面输入shift+#

方式2：

单行和多行一样的方式：Ctr+/（前提是选中需要注释的代码）

方式3：

输入''' '''或者""" """，将要注释的代码插在中间

                        
原文链接：https://blog.csdn.net/oMoDao1/article/details/81135170

 
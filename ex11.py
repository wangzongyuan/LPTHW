# --coding:utf8--

print("How old are you?"),
age = raw_input()
print("How tall are you?"),
height = raw_input()
print("How much do you weight?"),
weight = raw_input()

print("So, you're %r old, %r tall and %r heavy" % (age, height, weight))

# 上面的代碼一直跑出這樣的錯誤
'''
File "ex11.py", line 9
    print("So, you're %r old, %r tall and %r heavy"), % (age, height, weight)
                                                      ^
SyntaxError: invalid syntax
'''
'''
經過譯者表示ython2升级为python3后在，2中存在input和raw_input两个类似功能的函数，
在3认为这是冗余函数，于是3将raw_input作为垃圾扔掉了。因此我们在运行2的程序前需要将其中的raw_input全部替换为input。
'''
'''
print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How much do you weight?"),
weight = input()

print("So, you're %r old, %r tall and %r heavy" % (age, height, weight))
'''
"""
但是經過仔細檢查後發現在
print("So, you're %r old, %r tall and %r heavy" % (age, height, weight))中的 heavy"後多了一個,
經過刪除後，程式可以正常運轉
"""

#本章心得，使用過去使用過的格式字符串以及打印，並且學習到Python2與Python3的差異性。另外在debug上更須注意,是否多打。


'''
加分习题

1. 上网查一下 Python 的 raw_input 实现的是什么功能。
2. 你能找到它的别的用法吗？测试一下你上网搜索到的例子。
3. 用类似的格式再写一段，把问题改成你自己的问题。
4. 和转义序列有关的，想想为什么最后一行 '6\'2"' 里边有一个 \' 序列。单引号需要被转义，从而防止它被识别为字符串的结尾。有没有注意到这一点？
'''

#下面是菜鳥教程的範例練習

# !/usr/bin/python3


"""
str = input("請輸入：");
print ("您輸入的內容是： ", str)
"""

# 不Work，出現下面的提示
'''
Traceback (most recent call last):
  File "ex11.py", line 55, in <module>
    str = input("請輸入：");
  File "<string>", line 1
    Hello world
              ^
SyntaxError: unexpected EOF while parsing

'''

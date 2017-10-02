# --coding:utf8--
'''
from sys import argv

script, first, second, third, = argv

print ("The script is called:", script)
print ("Your first Variable is:", first)
print ("Your second Variable is:", second)
print ("Your third Variable is:", third)
print ("Done")
'''
'''

加分习题

1. 给你的脚本三个以下的参数。看看会得到什么错误信息。试着解释一下。
2. 再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名。
3. 将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
4. 记住“模组(modules)”为你提供额外功能。多读几遍把这个词记住，因为我们后面还会用到它。
'''

from sys import argv

script, you, me = argv

print ("The script is called: "), script
print ("Who are you? "), you
print ("Who am I? "), me

# 第一阶段为练习内容，第二阶段为加分习题的练习内容。
# 本章重点，学习怎样使用import 以及 modules的观念。可以在Google上搜寻相关资料

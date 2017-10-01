# --coding:utf8--

age = input ("How old are you? ")
height = input ("How tall are you? ")
weight = input ("How much do you weigh? ")

print("So, you're %r old, %r tall and %r heavy."% (age, height, weight))

'''
加分习题

1. 在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。如果你用的是 Window，那就试一下 python -m pydocraw_input 。
2. 输入 q 退出 pydoc。
3. 上网找一下 pydoc 命令是用来做什么的。
4. 使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。
'''
'''
在Python中有很多很好的工具来生成字符串文档(docstring)，比如说: epydoc、doxygen、sphinx，但始终觉得pydoc还是不错的工具，用法非常简单，功能也算不错，本文主要介绍pydoc.
pydoc是Python自带的模块，主要用于从python模块中自动生成文档，这些文档可以基于文本呈现的、也可以生成WEB 页面的，还可以在服务器上以浏览器的方式呈现！
相關的使用方法，需要更近一步去研究。
'''

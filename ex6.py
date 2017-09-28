# --coding:utf8--

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)
print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

#加分习题

# 1. 通读程序，在每一行的上面写一行注解，给自己解释一下这一行的作用。
# 2. 找到所有的”字符串包含字符串”的位置，总共有四个位置。  ans:5
# 3. 你确定只有四个位置吗？你怎么知道的？没准我在骗你呢。  ans:5?
# 4. 解释一下为什么 w 和 e 用 + 连起来就可以生成一个更长的字符串。

x = "There are %d types of people." % 10 
# 設定變數x 為字串There are %d types of people.其中這段字串為先前說過的模板，故使用%d 顯示數值10 (格式化字符串)
binary = "binary" # 設定變數binary 為字串(string)顯示 
do_not = "don't"  # 設定變數do_not 為字串顯示
y = "Those who know %s and those who %s." % (binary, do_not) 
#設定變數y 為 Those who know %s and those who %s 字串。並使用%s 格式化字符串（字串str顯示）

print(x) # 列印顯示 x
print(y) # 列印顯示 y 
print("I said: %r." % x) # 使用%r 顯示全部列印 其中%的值為x
print("I also said: '%s'." % y) # 使用%s ，值為y

hilarious = False #設定布爾值為False
joke_evaluation = "Isn't that joke so funny?! %r" #設定變數joke_evaluation的對應值（String）
print(joke_evaluation % hilarious) #列印出joke_evaluation 及對應格式化字符串%

w = "This is the left side of..." #設定變數w
e = "a string with a right side." #設定變數e
print(w + e) # 列印出 w 與 e

'''
心得：
本章节学习到加强对于格式化字符串的用法
以及变数的用法。
并起在练习中大量使用#字注释
'''

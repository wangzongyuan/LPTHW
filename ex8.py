# --coding:utf8--
formater = "%r %r %r %r"

print(formater % (1, 2, 3, 4))
print(formater % ("one", "two", "three", "four"))
print(formater % (True, False, False, True))
print(formater % (formater, formater, formater, formater))
print(formater % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	))
# 上面這句語法在練習的時候有出現TypeError ，因為漏掉,的部分。須留意
# 下面是習題中的轉換練習。將原本習題的 %r轉換為%s

formater = "%s %s %s %s"

print(formater % (1, 2, 3, 4))
print(formater % ("one", "two", "three", "four"))
print(formater % (True, False, False, True))
print(formater % (formater, formater, formater, formater))
print(formater % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	))

'''
加分习题

1. 自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误。
2. 注意最后一行程序中既有单引号又有双引号，你觉得它是如何工作的？

心得
本章练习print的用法。并且使用%S与%r 格式化字符串的用法练习

'''

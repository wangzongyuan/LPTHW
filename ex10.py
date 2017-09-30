# --coding:utf8--

'''
	本章學習重點，\ 的使用方式。 \\在Python中，更多所謂的轉義序列（escape sequences）。
	另一個重要的轉義序列，是使用單引號或雙引號。轉義
'''

"I am 6'2\" tall." #將字符串中的雙引號轉義
'I am 6\'2" tall.' # 將字符串中的單引號轉義

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

'''
	顯示結果為下：
		I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass

'''


# 加分习题

# 1. 上网搜索一下还有哪些可用的转义字符。
# 2. 使用\n ''' (三个单引号)取代三个双引号，看看效果是不是一样的？
# 3. 将转义序列和格式化字符串放到一起，创建一种更复杂的格式。
# 4. 记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。 将 %r 和 %s 比较一下。 注意到了吗？%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。

# 以下為加分習題2. 使用\n '''取代看看效果是否相同


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Gress
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# 轉意字符補充
# 轉意字符 		描述
# \			續行符
# \\			反斜杠符號	
# \'			單引號
# \"			雙引號
# \a 			響鈴
# \b 			退格（backspace）
# \e 			轉義
# \000 		空
# \n 			換行
# \v			縱向制表符
# \t 			橫向制表符
# \r 			回車
# \f 			換頁
# \oyy 		八進制yy代表的字符
# \xyy 		十進制yy代表的字符
# \other		其他的字符以普通的格式輸出


'''
本章遇見的問題與心得：
在進行最後註釋轉義字符的補充的時候，程式的運算跑不起來，透過逐步重新檢查。發現是上面那段補充出問題。
因為使用了三引號的註釋。
所以出現以下訊息
	ValueError: invalid \x escape
後更改為#註釋後即可run 
看來，未來使用多引號註釋的時機更需要小心。
另外\ 轉義字符的用法，在練習的時候，還不清楚他的作用，但是查詢了補充的字符後，對於相對應的功能與敘述，
可以在代碼中看得出來，也增加了一分了解。

'''

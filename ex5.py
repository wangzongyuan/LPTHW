# --coding:utf8--
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s."% my_name)
print("He's %d inches tall."% my_height)
print("He's %d pounds heavy"% my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."%(my_eyes,my_hair))
print("His teeth are usually %s depanding on the coffee."% my_teeth)
# This line is tricky,  try to get it exactly right
print("If i add %d,%d and %d I get %d."% (my_age, my_height, my_weight, my_age + my_height + my_weight))

# 以下練習題
# 加分习题

# 1. 修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不只是你使用``=``赋值过的地方。
# 2. 试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。
# 3. 在网上搜索所有的 Python 格式化字符。
# 4. 试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s."% name)
print("He's %d inches tall."% height)
print("He's %d pounds heavy"% weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."%(eyes,hair))
print("His teeth are usually %s depanding on the coffee."% teeth)
# This line is tricky,  try to get it exactly right
print("If i add %d,%d and %d I get %d."% (age, height, weight, age + height + weight))

'''                        #第一次嘗試多引號多行註解
以下為python 格式化字符的類型。

print("I'm %s.I'm %d years old."%)('Wang',28)
I'm %s.I'm %d years old.此為模板，%s 為第一個格式符，代表一個字符串。%d為第二個字符串,表示整數。
('Wang',28)的兩個元素,wang和28為替換%s跟%d的真實值。

學習來源：http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html

%s 字符串（採用str()的顯示）
%r 字符串 (採用repr()的顯示)
%c 單個字符
%b 二進制整數
%d 十進制整數
%i 十進制整數
%o 八進制整數
%x 十六進制整數
%e 指數 （基底寫為e）
%E 指數 （基底寫為E）
%f 浮點數
%F 浮點數（與上相同）
%g 指數（e）或是浮點數（根據顯示長度）
%G 指數（E）或是浮點數（根據顯示長度）

%% 字符"%"

'''
#下面為格式化字符的練習
print("I am %s.I am %d years old."% ('bill' , 24))

weight_lbs = 199 #lbs
weight_kg = weight_lbs * 0.45359
height_inch = 60
height_m = height_inch * 0.0254

print("I am %d kg and %d m"%(weight_kg, height_m)) # 嘗試用跟前面一樣%d 表達二進位
print("I am %i kg and %i m"%(weight_kg, height_m)) # 嘗試用%i 看看會有什麼變化 二進位
print("I am %o kg and %o m"%(weight_kg, height_m)) # 嘗試使用%o 八進制 
print("I am %f kg and %f m"%(weight_kg, height_m)) # 嘗試使用%f 看看是否會顯示小數點
#顯示後發現八進位可能需要google學習一下 八進制相關資料

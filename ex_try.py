# --coding:utf8--

age = input ("How old are you? ")
height = input ("How tall are you (m)? ")
weight = input ("How much do you weigh (Kg)? ")

# BMI 公式為 體重 除以身高的平方
BMI = weight / height ** 2

print ("Your BMI is %r " % BMI)

# 這是今天在路上想到昨天的練習，覺得可以試著用BMI的公式寫寫看。
# 意外的完成了變數跟input的練習還有print的練習。
# 公式的部分，有點錯誤，所以運算結果有出點問題，但是修正後，還可以接受
# 這算是Hello World之外，我真正寫的第一個程式。值得紀念！

# 其中使用input 与 变数，其中透过print将变数最后的值显示出来。与使用者及计算机互动

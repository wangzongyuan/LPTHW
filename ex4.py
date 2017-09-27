# --coding:utf8--
cars = 100
space_in_a_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passenger / cars_driven

print('There are'), cars, ('cars available.')
print("There are only"), drivers, ("drivers available.")
print("There will be"), cars_not_driven, ("empty cars today.")
print("We can transport"), carpool_capacity, ("people today.")
print("We have"), passenger, ("to carpool today.")
print("We need to put about"), average_passengers_per_car, ("in each car.")
print("Hello " ,cars ) # 我在測試print()函數的用法
print("Yo~", cars) # 這是測試的用的

# 以下為練習題
# 1. 我在程序里用了 4.0 作为 space_in_a_car 的值，这样做有必要吗？如果只用 4 会有什么问题?
# 2. 记住 4.0 是一个“浮点数”，自己研究一下这是什么意思。
# 3. 在每一个变量赋值的上一行加上一行注解。
# 4. 记住 = 的名字是等于(equal)，它的作用是为东西取名。
# 5. 记住 _ 是下划线字符(underscore)。
# 6. 将 python 作为计算器运行起来，就跟以前一样，不过这一次在计算过程中使用变量名来做计算，常见的变量名有 i, x, j 等等。

# weight = A
# height = B 

A = 66
B = 1.80

BMI = A / B**2


print(BMI)

# 遇到的问题，变量操作上还不成熟，哪些命名可以使用，哪些不行，在制作BMI算式的时候，weight与w的转换上，出现问题。还需要找寻资料更近一步的了解

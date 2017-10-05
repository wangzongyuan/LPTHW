# --coding:utf8-- 
from sys import argv

script, user_name = argv 

prompt = '>'

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s ?" % user_name)
likes = input (prompt)

print ("Where do you live %s?" % user_name)
lives = input (prompt)

print ("What kind of computer do you have?")
computer = input (prompt)

print ("""
	Alright, so you said %r about liking me.
	You live in %r. Not sure where that is.
	And you have a %r computer. Nice.
	"""
	% (likes, lives, computer)
	)


'''
修正過後還是跑這個訊息！
Traceback (most recent call last):
  File "ex14.py", line 4, in <module>
    script, user_name = argv 
ValueError: need more than 1 value to unpack
明日在排除，目前無法思考了。
'''

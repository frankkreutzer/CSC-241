Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randrange(1, 7)
3
>>> random.randrange(1, 7)
6
>>> random.randrange(1, 7)
6
>>> random.randrange(1, 7)
6
>>> random.randrange(1, 7)
4
>>> random.randrange(1, 7)
5
>>> random.randrange(1, 7)
4
>>> random.randrange(1, 7)
6
>>> random.random()
0.6932052577147882
>>> random.random()
0.004132743447264664
>>> random.random()
0.07271266610310445
>>> random.random()
0.5174839958138749
>>> random.random()
0.2857011947617255
>>> random.randrange(1, 7) + random.randrange(1, 7)
5
>>> lst = ['one', 'two', 'three', 'four', 'five']
>>> lst
['one', 'two', 'three', 'four', 'five']
>>> random.shuffle(lst)
>>> lst
['three', 'four', 'one', 'two', 'five']
>>> random.choice(lst)
'five'
>>> random.choice(lst)
'five'
>>> random.choice(lst)
'two'
>>> random.choice(lst)
'two'
>>> random.smaple(lst, 2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    random.smaple(lst, 2)
>>> random.sample(lst, 2)
['two', 'four']
>>> random.sample(lst, 2)
['five', 'three']
>>> random.sample(lst, 2)
['three', 'five']
>>> random.sample(lst, 2)
['one', 'five']
>>> random.sample(lst, 2)
['three', 'four']
>>> random.sample(lst, 2)
['five', 'three']
>>> 

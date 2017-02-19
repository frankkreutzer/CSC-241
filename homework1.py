Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

2.12
-----------------------------------------------
>>> s1 = '-'
>>> s2 = '+'

>>> s1 + s2
'-+'

>>> s1 + s2 + s1
'-+-'

>>> s2 + s1 + s1
'+--'

>>> (s2 + s1 + s1) * 2
'+--+--'

>>> (s2 + s1 + s1) * 10 + s2
'+--+--+--+--+--+--+--+--+--+--+'

>>> (s2 + s1 + (s2 * 3) + (s1 * 2)) * 5
'+-+++--+-+++--+-+++--+-+++--+-+++--'

2.14
-----------------------------------------------
>>> s = 'goodbye'
>>> s
'goodbye'

>>> s[0] == 'g'
True

>>> s[6] == 'g'
False

>>> s[0] == 'g' and s[1] == 'a'
False

>>> s[-2] == 'x'
False

>>> s[3] == 'd'
True

>>> s[0] == s[-1]
False

>>> s[-4] == 't' and s[-3] == 'i' and s[-2] == 'o' and s[-1] == 'n'
False

2.15
-----------------------------------------------
>>> len('anachronistically') - len('counterintuitive')
1

>>> 'misinterpretation' < 'misrepresentation'
True

>>> 'e' not in 'floccinaucinihilipilification'
True

>>> len('counterrevolution') == len('counter') + len('resolution')
True

2.16
-----------------------------------------------
>>> a = 6
>>> a
6

>>> b = 7
>>> b
7

>>> c = (a + b) / 2
>>> c
6.5

>>> inventory = ['paper', 'staples', 'pencils']
>>> inventory
['paper', 'staples', 'pencils']

>>> first = 'John'
>>> first
'John'

>>> middle = 'Fitzgerald'
>>> middle
'Fitzgerald'

>>> last = 'Kennedy'
>>> last
'Kennedy'

>>> fullname = first + ' ' + middle + ' ' + last
>>> fullname
'John Fitzgerald Kennedy'

2.17
-----------------------------------------------
>>> 17 + -9 < 10
True

>>> len(inventory)  > 5 * len(fullname)
False

>>> c <= 24
True

>>> a < 6.75 < b
True

>>> len(first) < len(middle) < len(last)
False

>>> len(inventory) == 0 or len(inventory) > 10
False

2.18
-----------------------------------------------
>>> flowers = ['rose', 'bougainvillea', 'yucca', ' marigold', 'daylilly', 'lilly of the valley']
>>> flowers
['rose', 'bougainvillea', 'yucca', ' marigold', 'daylilly', 'lilly of the valley']

>>> 'potato' in flowers
False

>>> thorny = flowers[0], flowers[1], flowers[2]
>>> thorny
('rose', 'bougainvillea', 'yucca')

>>> poisonous = flowers[-3], flowers[-2], flowers[-1]
>>> poisonous
(' marigold', 'daylilly', 'lilly of the valley')

>>> dangerous = thorny + poisonous
>>> dangerous
('rose', 'bougainvillea', 'yucca', ' marigold', 'daylilly', 'lilly of the valley')

2.19
-----------------------------------------------
>>> answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']

>>> numYes = answers.count('Y')
>>> numYes
5

>>> numNo = answers.count('N')
>>> numNo
6

>>> percentYes = (numYes/11) * 100
>>> percentYes
45.45454545454545

>>> answers.sort()
>>> answers
['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']

>>> f = answers.index('Y')
>>> f
6

2.20
-----------------------------------------------
>>> s = 'cat'
>>> s = s[2] + s[1] + s[0]
>>> s
'tac'


2.22
-----------------------------------------------
>>> lst = [3, 7, -2, 12]
>>> r = max(lst) - min(lst)
>>> r
14

2.24
-----------------------------------------------
>>> grades = ['A', 'D', 'D', 'C', 'A', 'A', 'B', 'B', 'B', 'F', 'A', 'C', 'C', 'C', 'B', 'B', 'F', 'B', 'A']
>>> grades.sort()
>>> count = grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')
>>> count
(5, 6, 4, 2, 2)

2.28
-----------------------------------------------
>>> lst = [5, 9, 2, -3, 10, 17, 20, 11, 8, 1, 0, 6, -1]

>>> lst.index(20)
6

>>> lst[6]
20

>>> lst.sort()
[-3, -1, 0, 1, 2, 5, 6, 8, 9, 10, 11, 17, 20]
>>> lst.reverse()
>>> lst
[20, 17, 11, 10, 9, 8, 6, 5, 2, 1, 0, -1, -3]

>>> lst.append(lst.pop(0))
>>> lst
[17, 11, 10, 9, 8, 6, 5, 2, 1, 0, -1, -3, 20]

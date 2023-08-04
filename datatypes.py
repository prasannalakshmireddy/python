Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3]
l+=(4,5,6)
l
[1, 2, 3, 4, 5, 6]

s={1,2,3,4,5}
s+={'a':20,'b':30}
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s+={'a':20,'b':30}
TypeError: unsupported operand type(s) for +=: 'set' and 'dict'
s="pyspiders"
s[0]
'p'
s[::-2]
'seisp'
s[0::4]
'pis'
s=s+"hello"
s
'pyspidershello'
s=s+" hello"
s
'pyspidershello hello'

s="hello"
s+="haii "+s
s
'hellohaii hello'



s="hiii"
s+="hello"
s
'hiiihello'
>>> s[:4]+" "+s[4:]
'hiii hello'
>>> s
'hiiihello'
>>> s[:4]+" how r u "+s[4:]
'hiii how r u hello'
>>> s
'hiiihello'
>>> s[:2]+s[4:]
'hihello'
>>> l=[1,2,['a','b'],"spiders",5,6,2]
>>> l[-1]
2
>>> l[0]=[20,30]
>>> l
[[20, 30], 2, ['a', 'b'], 'spiders', 5, 6, 2]
>>> l[2:2]=[]
>>> l
[[20, 30], 2, ['a', 'b'], 'spiders', 5, 6, 2]
>>> del l[2]
>>> l
[[20, 30], 2, 'spiders', 5, 6, 2]
>>> 
>>> 
>>> 
>>> t=(1,2,3,,45)
SyntaxError: invalid syntax
>>> 
>>> t=(1,2,3,4,5)
>>> t[0]
1
>>> t[:::]
SyntaxError: invalid syntax
>>> t[::1]
(1, 2, 3, 4, 5)
>>> t[0:2]+(30,40,50)+t[2:]
(1, 2, 30, 40, 50, 3, 4, 5)
>>> t
(1, 2, 3, 4, 5)
>>> t[0:2]+t[3:]
(1, 2, 4, 5)
>>> s={1,2,2,5,6}
>>> s|={2,3,7}
>>> s
{1, 2, 3, 5, 6, 7}

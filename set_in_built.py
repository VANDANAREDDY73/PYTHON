Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
S = {23,'a',(23,45),'v','pongal'}
S.pop()
'pongal'
S.pop()
'v'
s.pop()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.pop()
NameError: name 's' is not defined. Did you mean: 'S'?
S.pop()
23
S
{(23, 45), 'a'}
S.pop()
(23, 45)
S.pop()
'a'
S.pop()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    S.pop()
KeyError: 'pop from an empty set'
K = {4,'34',7,90}
K.discard('34')
K
{90, 4, 7}
K.discard(4)
K
{90, 7}
K.discard(90)
K
{7}
K.discard(7)
K
set()
K.discard(set())
k
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    k
NameError: name 'k' is not defined. Did you mean: 'K'?
K
set()
R = {4,6,1,'34',7,90}
R.remove(6)
R
{1, 4, '34', 7, 90}
K.remove(98)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    K.remove(98)
KeyError: 98
K.remove(False)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    K.remove(False)
KeyError: False
K.remove(True)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    K.remove(True)
KeyError: True
S = {4,5}
S.update('abc')
S
{'c', 4, 5, 'b', 'a'}
S.update(1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    S.update(1)
TypeError: 'int' object is not iterable
S.update((12))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    S.update((12))
TypeError: 'int' object is not iterable
S.update((12,))
S
{'c', 4, 5, 12, 'b', 'a'}
S = set()
S.add(4)
S
{4}
S.add(4)
S
{4}
S.add(3,6)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    S.add(3,6)
TypeError: set.add() takes exactly one argument (2 given)
S.add((3,4))
S
{4, (3, 4)}
S.add(True)
S
{True, 4, (3, 4)}
S.add(1)
S
{True, 4, (3, 4)}
S.add()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    S.add()
TypeError: set.add() takes exactly one argument (0 given)
>>> S1={10,19,20}
>>> S2={19,20,100}
>>> S1.difference(S2)
{10}
>>> S2.difference(S1)
{100}
>>> S3={('A','C',E)}
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    S3={('A','C',E)}
NameError: name 'E' is not defined
>>> S3={('A','C','E')}
>>> S4={('B','A','E')}
>>> S3.difference(S4)
{('A', 'C', 'E')}
>>> S4.difference(S3)
{('B', 'A', 'E')}
>>> S3={('A','C','E'),('B','A','E')}
>>> S4={('B','A','E'),('H','U','B')}
>>> S3.difference(S4)
{('A', 'C', 'E')}
>>> S4.difference(S3)
{('H', 'U', 'B')}

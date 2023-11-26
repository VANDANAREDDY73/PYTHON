fileob = open('read.txt')
print(fileob.tell())
print(fileob.read())
print(fileob.tell())
print(fileob.readable())
print(fileob.readline())
fileob.seek(0)
print(fileob.readlines())
print(fileob.tell())
fileob.close()

solution:
0
Python full stack developer
,Sql is a data base
,Web technologies is used for designing web pages10
abc
hello
hi
117
True

['Python full stack developer\n', ',Sql is a data base\n', ',Web technologies is used for designing web pages10\n', 'abc\n', 'hello\n', 'hi']
117

import os

file = open('hello.txt', 'w')
file.write('hello !!!!!!!!!!!!!!!!')
file.write('hello L!!!!!!!!!!!')
file.close()
print(os.getcwd())

file2 = open('hello.txt', 'w')
file2.write('tuesday !!!!!!!!!!!!!!!!\n')
file2.write('tuesday L!!!!!!!!!!!\n')
file2.close()
print(os.getcwd())

file = open('hello.txt', 'r')
lines = file.read()
print(lines)
file.close()

'''
file = open('hello.txt','r')
lines = file.readlines()
print(lines)
file.close()


file = open('hello.txt','a')
file.writelines('world\nbutterfly')

file.close() '''

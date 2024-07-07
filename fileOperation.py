import os
print(os.path.join('t1','t2'))
print(os.sep)
print(os.getcwd())
print(os.chdir('..\\'))
print(os.getcwd())
os.mkdir('folderTest')
print(os.chdir('.\\folderTest'))
print("mm   "+os.getcwd())
print(os.chdir('..\\pythonProject'))
print(os.getcwd())

print(os.chdir('C:\\'))
print('mmm  '+os.getcwd())

print(os.chdir('.\\users\\mvmgr'))
print(os.getcwd())

print(os.path.abspath(".\\PycharmProjects\\pythonProject"))
print(os.getcwd())

print(os.path.abspath("phoneAndEmail.py"))
print(os.path.isabs("phoneAndEmail.py"))
print(os.path.isfile(r'C:\Users\...\PycharmProjects\pythonProject\phoneAndEmail.py'))

print(os.getcwd())
print(os.chdir('.\\PycharmProjects\\pythonProject'))
print(os.getcwd())


file = open(os.path.join(os.getcwd(),'sweet.txt'), 'w')
file.write('sweet talks')
file.close()


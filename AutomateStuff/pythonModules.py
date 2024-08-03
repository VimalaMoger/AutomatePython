import glob
myfiles =  glob.glob(r'C:\Users\mvmgr\Documents\pycharmprojects\*.txt')
#print(myfiles)

for file in myfiles:
    with open(file, 'r') as fileName:
        print('/////////////////////////////////////////////////////////////\n')
        print(f'The contents in the name of file called {file}\n')
        print(fileName.read())


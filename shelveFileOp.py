import os
import shelve
import shutil

shelfFile  = shelve.open('hello')
shelfFile['cats']= {'aa','bb','cc','dd','ff'} #[]
print(shelfFile.get('cats'))
print(shelfFile.keys())
print(shelfFile.values())
shelfFile.close()

listFolders = os.walk(r'C:\users\mvmgr\PycharmProjects')
for fo, subfo, files in listFolders:
    print('folders ' + str(fo))
    print('subfolders '+ str(subfo))
    print('files'+ str(files))
    for subfolder in subfo:
        if subfolder.endswith('Test'):
            print(subfolder)
            os.renames(subfolder,'test')
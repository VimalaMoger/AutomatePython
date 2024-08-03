import  re
regDot = re.compile(r'.*')# dot is wild card character
moObj = regDot.search('serve the public trust\n protect the innocence\n uphold the law')
print(moObj.group())

regDot = re.compile(r'.*', re.DOTALL)#truly match \n new line as well
moObj = regDot.search('serve the public trust\n protect the innocence\n uphold the law')
print(moObj.group())

regDot = re.compile(r'[aeiou]', re.IGNORECASE)
moObj = regDot.findall('SErve the PUblIc trust\n protect the Innocence\n uphold the law')
print(moObj)
regDot = re.compile(r'World!$')
moObj = regDot.findall('Hello World!')
print(moObj)
regDot = re.compile(r'^Hello World!$')
moObj = regDot.findall('Hello World!')
print(moObj)

#word processor program
namesReg = re.compile(r'agent \w')
moObj = namesReg.findall('agent alice verses agent bob')
print(moObj)

namesReg = re.compile(r'agent \w+')
moObj = namesReg.findall('agent h alice verses agent j bob')
print(moObj)

moObj = namesReg.sub('Sean','agent h alice verses agent j bob')
print(moObj)

moObj = namesReg.sub('Sean','agent alice verses agent bob')
print(moObj)

namesReg = re.compile(r'agent (\w)\w+')
moObj = namesReg.findall('agent alice verses agent bob')
print(moObj)

moObj = namesReg.sub('gg','agent alice verses agent bob')
print(moObj)

moObj = namesReg.sub(r'agent  \1***', 'agent alice verses agent bob')
print(moObj)

namesReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moObj = namesReg.findall('agent alice 765-456-3456 verses agent bob 765-234-1234')
print(moObj)
namesReg = re.compile(r'(\d\d\d-)*\d\d\d-\d\d\d\d')
moObj = namesReg.findall('agent alice 765-456-3456 verses agent bob 765-234-1234')
print(moObj)
















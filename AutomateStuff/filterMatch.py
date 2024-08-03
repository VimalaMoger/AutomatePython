import pyperclip, re
phoneRegex = re.compile(r'((\d\d\d).\s\d\d\d-\d\d\d\d)')
pyperclip.copy('''


Eric Atchison

Vice President for Strategic Research

(501) 660-1015

eatchison@asusystem.edu

Julie Bates

Executive Vice President

(501) 660-1002

jbates@asusystem.edu

Katherine Berry

Special Assistant to the President

(501) 660-1000

kaberry@asusystem.edu
''')
text = pyperclip.paste()
mo = phoneRegex.findall(text)
print(mo)
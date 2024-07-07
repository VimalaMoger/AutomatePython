import re

phoneNum = "512-234-1234"
ph = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #create reg expression object
mo = ph.search('call me at 512-453-1234')
print(ph.findall(phoneNum))
#call match objects group method to get the matched string


ph = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  #python groups with parenthisis find mo.group() or mo.group(1)
#literally looking for paranthisis in a phone number like (512)-234-1234 using backslash character
#also use pipe to give options in finding one of many possible groups

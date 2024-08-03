#! python3
# Todo create regex fpr phone numbers
#todo: create a regex for email addresses
# todo: get the text off the clipboard
# todo: extract the email/phone form this text
# todo: copy the extracted  email/phone to the clipboard
import re
import pyperclip

phoneReg = re.compile(r'''
#434-567-2345, 678-4567,(123) 435-7685, ext 2345, ext. 12345,x12345
(
((\d\d\d)|(\(\d\d\d\)))?     #area code (optional)
(\s|-)                          #first seperator
\d\d\d                            #first 3 digits
 -                          #separtor
\d\d\d\d                            #last 4 digits
(((ext(\.)?\s)|x)(\d{2,5}))?                        #extension (optional)
                 #one extension starts with x
)
''', re.VERBOSE)

emailReg = re.compile(r'''
#email@stand.com
[a-zA-Z0-9.+_]+                #name part
@      #@ symbol
 [a-zA-Z0-9.+_]+     #domain name part
 
''', re.VERBOSE)
text = '''
Alisha Lewis
Associate Director of Communications
Email: Communications@adhe.edu,  Communication_s@adhe.edu
Phone: (501) 320-3095 ext1234
Fax: 501-371-8000, 678-345-3456
434-567-2345, 678-4567,(123) 435-7685, ext 2345, ext. 12345,x12345'''

phoneObj = phoneReg.findall(text)
print(phoneObj)
moObj = emailReg.findall(text)
print(moObj)

listsOfPhoneNum = []
for num in phoneObj:
    listsOfPhoneNum.append(num[0])
print(listsOfPhoneNum)
print('\n'.join(listsOfPhoneNum))
print('\n'.join(moObj))
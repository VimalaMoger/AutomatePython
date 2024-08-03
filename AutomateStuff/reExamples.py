import re
text = '23 _4wddd 234 _4wddd'
phoneRegex = re.compile(r'\d\d?\s\w?')
mo = phoneRegex.findall(text)
print(mo)
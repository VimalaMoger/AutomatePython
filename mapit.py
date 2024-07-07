import  webbrowser, sys#, pyperclip
#sys.argv # ['mapit.py', '12370', 'alameda trace circle'
address=""
#Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '12370', 'alameda trace circle'
   address = ' '.join(sys.argv[1:])
   #pyperclip.copy(address)
else:
    address = "12370 alameda trace circle" #pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)





import imapclient
import pyzmail


conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('mvty@gmail.com', 'jj12')
conn.select_folder('INBOX', 'True')
emails =conn.search(['SINCE 20-Aug-2023'])
# 'ON date', Before date, ALL, Subject "", Body "", TexT ""
#
emaildetail=conn.fetch(['emailNumber'], ['BODY[]','FLAGS'])

message = pyzmail.PyzMessage.factory(emaildetail['emailNumber'][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('bcc')
message.text_part
message.text_part.charset
conn.list_folders()
conn.select_folder('INBOX', readonly=False)
conn.delete_messages('UIDofemail')

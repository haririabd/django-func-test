from imap_tools import MailBox
from decouple import config

MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_USERNAME = config('MAIL_USERNAME')

with MailBox("imappro.zoho.com").login(MAIL_USERNAME, MAIL_PASSWORD, "Automation") as mb:
    #print(mb.folder.get())
    for msg in mb.fetch(limit=5, reverse=True, mark_seen=True):
        print(msg.subject, msg.date)
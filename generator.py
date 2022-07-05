import webbrowser
import os
import sys
from tkinter import *

def generate_html(surname, name, job, email):
    content = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Signature</title>
    </head>
    <body>
        <h3 style="color:blue;font-size: medium;">{surname} {name}</h3>
        <p style="color:cyan;">{job}</p>
        <a href="mailto:{email}">{email}</a>
    </body>
</html>
    '''
    html_content = content.format(**locals())
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    with open(path_to_signature, "w") as outfile:
        outfile.write(html_content)
    outfile.close()


def preview(surname, name, job, email):
    generate_html(surname, name, job, email)
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    path_to_signature = "file://" + path_to_signature
    webbrowser.open_new(path_to_signature)
    


def show_code(surname, name, job, email):
    generate_html(surname, name, job, email)
    window = Tk()
    window.title('TinoSign - Code')
    window.configure(background='white')
    window.geometry("600x400")
    window.resizable(0,0)

    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    with open(path_to_signature, "r") as outfile:
        data = outfile.read()

    outfile.close()
    result = Text(window,width=101,height=101)
    result.insert(0.0,data)
    result.config(state=DISABLED)
    result.pack()
    window.mainloop()

def google_help():
    webbrowser.open_new('https://support.google.com/mail/answer/8395?hl=fr&co=GENIE.Platform%3DDesktop')

def yahoo_help():
    webbrowser.open_new('https://fr.aide.yahoo.com/kb/SLN28060.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANoMO01EImZvj5dOwGvBBV_xIulXq0BmWZ1AwbafLFvpUf_9KjNt-TuKqFgUOBj7cC8l65A8_f13Z62dWeFiRqHMQ42KoRqJ4_sXAKsyb-HK_JeNBIqsKvg2F5qO7GxHJhA--wLhYXSa9ZZyJWfvMd6EFHXxHf1rqtbC_SIbYvwQ')

def outlook_help():
    webbrowser.open_new('https://support.microsoft.com/fr-fr/office/créer-une-signature-de-courrier-31fb24f9-e698-4789-b92a-f0e777f774ca')
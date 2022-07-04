from cgitb import html
import webbrowser
import os
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
    outfile = open('.ts_signature.html','w')
    outfile.write(html_content)
    outfile.close()


def preview(surname, name, job, email):
    generate_html(surname, name, job, email)
    webbrowser.open('.ts_signature.html')
    os.remove('.ts_signature.html')

def show_code(surname, name, job, email):
    generate_html(surname, name, job, email)
    window = Tk()
    window.title('TinoSign - Code')
    window.configure(background='white')
    window.geometry("600x400")
    f = open('.ts_signature.html','r')
    data = f.read()
    os.remove('.ts_signature.html')
    result = Text(window)
    result.insert(0.0,data)
    result.pack()
    window.mainloop()
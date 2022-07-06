import webbrowser
import os
import sys
from tkinter import Tk,Button,ttk,Text,Menu

def format_phone_number(num:str):
    num.replace(".","")
    num.replace("+33","0")
    output = num
    return output

def generate_html(surname:str, name:str, job:str, email:str, tel:str):
    name = name.upper()
    num = format_phone_number(tel)
    tel = format_phone_number(tel)
    num = '.'.join(a + b for a, b in zip(*[iter(num)]*2))
    slash =""
    if(len(num)!=0):
        slash="/"

    content = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Aperçu Signature</title>
</head>
<body>
<table style="padding: 0; margin: 0; border-collapse: collapse; min-width: 550px; font-size: 14px; font-family: Arial;">
    <tr>
        <td style="padding:10px;">
            <a href="https://apdiffusion.com"><img src="https://apdiffusion.com/wp-content/uploads/2019/03/logo.png"
                    alt="AP Diffusion" width="150" style="border:0px;"></a>
        </td>
        <td
            style="padding:10px 30px 10px 20px; vertical-align: middle; line-height: 1em; border-left: 1px solid lightgrey;">
            <p style="padding: 0; margin: 0; font-size: 18px; margin-bottom: 10px; line-height:1em;">
                <strong>{surname} {name}</strong></br>
                <span style="padding: 0; margin: 0; padding-top: 2px; font-size: 16px; ">
                    <i>{job}</i>
                </span>
            </p>
            <p style="padding: 0; margin: 0; color: #333333; text-decoration: underline;"><a
                    href="mailto:{email}"
                    style="color: #333333; border: 0; font-size: 14px;">{email}</a></p>
            <p style="padding: 0; margin: 0; color: #000; padding-top: 6px;">20 Bis Rue Strauss, </br>La Filature 70250
                RONCHAMP</p>
            <p style="padding: 0; margin: 0; padding-top: 6px;"><a
                    style="color: #000!important; text-decoration: none!important; border: 0;"
                    href="tel:0384207070">03.84.20.70.70</a> {slash} <a
                    style="color: #000!important; text-decoration: none!important; border: 0;"
                    href="tel:{tel}">{num}</a></p>
            <p style="padding: 0; margin: 0; color: #000; padding-top: 6px;"><a href="https://apdiffusion.com"
                    style="color:#333333 !important; text-decoration:underline!important;"><strong>https://apdiffusion.com/</strong></a>
            </p>
            <p style="padding: 0; margin: 0; color: #000; padding-top: 6px;"><a
                    href="https://www.facebook.com/apdiffusion1/"
                    style="color:#3B5998; text-decoration: underline;"><strong>Facebook</strong></a></p>
        </td>
        <td style="padding:10px; border-left: 1px solid lightgrey;">
            <a href="https://www.portail-cetal.fr/nos-portails/">
                <img src="https://www.portail-cetal.fr/wp-content/uploads/2021/11/Expert_CETAL_Professionnel_RVB.jpg"
                    alt="PROFESSIONNEL EXPERT CETAL" width="150" style="border:0px;">
            </a>
            </br>
            <a href="https://oknoplast.fr/fenetres/">
                <img src="https://www.rhone-alpes-stores.com/img/partners/oknoplast.png"
                    alt="Oknoplast Partenaire Premium" width="150" style="border:0px;padding-top:10px;">
            </a>
        </td>
    </tr>
</table>
</body>
</html>
    '''
    html_content = content.format(**locals())
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    with open(path_to_signature, "w") as outfile:
        outfile.write(html_content)
    outfile.close()


def preview(surname:str, name:str, job:str, email:str, tel:str):
    generate_html(surname, name, job, email, tel)
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    path_to_signature = "file://" + path_to_signature
    webbrowser.open_new(path_to_signature)
    


def show_code(surname:str, name:str, job:str, email:str, tel:str):
    generate_html(surname, name, job, email, tel)
    window = Tk()
    window.title('APsign - Code')
    window.geometry("600x400")
    window.resizable(0,0)

    # Création du menu    
    menubar = Menu(window)
    menuhelp = Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Aide',menu=menuhelp)
    menuhelp.add_command(label="Ajouter à Gmail", command=google_help)
    menuhelp.add_command(label="Ajouter à Outlook", command=outlook_help)
    menuhelp.add_command(label="Ajouter à Yahoo !", command=yahoo_help)
    window.config(menu=menubar)

    #Lecture et ajout du code
    data=""
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_signature = os.path.abspath(os.path.join(bundle_dir,'.ts_signature.html'))
    with open(path_to_signature, "r") as outfile:
        data = outfile.read()

    outfile.close()
    result = Text(window,width=101,height=101)
    result.insert(0.0,data)
    result.pack()
    window.mainloop()

def google_help():
    webbrowser.open_new('https://support.google.com/mail/answer/8395?hl=fr&co=GENIE.Platform%3DDesktop')

def yahoo_help():
    webbrowser.open_new('https://fr.aide.yahoo.com/kb/SLN28060.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANoMO01EImZvj5dOwGvBBV_xIulXq0BmWZ1AwbafLFvpUf_9KjNt-TuKqFgUOBj7cC8l65A8_f13Z62dWeFiRqHMQ42KoRqJ4_sXAKsyb-HK_JeNBIqsKvg2F5qO7GxHJhA--wLhYXSa9ZZyJWfvMd6EFHXxHf1rqtbC_SIbYvwQ')

def outlook_help():
    webbrowser.open_new('https://support.microsoft.com/fr-fr/office/créer-une-signature-de-courrier-31fb24f9-e698-4789-b92a-f0e777f774ca')
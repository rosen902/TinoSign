from tkinter import Tk, Label, Entry, ttk
from turtle import bgcolor
from tkmacosx import Button
from generator import *


# Création de la fenetre et du fichier de base
window = Tk()
window.title('TinoSign')
window.geometry("600x300")
window.resizable(0,0)
generate_html("unknown","unknown","unknown","unknown")

#Instance de styles
style = ttk.Style(window)
style.theme_use('aqua')

# Création du menu
menubar = Menu(window)
menuhelp = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Aide',menu=menuhelp)
menuhelp.add_command(label="Ajouter à Gmail", command=google_help)
menuhelp.add_command(label="Ajouter à Outlook", command=outlook_help)
menuhelp.add_command(label="Ajouter à Yahoo !", command=yahoo_help)


window.config(menu=menubar)


# Création et insertion du formulaire
main_frame = Frame(window)
main_frame.grid_columnconfigure((0,1),weight=1)

# Création des labels
surname_label = ttk.Label(main_frame, text="Prénom : ")
name_label = ttk.Label(main_frame, text="Nom : ")
job_label = ttk.Label(main_frame, text="Poste : ")
email_label = ttk.Label(main_frame, text="Email : ")

# Création des entrées associées
surname_entry = ttk.Entry(main_frame,width=50,background='white')
name_entry = ttk.Entry(main_frame,width=50,background='white')
job_entry = ttk.Entry(main_frame,width=50,background='white')
email_entry = ttk.Entry(main_frame,width=50,background='white')

# Organisation du formulaire
surname_label.grid(row=3,column=0,pady=10)
surname_entry.grid(row=3,column=1,pady=10)

name_label.grid(row=4,column=0,pady=10)
name_entry.grid(row=4,column=1,pady=10,padx=10)

job_label.grid(row=5,column=0,pady=10)
job_entry.grid(row=5,column=1,pady=10,padx=10)

email_label.grid(row=6,column=0,pady=10)
email_entry.grid(row=6,column=1,pady=10,padx=10)

main_frame.pack()

secondary_frame = Frame(window,width=100,pady=10)

# Création du bouton d'apeçu
preview_button = ttk.Button(secondary_frame, text='Aperçu dans le navigateur', padding=10 , command=lambda: preview(surname_entry.get(),name_entry.get(),job_entry.get(),email_entry.get()))
preview_button.pack(side=LEFT,padx=10)

# Création du bouton de génération du code
result_button = ttk.Button(secondary_frame,text="Générer signature", padding=10,command=lambda: show_code(surname_entry.get(),name_entry.get(),job_entry.get(),email_entry.get()))
result_button.pack(side=RIGHT,padx=10)
secondary_frame.pack()

window.mainloop()



from tkinter import *
from generator import *

# Création de la fenetre
window = Tk()
window.title('TinoSign')
window.configure(background='white')
window.geometry("500x300")
window.resizable(0,0)

# Création et insertion du formulaire
main_frame = Frame(window,background='white')
main_frame.grid_columnconfigure((0,1),weight=1)

# Création des labels
surname_label = Label(main_frame, text="Prénom : ",background="white")
name_label = Label(main_frame, text="Nom : ",background="white")
job_label = Label(main_frame, text="Poste : ",background="white")
email_label = Label(main_frame, text="Email : ",background="white")

# Création des entrées associées
surname_entry = Entry(main_frame,width=50)
name_entry = Entry(main_frame,width=50)
job_entry = Entry(main_frame,width=50)
email_entry = Entry(main_frame,width=50)

# Organisation du formulaire
surname_label.grid(row=3,column=0,pady=4)
surname_entry.grid(row=3,column=1,pady=4)

name_label.grid(row=4,column=0,pady=4)
name_entry.grid(row=4,column=1,pady=4,padx=4)

job_label.grid(row=5,column=0,pady=4)
job_entry.grid(row=5,column=1,pady=4,padx=4)

email_label.grid(row=6,column=0,pady=4)
email_entry.grid(row=6,column=1,pady=4,padx=4)

main_frame.pack()

secondary_frame = Frame(window,background='white',width=100,pady=10)

# Création du bouton d'apeçu
preview_button = Button(secondary_frame,text="Aperçu dans le navigateur",command=lambda: preview(surname_entry.get(),name_entry.get(),job_entry.get(),email_entry.get()),background='#4575b9',activebackground='cyan',foreground='white')
preview_button.pack(side=LEFT)

# Création du bouton de génération du code
result_button = Button(secondary_frame,text="Générer signature",command=lambda: show_code(surname_entry.get(),name_entry.get(),job_entry.get(),email_entry.get()),background='#4575b9',activebackground='cyan',foreground='white')
result_button.pack(side=RIGHT)
secondary_frame.pack()

window.mainloop()



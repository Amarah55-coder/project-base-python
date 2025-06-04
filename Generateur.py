import customtkinter as ctk
import string
import random
import pyperclip


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Générateur de mot de passe")
app.geometry("600x320")
app.resizable(False, False)

def generer_mot_de_passe():
    longueur = slider_longueur.get()
    charset = ""
    if check_az.get():
        charset += string.ascii_letters
    if check_09.get():
        charset += string.digits
    if check_speciaux.get():
        charset += string.punctuation

    if not charset:
        password_var.set("Aucun type sélectionné")
        return

    password = ''.join(random.choice(charset) for _ in range(int(longueur)))
    password_var.set(password)
    label_force.configure(text="✅ Strong Password", text_color="green")
    bouton_copier.configure(text="📋 Copier")

def copier_mot_de_passe():
    mot = password_var.get()
    if mot and "Aucun" not in mot:
        pyperclip.copy(mot)
        bouton_copier.configure(text="✔️ Copié !")

def basculer_visibilite():
    global visible
    visible = not visible
    if visible:
        entry_mot_de_passe.configure(show="")
        bouton_visibilite.configure(text="🙈")
    else:
        entry_mot_de_passe.configure(show="•")
        bouton_visibilite.configure(text="👁️")

def maj_longueur(val):
    label_longueur.configure(text=f"Character Length: {int(float(val))}")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)


password_var = ctk.StringVar()
entry_mot_de_passe = ctk.CTkEntry(frame, textvariable=password_var, font=("Courier", 18),
                                  width=400, show="•")
entry_mot_de_passe.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")


visible = False
bouton_visibilite = ctk.CTkButton(frame, text="👁️", width=30, command=basculer_visibilite)
bouton_visibilite.grid(row=0, column=3, padx=5)


bouton_generer = ctk.CTkButton(frame, text="🎲", width=30, command=generer_mot_de_passe)
bouton_generer.grid(row=0, column=4, padx=5)

label_force = ctk.CTkLabel(frame, text=" ", text_color="green")
label_force.grid(row=1, column=0, columnspan=2, pady=5, sticky="w", padx=10)


slider_longueur = ctk.CTkSlider(frame, from_=4, to=32, number_of_steps=28, command=maj_longueur)
slider_longueur.set(16)
slider_longueur.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

label_longueur = ctk.CTkLabel(frame, text="Character Length: 16")
label_longueur.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

check_az = ctk.CTkCheckBox(frame, text="A-Z", checkbox_height=20, checkbox_width=20)
check_az.select()
check_az.grid(row=4, column=0, padx=10, pady=5, sticky="w")

check_09 = ctk.CTkCheckBox(frame, text="0-9", checkbox_height=20, checkbox_width=20)
check_09.select()
check_09.grid(row=4, column=1, padx=10, pady=5, sticky="w")

check_speciaux = ctk.CTkCheckBox(frame, text="!@#", checkbox_height=20, checkbox_width=20)
check_speciaux.select()
check_speciaux.grid(row=4, column=2, padx=10, pady=5, sticky="w")

bouton_copier = ctk.CTkButton(frame, text="📋 Copier", command=copier_mot_de_passe)
bouton_copier.grid(row=5, column=0, columnspan=5, pady=10)

app.mainloop()

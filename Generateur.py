import random
import string

try:
    longueur_mot_de_passe = int(input("Entrer la longueur de votre mot de passe: "))
except ValueError:
    print("Veuillez entrer un nombre entier.")
    exit()

if longueur_mot_de_passe < 8:
    mot_de_passe = "Mot de passe trop court"
else:
    format_mot_de_passe = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    mot_de_passe += [random.choice(format_mot_de_passe) for _ in range(longueur_mot_de_passe - 4)]
    random.shuffle(mot_de_passe)
    mot_de_passe = ''.join(mot_de_passe)

print(f"Mot de passe généré: {mot_de_passe}")

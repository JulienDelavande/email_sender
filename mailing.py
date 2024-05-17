import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
from dotenv import load_dotenv
import os
from agence_immo.mail_template_discussion import mail_template_discussion
import pandas as pd

# Load environment variables from a specific .env file location
load_dotenv(dotenv_path='.env')  # Adjust the path if necessary

email_supaero = os.getenv("EMAIL_SUPAERO")
mot_de_passe = os.getenv("MDP_SUPAERO")
serveur_smtp = os.getenv("SERVEUR_SMTP")
port_smtp = os.getenv("PORT_SMTP")
id_supaero = os.getenv("ID_SUPAERO")
email_copy_1 = os.getenv("EMAIL_COPY_1")
email_copy_2 = os.getenv("EMAIL_COPY_2")
nom = os.getenv("NOM")
prenom = os.getenv("PRENOM")
linkedin = os.getenv("LINKEDIN")
tel = os.getenv("TEL")


def envoyer_email(destinataire, sujet, corps):

    # Verify environment variables are loaded
    if not email_supaero or not mot_de_passe or not serveur_smtp or not port_smtp:
        print("Erreur: Les variables d'environnement ne sont pas correctement définies.")
        return

    # Création du message
    message = MIMEMultipart()
    message['From'] = email_supaero
    message['To'] = destinataire
    message['Cc'] = email_copy_1 + ", " + email_copy_2
    message['Subject'] = sujet
    message.attach(MIMEText(corps, 'plain'))

    # Connexion au serveur SMTP et envoi de l'email
    try:
        # Contexte SSL pour sécuriser la connexion
        contexte = ssl.create_default_context()
        with smtplib.SMTP_SSL(serveur_smtp, port_smtp, context=contexte) as serveur:
            #serveur.set_debuglevel(1)  # Active le débogage
            serveur.login(id_supaero, mot_de_passe)
            serveur.send_message(message)
        print(f"Email envoyé à {destinataire}")
    except smtplib.SMTPException as e:
        print(f"Erreur SMTP lors de l'envoi de l'email à {destinataire}: {e}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email à {destinataire}: {e}")

# Liste des destinataires
csv_file = "./agence_immo/contacts.csv"
df = pd.read_csv(csv_file, sep=",")
print(df.columns)
destinataires = df["email"].tolist()

# Sujet et corps de l'email
path = "./agence_immo/mail_template_discussion.py"
sujet, corps = mail_template_discussion(nom, prenom, tel, linkedin)

# Envoi des emails
for destinataire in destinataires:
    envoyer_email(destinataire, sujet, corps)

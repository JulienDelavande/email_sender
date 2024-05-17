import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
#dotenv
from dotenv import load_dotenv
import os

load_dotenv()
email_supaero = os.getenv("EMAIL_SUPAERO")
mot_de_passe = os.getenv("MDP_SUPAERO")
serveur_smtp = os.getenv("SERVEUR_SMTP")
port_smtp = os.getenv("PORT_SMTP")

def envoyer_email(destinataire, sujet, corps):

    # Création du message
    message = MIMEMultipart()
    message['From'] = email_supaero
    message['To'] = destinataire
    message['Subject'] = sujet
    message.attach(MIMEText(corps, 'plain'))

    # Connexion au serveur SMTP et envoi de l'email
    try:
        # Contexte SSL pour sécuriser la connexion
        contexte = ssl.create_default_context()
        with smtplib.SMTP_SSL(serveur_smtp, port_smtp, context=contexte) as serveur:
            serveur.set_debuglevel(1)  # Active le débogage
            serveur.login(email_supaero, mot_de_passe)
            serveur.send_message(message)
        print(f"Email envoyé à {destinataire}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email à {destinataire}: {e}")

# Liste des destinataires
destinataires = ["destinataire1@example.com", "destinataire2@example.com"]

# Sujet et corps de l'email
sujet = "Sujet de votre email"
corps = "Corps de votre email."

# Envoi des emails
for destinataire in destinataires:
    envoyer_email(destinataire, sujet, corps)

def mail_template_discussion(sender_name, sender_first_name, sender_tel, sender_linkedin):

    object = "Invitation pour une discussion au sujet de l’IA pour l’immobilier."
    subject =  f"""
    Bonjour Madame, Monsieur,

    
    J'espère que vous allez bien.

    
    Nous sommes un groupe d’étudiants spécialisés en IA qui cherche à mieux comprendre le secteur immobilier.

    
    Nous avons pour projet de développer une intelligence artificielle capable de pré-traiter les dossiers des candidats qui se positionnent sur les annonces immobilières.

    
    Nous aimerions beaucoup échanger avec vous au sujet de votre métier et de vos problématiques afin de mieux comprendre comment l’IA pourrait vous faciliter certaines tâches.

    
    Accepteriez-vous un court échange dans les prochains jours ?

    
    Je vous remercie par avance,

    
    Sincèrement,

    
    {sender_name} {sender_first_name}

    
    Mon profil : {sender_linkedin}

    {sender_tel}
    """
    
    return object, subject
    
    
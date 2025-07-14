# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image debut = "debut.png"

# Déclarez les personnages utilisés dans le jeu.
# define e = Character('Eileen', color="#c8ffc8")
# define nvl = Character(kind=nvl)

# Le jeu commence ici
label start:
    scene debut
    $ mort = 0
    $ nom = ""
    $ cle=False
    $ item = ""
    $ chap=0
    "Bienvenue dans Aventure Stupide, un jeu a l'humour décalé."
    "Le texte a été écrit par un humain mais les images ont été réalisés par IA faute de compétences en dessin."
    "Des musiques et des sons seront peut-être créés au clavier MIDI et  ajoutées plus tard mais pour l'instant il n'y en a pas. quand aux futurs chapitres on verra"
    "Si vous ne l'avez pas déja fait regarder les sections 'Aide' et 'A propos' pour plus d'informations sur le jeu et sa conception."
    "Dans ce jeu vous incarnez un type très... Intelligent.. Son but (actuellement) est de survivre (ou pas) dans son appartement."
    jump intro
    return

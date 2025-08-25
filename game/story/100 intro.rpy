# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image intro = At("BG/intro.jpeg", UtoDlow)
image Ville = At("BG/Ville.jpeg", UtoDlow)
image Cuisine = At("BG/Cuisine.jpeg", UtoDlow)
image meteorite  = At("OBJ/Meteorite.png", chute)
image image_faucheuse = At("PNJ/Mort.png")

# Déclarez les personnages utilisés dans le jeu.
# define e = Character("Eileen")
define p = Character("{nom}", color="#fbff00")
define dd = Character(_("Faucheuse"), color="#ea00ff", image="image_faucheuse")


# Le jeu commence ici
label intro:
    $ item=""
    scene intro
    if cle==True:
        play sound "FX/Boum.ogg"
        "BANG! Vous vous réveillez en sursaut dans votre lit. Quelqu'un vous a lancé vos clé d'appartement en pleine figure... Mais vous ne voyez personne! A moitier sonné, vous regardez autours de vous..."
    if mort == 0:
        pause 10
        "Le soleil se lève et une merveilleuse journée commance. Les oiseaux chantent que rien de mal ne va arriver."
    else:
        "Le soleil se lève et une merveilleuse journée recommance. Les oiseaux chantent que rien de mal ne va arriver cette fois-ci."
    menu:
        "C'est un bon jour pour sortir de son appartement mais que faire."
        "Prendre un petit dejeuner":
            scene Cuisine
            "Vous allez en direction de la cuisine a la vitesse d'une limace au galop."
            menu:
                    "Vous n'avez rien dans votre frigo"
                    "Aller au café du quartier faute de mieux":
                        jump ville
                    "Aller a la fenêtre avec de quoi zigouiller du zozio":
                        jump chasseurfenetre
        "Retourner au lit":
            play music "Music/Dodo.ogg"
            "Vous vous retournez dans votre lit et vous vous endormez."
            "Mais... Qu'est-ce que c'est ?"
            show meteorite
            pause 1
            play sound "FX/Chute.ogg"
            "Une météorite??? Elle tombe du ciel et vous écrase. COUIC!"
            $ item="meteorite"
            jump zetemort
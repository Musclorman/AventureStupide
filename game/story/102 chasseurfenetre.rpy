image win = At("BG/win.jpeg", updownmiddlezoom)
image voisine  = At("PNJ/Voisine.webp", top)
image zozio  = At("PNJ/Zozio.webp", top)


label chasseurfenetre:
    $ renpy.fix_rollback()
    $ item="fusil"
    scene win
    "Encore a moitier endormis vous préparer des baballes et un gros fusil! Vous marchez tel un zombi en direction de la fenêtre"
    "et vous remarquez une voisine en dessous que vous détestez depuis une sombre histoire de chat qui a fini en ragoût lors d'un de ses rituels démoniaque..."
    menu:
        "qu'allez-vous bien tuer pour commencer la journée"
        "Transformer la voisine en passoire":# renpy-graphviz: IGNORE
            $ renpy.fix_rollback()
            show voisine
            "Vous prenez un air déterminé, vous ouvez la fenêtre et vous descendez la voisine avec votre fusil... A l'envers. Vous avez pris une balle entre les 2 yeux."
            "Fallait regarder dans quel sens vous teniez votre fusil mais vous n'ête pas le premier a mourir stupidement. N'est-ce pas?"
            jump zetemort
    
        "Tirer sur un gros pigeon plein de bonne viande fraiche":# renpy-graphviz: IGNORE
            $ renpy.fix_rollback()
            show zozio
            "Vous visez un pigeon et vous tirez... Vous avez touché la vitre de la fenêtre que vous n'avez pas ouverte le tout sour le regard intrigué du volatile."
            "Les bris de verre vous ont transformé en viande saignante mais pas fraiche."
            jump zetemort
    

    return

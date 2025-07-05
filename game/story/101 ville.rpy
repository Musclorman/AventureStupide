label ville:
    if chap==0:
        "Vous sortez dans la rue pour prendre un verre... De café."
        if cle==False:
            "mais vous ne savez plus ou est la clé de votre appartement alors pour sortir vous défoncez la porte comme un gros bourrin."
            $ item="brute"
            "Vous y allez tellement fort que vous défoncez la porte et vous vous cassez la jambe et le bras. Pour couronner le tout, les reste de la porte vous tombe dessus et vous éclate la cervelle."
            jump zetemort
        if cle==True:
            scene ville
            "Vous voila dans la rue"
            $ mort = 0
            $ cle=False
            $ item = ""
            $ chap=1
        if chap==1:
            jump ville1
label ville1:
    if mort==0:
        "Vous vous retrouvez dans la rue, devant votre appartement et votre bar préféré est a 5 minutes a pied."
    if mort==1:
        scene ville
        "Vous vous réveillez dabs le caniveau comme a la fin d'une soirée trop arrosé. Vous ne savez pas comment vous êtes arrivé la mais vous avez soif!"
        "Vous vous relevez et vous vous rappellez que vous etiez en chemin pour boir un coup au bar."
    if mort>=2:
        scene ville
        "Vous vous réveillez encore une fois dans le caniveau. A ce rythme la, vous allez finir par y vivre. Dire que le bar est juste a 5 minutes a pied..."
    menu:
        "Vous pouvez y aller en passant par le parc ou en prenant la ruelle glauque et sombre qui est derrière votre immeuble."
        "Aller au parc":
            "Vous décidez de prendre le chemin du parc, c'est plus agréable et moins glauque."
            jump parc
        "aller dans la ruelle":
            "Vous décidez de prendre la ruelle, c'est plus rapide mais c'est glauque et sombre et vous n'aimez pas trop ça."
            jump ruelle

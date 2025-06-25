label ville:
    $ renpy.fix_rollback()
    scene ville
    "Vous sortez dans la rue pour prendre un verre... De café."
    if cle==False:
        "mais vous ne savez plus ou est la clé de votre appartement alors pour sortir vous défoncez la porte comme un gros bourrin."
        $ item="brute"
        "Vous y allez tellement fort que vous défoncez la porte et vous vous cassez la jambe et le bras. Pour couronner le tout, les reste de la porte vous tombe dessus et vous éclate la cervelle."
        jump zetemort

    if cle==True:
        "Bravo! Vous avez suvécu... Pour l'instant. Peut-être qu'il y aura une suite..."

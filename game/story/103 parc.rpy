label parc:
    image parc = At("BG/Parc.jpeg")
    scene parc
    "Vous vous baladez gaiement au milieux des arbres, des fleurs et des papillons multicolores. Il fait beau et tout est calme et tranquille..."
    image dog  = At("PNJ/EvilDog.webp", sczoom)
    show dog
    """Jusqu'a ce que qu'un gros bouledog sans laisse surgisse de derrière un des nombreux panneaux "INTERDIS AUX CHIENS" plantés tout les 10 mètres et qu'il se mette a courir vers vous d'un air menacant."""
    menu:
        "Comment allez-vous bien faire pour ne pas devenir son petit dej?..."
        "L'affronter a main nue tel un gladiateur des temps modernes":
            "Vous essayez de prendre la pose comme une des statut de dieux grec qu'on voit dans les musés"
            "Vous lui enfoncez votre poing dans les dents mais elles sont tellement pointus et solides que vous vous empalez la main."
            "Vous vous retrouvez a genous en pleine agonis jusqu'a ce que vous soyez assez dévorré pour retrouver votre copain squelette."
            jump zetemort
        "Vous cacher derrière un toboggan en éspèrant qu'il trouve un autre repas":
            "Vous fuyez courageusement en direction du toboggan."
            if cle==False:
                hide dog
                "Alors que vous attentez, vous entandez un hurlement et voyez un ballon de foot rouler dans votre direction"
                $ cle = True
                show dog
                "Vous prenez le ballon et voyant le chien dévorrer un petit garçon vouv vous décider a courir ver la sortie"
                "Mais le chien en vous voyant décide que le petit n'a pas assez de viande et se jette sur vous. Bon appetit!"
                jump zetemort
            else:
                "mais le chien affamé vous tire par la jambe direction le bac a sable avant de vous dévorer."
                jump zetemort
        "Escalader un arbre comme SuperTarzan" if cle==False:
            hide dog
            "Vous grimpez a un arbre et vous vous hissez sur une grosse branche solide... Mais visiblement vous être trop lourd et la branche cède"
            show dog
            "Vous tombez tout droit en direction des grandes dents du molosse et naturellement il passe a table... Miam!"
            jump zetemort
        "Faire bouclier avec le ballon" if cle==True:
            "Vous vous servez du ballon comme d'un bouclier mais un gros coup de tête du chien vous mêt par terre... Il vous dévore sans faire attention a la baballe"
            jump zetemort
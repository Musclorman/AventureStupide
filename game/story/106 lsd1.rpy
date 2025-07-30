label lsd1:
    image forest = At("BG/Forest.jpeg", UtoDxlow)
    image Houseforestout=At("BG/House_forest_out.jpeg", UtoDlow)
    scene Houseforestout
    "Et vous réalisez que la sortie donne sur une prairie verdoyante."
    "En marchant un peu vous voyez une licorne multicolore brouter de l'herbe près du chemin."
    "Vous vous approchez mais elle lève la tête et commence a vous charger avec sa corne pointue en avant. Vous fuyez en courant en Direction une forêt bordant un lac."
    $ mort = 0
    $ cle=False
    $ chap = 2
    scene forest
    "Vous vous retrouvez dans une forêt bordant un lac."
    "Vous entendez des bruits étranges venant de la forêt. Vous décidez de vous enfoncer un peu plus dans les bois."
    menu:
        "Vous continuez à avancer dans la forêt..."
        "Direction le lac":
            "Vous vous dirigez vers le lac en suivant le bruit de l'eau avec l'intention de prendre un bain."
            image lake = At("BG/Lake.jpeg", UtoDxlow)
            scene lake
            "Vous arrivez au bord du lac et vous décidez de vous baigner."
            "L'eau est fraîche et agréable. Vous nagez un peu avant de sortir de l'eau."
            "En sortant, vous remarquez une bouteille de [item] brillante au fond du lac. Vous plongez pour la récupérer..."
            "Mais il semble que vous ne nagez pas tout seul"
            image crocodile = At("BG/Crocodile.jpeg", DtoUxlow)
            scene crocodile
            "Un crocodile géant surgit de l'eau et vous attaque!"
            "Vous essayez de nager pour échapper à la bête mais elle est trop rapide."
            "Vous sentez ses dents se refermer sur vous et tout devient noir..."
            jump bar2
        "Direction la les profondeurs de la forêt":
            "Vous décidez de vous enfoncer plus profondément dans la forêt, attiré par les bruits étranges."
            "Vous continuez à avancer dans la forêt, le bruit des branches craquant sous vos pieds résonnant dans le silence ambiant."
        "Direction une clairière":
            "Vous décidez de vous diriger vers une clairière que vous apercevez au loin."
        "Direction une grotte":
            "Vous décidez de vous diriger vers une grotte que vous apercevez au loin."

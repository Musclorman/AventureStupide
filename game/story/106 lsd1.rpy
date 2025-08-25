label lsd1:
    image forest = At("BG/Forest.jpeg", UtoDxlow)
    image Houseforestout=At("BG/House_forest_out.jpeg", UtoDlow)
    scene Houseforestout
    "Et vous réalisez que la sortie donne sur une prairie verdoyante."
    "En marchant un peu vous voyez une licorne multicolore brouter de l'herbe près du chemin."
    image Metalicorne = At("PNJ/Metalicorne.webp", DtoU)
    show Metalicorne
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
            image princessedesbois = At("BG/Princesse 2.jpeg", DtoUxlow)
            scene princessedesbois
            "Une belle demoiselle assise sur un trone semble vous attendre."
            "Ca doit être une princesse ou une fée"
            menu:
                "Mais que faire"
                "Lui parler":
                    "[nom]" "Bonjour madame... Je cherche mon chemin... Savez-vous ou je suis?"
                    "Princesse" "Bonjour monsieur. Je connais très bien cet endroit. Ici nous sommes..."
                    "Princesse" "DEBOUT!"
                    jump bar2
                "Lui envoyer votre poing entre les deux yeux":
                    "Vous lui collez une grande baffe dont elle se rappellera toute sa vie..."
                    play sound "FX/Boum.ogg"
                    "... Mais elle vous projette sur le sol avant de vous coller une série de grandes gifles!"
                    jump bar2
        "Direction une grotte":
            "Vous décidez de vous diriger vers une grotte que vous apercevez au loin."
            image cavemort  = At("bg/CaveMort.jpeg")
            scene cavemort
            "Ce lieux vous rappelle un endroit famillier... mais vous glissez et tombez le nez sur la pierre a moins de 10 mêtres de l'entrée"
            jump bar2

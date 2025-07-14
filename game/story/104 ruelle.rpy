label ruelle:
    image RuelleSombre = At("BG/RuelleSombre.jpeg")
    image Typelouche = At("PNJ/TypeLouche.png", DtoUlow)
    scene RuelleSombre
    "D'ailleurs vous sentez une présence derrière vous..."
    show Typelouche
    "Vous vour retournez et voyez un type louche armé d'une batte de baseball avancer discrètement vers vous..."
    menu:
        "Vous n'y connaissez rien au baseball mais vous avez une petite idée de ce qui vous attend si vous ne faites rien"
        "Courir":
            if cle==False:
                "Vous courrez a tout allure sans regardez ou vous allez."
                image extbarscene = At("BG/Barext.jpg", UtoD)
                scene extbarscene
                "Vous traversez la rue face a votre bar préféré sans vérifier au préalable qu'il n'y ai pas de voiture."
                "Et effectivement y avait pas de voiture... Mais un gros camion qui fraine... Trop tard."
                "Vous ête applatis comme une crêpe alors que vous avez presque atteint votre but. Dommage!"
                jump zetemort
            if cle==True:
                "Vous courrez a toute vitesse en laissant échapper le ballon. Le type louche glisse dessus mais vous assomme avant de tomber."
                "Il se relève, réduit votre tête en purée, mêt le ballon a la place et s'en va tout content de son oeuvre d'art"
                jump zetemort
        "Lui déclarer votre amour et le demander en mariage" if cle==False:
            "Vous commencer a lui chanter un poême a l'eau de rose quand vous ête interrompus par la batte en plein visage"
            "Le type louche vous fracasse le crâne, vide vos poches et s'en vas tranquillement."
            jump zetemort
        "Jouer avec le ballon que vous avez pris avant de vous faire déchiqueter" if cle==True:
            "Vous donnez un giga coup de pied dans le ballon... Et fracassez ma vitre d'un appartement. Vous courrez en esperant au moins que ca fasse diversion."
            "Moins de 10 secondes après le bris de verre une vieille dame en robe de chambre sort sa tête de la vitre brisé... Puis lance un vieil obus par la fenêtre."
            "La secousse provoqué vous envois sur le sol mais vous n'avez rien. Vous vous relevez et vous voyez le type louche encore vivent..."
            "mais par terre et avec sa batte et ses jambes en lanbeaux. Vous partez alors en direction du bar sans vous retourner."
            jump extbar

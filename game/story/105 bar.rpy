label extbar:
    image extbarscene = At("BG/Barext.jpg", DtoUxlow)
    scene extbarscene
    image voisine = At("PNJ/Voisine.webp", top)
    define voisine = Character("Voisine gothique", color="#ff3700")
    "Vous arrivez devant votre bar préféré mais vous voyez votre voisine gothique tentant d'attrapper un énième chat pour ses expèriences paranormales."
    "Vous vous rappelez qu'elle vous a déjà parlé de ses expériences et qu'elle vous a même montré votre chat dans un bocal rempli de liquide vert fluo bien rangé au font d'un frigo..."
    "Autant dire que vous auriez préféré ne pas la croiser."
    menu:
        "Comment éviter qu'elle vous remarque..."
        "Vous la contournez discrètement en vous faufilant":
            "Vous essayez de la contourner discrètement en vous faufilant derrère des voitures garés sur le trottoir mais elle vous remarque quand même..."
        "Vous faites comme si vous ne l'aviez pas vue et avancez tout droit vers le bar.":
            "Vous faites comme si vous ne l'aviez pas vue mais elle vous voit..."
    "... Et elle vous interpelle."
    show voisine
    voisine "Alors [nom] on fait encore la tournée des bars ?"
    menu:
        "Vous lui répondez..."
        "Non j'achète un magasine":
            voisine "Tu sait lire maintenant ?"
        "Juste un café":
            voisine "Bien sur... Et ton café tu va le couper avec des shots de vodka... Ou peut-être de rhum."
        "J'ai eut une dure journée et j'ai besoin de me détendre":
            voisine "On est que le matin... Si ca se trouve t'a pas dormis de la nuit et tu as déjà bu avant de sortir de chez toi."
    voisine "Tu a une drôle de tête aujourd'hui. Tu as l'air d'avoir croisé la mort dans une autre dimention mais c'est peut-être juste un simple mur en béton armé."
    menu:
        "Vous lui répondez..."
        "C'est juste que j'ai pas dormis de la nuit":
            voisine "Tu devrais aller te coucher au lieu de sortir dans la rue comme un zombie."
        "Comment t'a deviné ?":
            voisine "Vu ta tête c'est facile a deviner. Combien de fois je t'ai vu t'applatir contre un mur en cherchant une clé ou je ne sait quoi ?"
        "J'AI SOIF!":
            voisine "Comme d'habitude..."
    voisine "Bon, je te laisse. Je dois aller chercher du materiel pour mon prochain rituel. Au revoir [nom]!"
    hide voisine
    "Vous la regardez partir en vous disant que vous avez de la chance de ne pas être un chat. Pauvres bêtes!"
    "Dire qu'elle croit que les chats sont des créatures maléfiques et qu'elle doit les sacrifier pour invoquer des bestioles encore plus maléfiques"
    menu:
        "Est-ce qu'il est nécessaire de dire qu'elle aime tout ce qui est très maléfiques?"
        "Oui":
            "Vraiment? Depuis le temps que vous jouez a ce jeu... Vous lisez toujours les dialogues n'est-ce pas?"
        "Non":
            "Vous avez raison, c'est inutile de le préciser. C'est répétitif a force."
    "Plus que quelques mètres et vous serez enfin au bar. mais peut-être que vous voudriez savoir ce qui vous attend la-bas? Ba... Vous saurez bien assez tôt..."
    "Vous entrez dans le bar et vous vous asseyez au comptoir."
    "A suivre car en cours d'écriture"

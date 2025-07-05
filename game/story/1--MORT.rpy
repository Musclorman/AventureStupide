image cavemort  = At("bg/CaveMort.jpeg")
label zetemort0:
    scene cavemort
    $ mort += 1
    if mort == 1 :
        "Vous vous trouvez dans un genre d'endroit sombre et froid. Vvous voyez un genre de squelette sinistre s'avancer vers vous."
        dd "Salut. Je ne t'ai jamais vu ici. Tu viens de mourir ? Tu sait ou t'es au moins?"
    if mort == 2 :
        "Vous vous retrouvez face au squelette qui vous regarde d'un air amusé."
        dd "déjà de retour [nom]? Je t'avais manqué? Tu n'as pas l'air d'avoir appris de tes erreurs. Tu sais que tu es mort, n'est-ce pas?"
    if mort == 3 :
        "Vous vous retrouvez face au squelette qui vous regarde d'un air un peut lassé."
        dd "Encore [nom]... Tu n'as toujours pas l'air d'avoir appris de tes erreurs."
    if mort == 4 :
        "Vous vous retrouvez encore face au squelette."
        dd "Bon... T'es vraiment un abruti fini alors j'ai un petit cadeau pour toi. Tu veut ta clé perdue de ton appart? Tu l'aura a ton reveil."
        $ cle=True
    if mort >= 5 :
        "Vous vous retrouvez face au squelette qui vous regarde d'un air exaspéré."
        dd "Je n'ai jamais vu un client aussi idiot. T'a la clé? Alors tu va pouvoir sortir de ton appart."
        $ cle=True
    if item=="meteorite":
        dd "T'était un chancreux toi. Tu t'es fait écraser par une météorite alors qu'il aurait été plus simple de jouer au loto ou devenir miliardaire!"
    if item=="fusil":
        dd "Alors Cowboy? On fait joujou avec un gros flinflingue sans savoir s'en servir? Tu sais que tu aurais pu te faire tuer avec ça..."
        dd "Ah bah oui, c'est ce qui t'es arrivé! Suis-je bête!"
    if item=="brute":
        dd "Ah... Un bourrin qui défonce des portes! Tu sais que tu aurais pu juste utiliser la clé de ta porte? Non? Bah tu viens de mourir comme un abruti alors que tu aurais pu survivre!"
    if mort == 1 :
        dd "J'aime bien ton air abrutis et ton regard vide. Un homme tel que toi doit bien avoir un petit nom stylé qui va avec cette allure de zombie!"
        dd "Tu sait encore comment tu t'appelles au moins? Essaie un truc que t'a visiblement jamais fait de ton vivent..."
        dd "Fait marcher un petit neurone ou deux! Ca n'a jamais tué personne et encore moins un type déja mort!"
        label sansnom:
            $ renpy.fix_rollback()
            $ nom=renpy.input("Ecris ton nom ici(si tu y arrive):")
            $ nom=nom.strip()
            if nom == "":
                dd "Ah bah bravo, tu n'es même pas capable de mettre un nom sur ton cadavre. lance-toi. Tu n'a plus rien à perdre de toute façon"
                jump sansnom
            if len(nom) < 3:
                dd "Tu sais, un nom c'est pas juste un mot d'une ou deux lettres. C'est une identité! Alors sort-moi un truc un peu plus long et plus classe que ça!"
                jump sansnom
            if len(nom) > 10:
                dd "Bien looong comme nom. Tu est un noble moyen-âgeux? Tu peu laisser tomber les titres et les noms à rallonge, ici le roi c'est MOOOAAAA HA... HA... Atchoum!"
                jump sansnom
            else:
                dd "Ba voila! Tu a réussis mon cher [nom]. C'est pas si compliqué de se souvenir de son nom, même quand on est mort!"
                dd "Bon, comme t'a l'air marrant je vais te faire remonter le temps afin que tu puisse revivre et éviter de mourir comme un idiot."
    if mort > 0 :
        dd "Par le pouvoir du crâne ancestral qui est le mien, je te réssuscite et te renvoie dans le passé! A plus dans l'bus [nom]!"
    if mort >= 5:
        dd "Ah et vu que t'avait pas trouvé ta clé je vais te la relancer en pleine tronche en y allant fort cette fois! Tu devrait pas la louper!"
        $ cle=True
    jump intro
 At("bg/CaveMort.jpeg")
label zetemort1:
    scene cavemort
    $ mort += 1
    if mort == 1 :
        dd "Serieux [nom] je t'aide, je te donne ta clé et tu meurs 2 minutes après? T'a pas une malédiction ou un truc du genre? Appelle un exorciste!"
        dd "Bon ba... Je te renvois dans ta rue pour que tu puisse mourir de nouveau. Moi je t'observe de loin avec mes popcorns et je me marre comme un fou!"
    if mort == 2 :
    dd "Je change de formule et j'invoque le grand portail pour te ramener la ou tu devrait être. Au revoir dans l'autocar [nom]!"
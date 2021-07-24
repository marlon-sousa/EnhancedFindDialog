# EnhancedFindDialog pour NVDA ${addon_version}
Extension qui améliore le dialogue de recherche de NVDA:

* historique de recherche
* continuité de recherche, configurée par profil
* respecter la casse, configurée par profil
* informations contextuelles sur les recherches

## Télécharger
Télécharger l'extension [Enhanced Find Dialog ${addon_version}](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Caractéristiques

### Historique de recherche
Dans de nombreuses pages Internet et d'autres applications, le moyen le plus rapide d'accéder à certains endroits spécifiques consiste à utiliser la commande "Rechercher", généralement liée aux touches "ctrl+nvda+f".

Le dialogue de recherche nous permet d'écrire un texte et en appuyant sur "Entrée", d'être placé dans la prochaine occurrence de ce texte s'il existe.

Dans de nombreux cas, vous visiterez plusieurs fois les mêmes endroits d'une page, même les mêmes pages pendant  la même session NVDA. Par conséquent, vous devez rechercher les mêmes termes, surtout s'il s'agit du seul moyen d'accéder rapidement à un lien ou à une section de ce site.

C'est notamment le cas des personnes qui travaillent, dans leur vie quotidienne, avec des systèmes Web.

Cependant, NVDA ne garde pas  un historique des termes précédemment recherchés, ce qui diminue votre productivité car, à moins que vous ne recherchiez exactement le même terme  de votre dernière recherche, vous devez l'écrire à nouveau.

Cette extension garde un historique de recherche qui dure tant que   NVDA est en cours d'exécution. Par conséquent, lorsque vous appuyez sur les touches pour effectuer la recherche , si vous avez déjà cherché un terme ou une expression donné, vous devez simplement appuyer sur les flèches bas ou haut pour sélectionnez les termes précédemment recherchés afin d'effectuer une nouvelle recherche et revenir à l'endroit souhaité.

Bien sûr, vous pouvez toujours écrire de nouveaux termes. Dans ce cas, ils seront également ajoutés à la liste, la prochaine fois que vous activez la boîte de dialogue de recherche.

#### Comment ça marche?

Il suffit d'installer l'extension. Lorsqu'elle est activée, à l'aide des touches "ctrl+nvda+f", comme vous le faites habituellement pour le dialogue de recherche NVDA , appuyez sur les flèches  haut et bas dans le champ d'édition, ce qui vous permet de naviguer dans la liste des termes et des expressions précédemment recherchés.

Vous pouvez à tout moment et quand vous en avez besoin, écrire un nouveau terme, comme d'habitude.

### Continuité de recherche

La continuité de recherche est une fonctionnalité qui, si configurée, ne considère pas la position actuelle dans laquelle il se trouve, dans un texte, lors de la recherche.

Cela signifie que si vous recherchez quelque chose qui n'est pas présent en dessous de votre position actuelle, la recherche sera effectuée à partir du début du texte pour vérifier que ce terme existe quelque part dans le document.

Ceci est particulièrement important pour les personnes qui travaillent avec des systèmes Web et doivent trouver un déterminé bouton ou une partie du texte, indépendamment de l'endroit où ils sont sur la page.

Cette option est spécifique pour  un profil, ce qui signifie que vous pouvez avoir un profil où il est active et un autre où il n'est pas.

#### Comment ça marche?

Il suffit d'installer l'extension. Lorsqu'elle est activée, la boîte de dialogue "Rechercher" proposera une case à cocher appelée "Continuité de recherche".

Si c'est cochée:

1. Si vous recherchez un terme et il se trouve en bas de la position actuelle, le curseur sera  placé sur ce texte.
2. Si ce terme ne se trouve pas en bas de la position actuelle, il sera recherché en haut du texte.
3. Si le terme est trouvé,  un petit bip s'émettra pour vous informer que le texte trouvé   est au-dessus de votre position actuelle et que le curseur est placé sur cette position.
4. Si ce terme n'est pas trouvé, le message texte non trouvé sera affiché.

Changer cette case à cocher et effectuer une  recherche enregistrera le nouvel état (cochée ou non cochée) pour le profil actif. Annuler la recherche ne changera pas l'état sur le profil actif, même si vous l'avez changé avant d'annuler la recherche.

### Respecter la casse

NVDA propose déjà la case à cocher "Respecter la casse" pour permettre les recherches en considérant ce cas. Cette extension étend cette fonctionnalité en enregistrant l'état de cette case à cocher sur le profil actif, pour que vous ayez des profils configurés différemment.

#### Comment ça marche?

Il suffit d'installer l'extension. Changer la case à cocher  "Respecter la casse" et effectuer une  recherche enregistrera le nouvel état (cochée ou non cochée) pour le profil actif. Annuler la recherche ne changera pas l'état sur le profil actif, même si vous l'avez changé avant d'annuler la recherche.

### Informations contextuelles sur les recherches

Actuellement, sans cette extension, la manière dont NVDA se comporte lorsqu'un terme de recherche est trouvé, est le suivant: le curseur est placé sur la position du terme recherché et  ce terme est prononcé.

Cela devient quelque chose de problématique lorsque vous devez rechercher plusieurs fois pour n'importe quel terme (à l'aide de NVDA + f3) parce que la première chose qui est entendue est le terme recherché, ce qui est redondant, parce que  vous venez de le rechercher!

Cette extension place le curseur sur la position du terme, mais au lieu de lire le terme en lui-même, lit la ligne complète fournissant le contexte sur lequel ce terme a été trouvé.

Par exemple, supposons que vous recherchiez "Marlon" parce que vous savez qu'il y a un bouton appelé "Mentionner Marlon" quelque part sur la page. Vous ne voulez pas rechercher le terme "mentionner," car il existe d'autres boutons appelés "mentionner x y z" et vous voulez trouver le bouton "Mentionner Marlon".

Voici le texte:

Exclure les commentaires de Marlon

répondre directement à Marlon

Signaler Marlon en tant que spammeur

Mentionner Marlon dans une réponse

Si vous avez cherché "Marlon" avant ce bloc, vous entendriez
"commentaires de Marlon"

Si vous maintenez enfoncée les touches NVDA + f3, vous entendriez

"Marlon"

Marlon en tant que spammeur

Marlon dans une réponse

Cela réduirait votre productivité, car, d'abord, vous entendrez à peine Marlon, sans rien savoir sur cette occurrence.

La prochaine fois, vous entendriez Marlon et devriez attendre que "en tant que spammeur" soit prononcé, car vous ne sauriez pas ce qu'il y a à propos de Marlon sur ce texte.

De la même manière, la prochaine fois, vous devriez attendre que le reste de la phrase "dans une réponse" soit prononcé, car vous n'auriez pas la certitude sur de ce qui était la chose à propos  de Marlon.

De plus, si vous appuyez sur NVDA + f3 rapidement, vous écouterez Marlon, Marlon, Marlon, Marlon... ce qui n'est pas productif parce que vous savez que vous recherchez Marlon.

#### Comment ça marche?

Il suffit d'installer l'extension.

Après l'installation, la ligne actuelle du terme de recherche est lue et le curseur est placé sur ce terme.

Dans l'exemple précédent, la première fois que la recherche a été effectuée, vous avez écouté

"Exclure les commentaires de Marlon"

Si vous maintenez enfoncée les touches NVDA + f3, vous entendriez

"répondre directement à Marlon"

"Signaler Marlon en tant que spammeur"

"Mentionner Marlon dans une réponse"

De plus, si vous appuyez sur NVDA + f3 rapidement, vous écoutez le début de chaque ligne, vous permettant d'appuyer rapidement sur  "Entrée" sur la ligne commençant par Mentionner, car vous savez que le terme "Marlon" est présent sur une dernière position sur cette même ligne.

# aidant à traduire ou à développer l'extension

Si vous voulez aider à traduire ou à développer l'extension, s'il vous plaît accéder au [dépôt du projet](https://github.com/marlon-sousa/EnhancedFindDialog) et recherchez le fichier contributing.md dans le répertoire de documentation équivalent à votre langue.

## Contributeurs

Remerciement spécial à


* Ângelo Miguel Abrantes - Traduction Portugais Portugal
* Rémy Ruiz - Traduction Français
* Rémy Ruiz - Traduction Espagnol
*  Thiago Seus - Traduction Portugais Brésil
* Valentin Kupriyanov - Traduction Russe
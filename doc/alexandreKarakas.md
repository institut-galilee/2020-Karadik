## Fiche personnelle d'activité Alexandre KARAKAS

### Résumé des activités

Au tout début du projet, nous avons fait le choix de construire une poubelle connectée afin des permettre à chacun et de manière ludique d'apprendre à trier ses déchets. 
Dans une première partie du projet nous avons conçu de manière schématique la poubelle connectée. Puis j'ai du réflechir aux composants nécéssaire.
Chacun de notre côté avons réflechis aux composants. Nous nous sommes vu plusieurs fois pour pouvoir discuter sur les composants à achetés. 

Pour pouvoir mené à bien notre projet nous avons séparer le projet en plusieurs partie dont :
La conception, le montage, l'interface et l'etude de marchés. 
Je me suis chargé de l'interface dont vous trouverez les fichiers sur le git. 

#### Interface
Pour pouvoir faire le lien avec les composants, j'ai décidé avec l'accord de mon binôme, d'utiliser Tkinter. Tkinter est un module à la fois simple et fonctionnelle pour créer des interfaces graphiques assez rapiedment. J'ai donc créer une interface avec plusieurs boutons. Un bouton pour pouvoir prendre des photos, ces photos seront ensuite analysés par un programme qui s'appelle Tensorflow.
Un bouton pour pouvoir indiqué l'état de la poubelle en particulier sur le taux de remplissage de la poubelle
Un autre bouton pour pouvoir rapidement quitter l'interface.

Nous avions également à un problème qui était apparu dans le projet. 
Nous n'avions pas de bouton pour pouvoir prendre une photo.
j'ai eu donc l'idée de creer des boutons virtuels pour remplacer un bouton physique. J'ai donc décider d'en parler avec mon collegue et par son accord nous avons décider de suivre cette solution. J'ai donc créer deux fichier dont :
- [TestInterface.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/TestInterface.py)
- [Graphique.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/Graphique.py)

#### Caméra
Je me suis également chargé de créer un fichier pour la [caméra](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/camera.py). Grâce au module de la caméra piCamera qui est présent dans le système de la Raspberry pi 3, ce fichier permet de prendre une photo. Le fichier [classify_original](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/classify_original.py) permet de l'analyser et renvoie la valeur. 

#### Etat de l'art
Conernanr l'état de l'art, nous avons partagés les recherches sur l'état de l'art et sur les solutions qui existe dans le monde. L'état de l'art à été fait en collaboration avec Nady

## Les acquis

Le projet dans son ensemble m'a permis d'apprendre a mener à bien un projet, de la conception à la réalisation du prototype. Malgrès une periode difficile, j'ai pu apprendre à utiliser Python et à créer un interface avec ce même langage. 
Faire une étude de marché à été enrichissant en particulier de rechercher des solutions existante ainsi que l'étendu du marché. Ce qui peut me permettre à l'avenir de créer une start up sur ces bases. 
Le projet m'a permis de résoudre des problèmes que nous avons rencontré tout au long du projet. Ce qui permet aussi d'apprendre à gérer les imprévus. 

Les connaissances que j'ai acquis sur le materiels en particulier sur les Raspberry et sur les montages me permettra d'avoir une expérience sur les objets connectée, leur fonctionnement et de comment ont-ils été conçus.

Faire une étude de marché permet de savoir si notre produit correspond bien à un besoin spécifique d'une entreprise, d'un particulier ou d'une structure publique. Cette étude permet aussi d'améliorer le produit existants et d'avoir une longueurs d'avance sur les concurrents.



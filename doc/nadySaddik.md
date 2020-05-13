# Fiche personnelle de Nady SADDIK

## Résumé de l'activité
Au cours de ce projet, Alexandre et moi avons conçu une poubelle connectée. Nous nous sommes beaucoup entraidés sur la partie code, qui était le gros du travail.
A titre personnel, je me suis chargé de la réalisation du [schéma Fritzing](https://raw.githubusercontent.com/institut-galilee/2020-Karadik/master/lab/Project/eco3-theoretical-sketch.png). Comme nous avons rencontré des soucis de matériel (détaillé dans le rapport), nous n'avons malheureusement pas pu tester l'intégralité de ce schéma.

Niveau code, j'ai créé les fichiers :

 - [servo.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/servo.py), qui s'occupe de gérer les servomoteurs et en active un des trois lorsqu'il le faut.
 - [sonar.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/sonar.py), qui se charge de gérer les SONARs et calcule le taux de remplissage des bacs de la poubelle.

J'ai aussi apporté ma contribution au fichier [camera.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/code/camera.py), avec la liaison du résultat de l'analyse au type de déchet.

Ayant le matériel depuis le début du confinement, je me suis chargé du montage et de tester les différents codes mis au point par Alexandre et par moi-même (et de les corriger légèrement si nécessaire). 

Enfin, pour ce qui est de la documentation (état de l'art, rapport), nous l'avons réalisée en collaboration. Je me suis aussi chargé de filmer la vidéo de présentation et de faire le montage : [elle est disponible sur Youtube](https://www.youtube.com/watch?v=kYA4_jZysQE).


## Les acquis permis par le projet
La réalisation de ce projet, bien qu'entachée par un imprévu regrettable, m'a permis d'apprendre à développer en Python. C'était aussi la première fois que je manipulais une Raspberry Pi et ça m'a permis d'apprendre à l'utiliser. Créer un projet concret est également une première et est très appréciable, car on a rarement l'occasion de faire cela en projet.

De plus, j'ai appris les différentes étapes dans la conception d'un produit (état de l'art, création d'un diagramme use-case avant de concevoir le produit fini). Cette compétence qui me sera très utile dans le monde du travail.

Enfin, bien que très sommaire, la création d'une vidéo de présentation m'a permis d'apprendre un peu à maîtriser des logiciels de montage.

En somme, ce projet m'a apporté des choses très bénéfiques. J'aurais énormément aimé pouvoir le finir complètement, et c'est probablement quelque chose que je ferai prochainement avec mon collègue Alexandre.
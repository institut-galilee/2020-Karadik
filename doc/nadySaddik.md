# Fiche personnelle de Nady SADDIK

## Résumé de l'activité
Au cours de ce projet, Alexandre et moi avons conçu une poubelle connectée. Nous nous sommes beaucoup entraidés sur la partie code, qui était le gros du travail.
A titre personnel, je me suis chargé de la réalisation du [schéma Fritzing](https://raw.githubusercontent.com/institut-galilee/2020-Karadik/master/lab/Project/eco3-theoretical-sketch.png). Comme nous avons rencontré des soucis de matériel (détaillé dans le rapport), nous n'avons malheureusement pas pu tester l'intégralité de ce schéma.

Niveau code, j'ai créé les fichiers :

 - [servo.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/misc/Code_camera/servo.py), qui s'occupe de gérer les servomoteurs et en active un des trois lorsqu'il le faut.
 - [sonar.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/misc/Code_camera/sonar.py), qui se charge de gérer les SONARs et calcule le taux de remplissage des bacs de la poubelle.

J'ai aussi apporté ma contribution au fichier [camera.py](https://github.com/institut-galilee/2020-Karadik/blob/master/src/misc/Code_camera/camera.py), avec la liaison du résultat de l'analyse au type de déchet.

Ayant le matériel depuis le début du confinement, je me suis chargé du montage et de tester les différents codes mis au point par Alexandre et par moi-même. 

Enfin, pour ce qui est de la documentation, nous l'avons réalisée en collaboration.


## Les acquis permis par le projet
La réalisation de ce projet, bien qu'entachée par un imprévu regrettable, m'a permis d'apprendre à développer en Python. C'était aussi la première fois que je manipulais une Raspberry Pi et ça m'a permis d'apprendre à l'utiliser. Créer un projet concret est également une première et est très appréciable, car on a rarement l'occasion de faire cela en projet.
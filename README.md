# Moviflix

## **Avant Propos**
Moviflix est une application FullStack de recommandation de films qui tire parti des technologies suivantes : 
- [Docker-Compose]
- [FastAPI]
- [JWT]
- [MongoDB]
- [Vue 3]
- [PrimeVue/PrimeFlex]
- [IMDB API] (https://imdb-api.com/)

## **Dettes Techniques**
- Utilisation de tokens JWT pour décoder le nom de l'utilisateur qui effectue la requête
- Système de notation des films (backend)
- Gestion des groupes (frontend)
- Ajout d'un fichier de configuration et utilisation des variables d'environnement pour toutes les constantes (liens vers les API)
- Problème de CORS lorsque l'on se connecte au serveur depuis un autre PC sur le réseau.

## **Fonctionnalités**
1) Détails des films (snippet trailer imdb, résumé, acteurs etc...)
2) Système d'inscription et de connexion
3) Système de recommandations : 
A partir de la liste des membres d'un groupe d'utilisateurs, on sélectionne un film au hasard parmis ceux qui ont un genre pertinent et qui n'ont pas encore été vus par le groupe. 
4) Système de Logs

## **Installation**
### 1) **Pré-requis**
- docker [20.10.14]
- docker-compose [1.29.2] (https://docs.docker.com/compose/install/)

### 2) **BDD**
- La BDD n'est pas diffusée publiquement conformément aux conditions d'utilisation de l'API IMDB.
- Une fois récupérée, copiez le .gz dans back-moviflix/db/import/

### 3) **Lancement du projet**
A la racine du projet, effectuez la commande suivante :
```sh
docker-compose up
```
Important : Il faut s'assurer que le nom des conteneurs sont **EXACTEMENT** les suivants : 
- moviflix_client-vuejs_1
- moviflix_recommendation-api_1
- moviflix_db-api_1
- moviflix_db_1

Si ce n'est pas le cas vous pouvez renommer les conteneurs avec **docker rename ...**

- Le frontend est disponible à l'adresse : http://localhost:8080
- L'API REST qui permet de stocker les données en base : http://localhost:3002/docs
- L'API REST qui calcule la recommandation : http://localhost:3001/docs

## **Développement avec docker-compose**
Le projet est entièrement conteneurisé avec docker-compose. L'avantage ? Une seule commande pour construire toutes les images et lancer les 4 conteneurs. Des volumes ont été montés pour pouvoir réexécuter le code à la volée sans devoir reconstruire les images.


### **Supprimer les conteneurs**
```sh
$ docker-compose down
```
### **Mettre à jour les dépendances** 
Dans le cas où on ajoute de nouvelles librairies (Javascript ou Python) ou on modifie le Dockerfile d'un conteneur, la commande suivante permettra de reconstruire les images et relancer uniquement les conteneurs affectés par un changement.  
```sh
$ docker-compose up --build 
```

### **Points importants** 
1) A chaque mise à jour des dépendances un volume est nouvellement créé. Il faut penser à supprimer les volumes anonymes sans quoi ils pourraient prendre beaucoup d'espace disque en local.
2) Chaque conteneur possède un volume particulier isolé qui l'empêche de voir le volume des autres conteneurs. Il faudra ajouter un volume commun si on souhaite partager des fichiers entre les conteneurs.

## **Credits**
- Mathieu L.
- Romain R.
- Louis C.
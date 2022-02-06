# Moviflix

## **Sujet**

Considérons un groupe de N personnes :
« Recommander, un ou plusieurs films, à un instant T, qui n’ont pas encore été vus par ce groupe de N personnes et qui partage un maximum de points commun entre ces personnes. »

## **Développement avec docker-compose**
### **Pré-requis** 
- docker installé 
- docker-compose installé (https://docs.docker.com/compose/install/)

### **Initialisation du projet**
Se placer dans à la racine du dépôt (moviflix) puis :
```sh
docker-compose up
```
### **Supprimer les conteneurs**
```sh
docker-compose down
```
### **Mettre à jour les dépendances** 
```sh
docker-compose up --build -V
```

### **Points importants** 
1) A chaque mise à jour des dépendances un volume est nouvellement créé. Il faut penser à supprimer les volumes anonymes sans quoi ils pourraient prendre beaucoup d'espace disque en local.
2) 
### **Sources utiles**
- https://blog.atulr.com/docker-local-environment/#:~:text=frankly%20annoying%20%F0%9F%A4%AF.-,%F0%9F%95%B6%20Docker%20based%20local%20development%20environment,all%20out%20as%20one%20package.

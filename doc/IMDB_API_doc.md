# IMDB API DOCUMENTATION

## Lien
https://imdb-api.com/

## Fonctionnement
1) Créer un compte imdb-api
2) Récupérer sa clé API ici : https://imdb-api.com/Identity/Account/Manage
3) La clé API devra être présente dans l'url de la requête
4) Consulter ses droits sur l'API imdb (nombre de requêtes par jour = **100**) à l'adresse suivantes : https://imdb-api.com/Identity

## Fetch toutes les infos d'un film
### **1] https://imdb-api.com/en/API/Title/{apiKey}/{movieID}/FullActor,Posters,Images,Trailer**

get  : 
- **duration** (runtimeMins)
- **trailer URL** (trailer.linkEmbed)
- **movieCoverUrl** (image)
- **year** (year)
- **synopsis** (plot)
- **image urls** (images.items.image)

## Intégration du trailer d'un film avec l'API IMDB

Remplacer l'url de src jusqu'à ..."embed?"
```sh
<iframe src="https://www.imdb.com/video/imdb/vi1032782617/imdb/embed?autoplay=false&width=640" width="640" height="640" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" frameborder="no" scrolling="no"></iframe>
```


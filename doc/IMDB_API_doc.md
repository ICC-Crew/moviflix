# IMDB API DOC

## Link
https://imdb-api.com/

## Fetch all infos of one movie
### **1] https://imdb-api.com/en/API/Title/{apiKey}/{movieID}/FullActor,Posters,Images,Trailer**

get  : 
- **duration** (runtimeMins)
- **trailer URL** (trailer.linkEmbed)
- **movieCoverUrl** (image)
- **year** (year)
- **synopsis** (plot)
- **image urls** (images.items.image)

## Embedded trailer media player code snippet

Replace src url by trailer url until ..."embed?"
```sh
<iframe src="https://www.imdb.com/video/imdb/vi1032782617/imdb/embed?autoplay=false&width=640" width="640" height="640" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" frameborder="no" scrolling="no"></iframe>
```


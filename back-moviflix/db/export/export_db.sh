#!/bin/sh
docker_id=$(docker ps -aqf "name=moviflix_db_1")

docker exec -i $docker_id sh -c 'exec mongodump --db moviflixDB --archive --gzip' | cat > moviflixdb_dump.gz
#!/bin/bash
cat /docker-entrypoint-initdb.d/moviflixdb_dump.gz | mongorestore --host localhost:27017 --archive --gzip --drop --db=moviflixDB
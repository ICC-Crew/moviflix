db.createCollection('movies');
db.createCollection('users');
db.createCollection('groups');
db.createCollection('userOpinions');

movieId1 = ObjectId(); 
userId1 = ObjectId();
userId2 = ObjectId();

db.movies.insertOne(
    {   
        _id:movieId1,
        imdbID :"tt0133093",
        fetched :1,
        title : "The Matrix",
        duration : 136,
        movieCoverUrl:"https://imdb-api.com/images/original/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_Ratio0.6762_AL_.jpg", 
        genres : ["Action","Sci-fi"], 
        directors: ["Lana Wachowski","Lilly Wachowski"], 
        year:1999,
        synopsis:"Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. As a rebel against the machines, Neo must confront the agents: super-powerful computer programs devoted to stopping Neo and the entire human rebellion.",
        trailerUrl:"https://www.imdb.com/video/imdb/vi1032782617/imdb/embed", 
        moviePicturesURL: ["https://imdb-api.com/images/original/MV5BMjQ1NDAwMzI4Nl5BMl5BanBnXkFtZTgwMDkwMTEyMjI@._V1_Ratio1.9200_AL_.jpg"
            ,"https://imdb-api.com/images/original/MV5BNzM4OTkzMjcxOF5BMl5BanBnXkFtZTgwMTkxMjI1MTI@._V1_Ratio2.4000_AL_.jpg"
            ,"https://imdb-api.com/images/original/MV5BMTMxMDg1MjY4OF5BMl5BanBnXkFtZTcwMTU3MTIxNA@@._V1_Ratio1.5000_AL_.jpg"
        ],
       
        actors:
        [
            { 
                name: "Keanu Reeves",
                asCharacter: "Neo",
                imgActorUrl:"https://imdb-api.com/images/original/MV5BYTkzODI4MDMtNDNmZC00NDZlLWFmNTktNDRhOWE2YzhlZTQ2XkEyXkFqcGdeQXVyMTE1MTYxNDAw._V1_Ratio0.7727_AL_.jpg"
            }
            ,
            {
                name:"Carrie-Anne Moss",
                asCharacter: "Trinity",
                imgActorUrl : "https://imdb-api.com/images/original/MV5BMTYxMjgwNzEwOF5BMl5BanBnXkFtZTcwNTQ0NzI5Ng@@._V1_Ratio0.7273_AL_.jpg"
            }
            ,
            {
                name:"Laurence Fishburne",
                asCharacter:"Morpheus",
                imgActorUrl:"https://imdb-api.com/images/original/MV5BMTc0NjczNDc1MV5BMl5BanBnXkFtZTYwMDU0Mjg1._V1_Ratio0.7273_AL_.jpg"
            }
            
        ]
    
    }
);

db.users.insertMany([
    {   
        _id:userId1,
        userName:"eisti", 
        pass:"icc2k22"
    },
    {   
        _id:userId2,
        userName:"lo0kat", 
        pass:"dbmaster97438" 
    }
]);

db.userOpinions.insertOne(
    {
        movieId: movieId1,
        userId : userId2,
        rating:5,
        comments:["Une référence en matière de SF :D !"]
    }
);

db.groups.insertOne(
    {
        groupName:"ICC",
        admin:userId1,
        members:[userId1,userId2]
    }
);
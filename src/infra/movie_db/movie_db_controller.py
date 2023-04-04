from domain.models.person import Person
from domain.models.rating import Rating
from dataclasses import dataclass, field
from domain.models.movie import Movie
from domain.models.genre import Genre
from PyMovieDb import IMDB
from typing import List
import json
import uuid


@dataclass
class MovieDBController:
    imdb: IMDB = field(default=IMDB())

    def dict_to_movie(self, response: dict) -> Movie:
        genres = []
        for genre in response["genre"]:
            genres.append(Genre(id=uuid.uuid4(), name=genre))

        keywords = []
        for keyword in response["keywords"].split(","):
            keywords.append(keyword)

        actors = []
        for actor in response["actor"]:
            actors.append(Person(id=uuid.uuid4(), name=actor["name"], url=actor["url"]))
        
        directors = []
        for director in response["director"]:
            directors.append(Person(id=uuid.uuid4(), name=director["name"], url=director["url"]))

        creators = []
        for creator in response["creator"]:
            creators.append(Person(id=uuid.uuid4(), name=creator["name"], url=creator["url"]))

        return Movie(
            id=uuid.uuid4(),
            type=response["type"],
            name= response["name"],
            url=response["url"],
            description=response["description"],
            rating=Rating(
                id=uuid.uuid4(),
                ratingCount=response["rating"]["ratingCount"],
                bestRating=response["rating"]["bestRating"],
                worstRating=response["rating"]["worstRating"],
                ratingValue=response["rating"]["ratingValue"],
            ),
            contentRating=response["contentRating"],
            genre=genres,
            datePublished=response["datePublished"],
            keywords=keywords,
            duration=response["duration"],
            actor=actors,
            director=directors,
            creator=creators
        )


    def get_by_name(self, name: str) -> Movie:
        response = json.loads(self.imdb.get_by_name(name))
        movie = self.dict_to_movie(response)
        return movie
    
    def get_by_id(self, id: str) -> Movie:
        response = json.loads(self.imdb.get_by_id(id))
        
        if "status" not in response:
            movie = self.dict_to_movie(response)
            return movie
        return None
    def search_all(self) -> List[Movie]:
        terms = ("a", "b", "c", "d", "e", "f", "g", "h", "i", )
                #  "j", "k", "l", "m", "n", "o", "p", "q", "r", 
                #  "s", "t", "u", "v", "w", "x", "y", "z", "1", 
                #  "2", "3", "4", "5", "6", "7", "8", "9", "0")
        movies = []
        
        for t in terms:
            responses = json.loads(self.imdb.search(t))

            for response in responses["results"]:
                movie = self.get_by_id(response["id"])
                if movie:
                    movies.append(movie)
                    print(f"Collected Movies: {len(movies)}")
        
        return movies
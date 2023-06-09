from api.application.view_models.movie_view_model import MovieViewModel
from api.application.view_models.genre_view_model import GenreViewModel
from api.application.view_models.person_view_model import PersonViewModel
from api.application.view_models.rating_view_model import RatingViewModel
from api.domain.models.genre import Genre
from api.domain.models.person import Person
from api.domain.models.rating import Rating
from api.domain.models.movie import Movie
from typing import List


class MovieDomainToViewModel:

    @staticmethod
    def to_view_model(movie: Movie) -> MovieViewModel:
        if movie:
            return MovieViewModel(
                name=movie.name,
                id=movie.id,
                description=movie.description,
                rating=RatingDomainToViewModel.to_view_model(movie.rating),
                genre=GenreDomainToViewModel.to_view_models(movie.genre),
                year=movie.year,
                duration=movie.duration,
                actor=PersonDomainToViewModel.to_view_models(movie.actor),
                director=PersonDomainToViewModel.to_view_models(movie.director),
            )

    @staticmethod
    def to_view_models(movies: List[Movie]) -> List[MovieViewModel]:
        movie_vms = list()
        if movies:
            for customer in movies:
                movie_vms.append(MovieDomainToViewModel.to_view_model(customer))
        return movie_vms

class RatingDomainToViewModel:

    @staticmethod
    def to_view_model(rating: Rating) -> RatingViewModel:
        if rating:
            return RatingViewModel(
                id=rating.id,
                rating=rating.rating,
                votes=rating.votes,
                metascore=rating.metascore,
                imdb_ratings=rating.imdb_ratings
            )

class GenreDomainToViewModel:

    @staticmethod
    def to_view_model(genre: Genre) -> GenreViewModel:
        if genre:
            return GenreViewModel(
                name=genre.name
            )
    
    @staticmethod
    def to_view_models(genres: List[Genre]) -> List[GenreViewModel]:
        genre_vms = list()
        if genres:
            for g in genres:
                genre_vms.append(GenreDomainToViewModel.to_view_model(g))
        return genre_vms

class PersonDomainToViewModel:

    @staticmethod
    def to_view_model(person: Person) -> PersonViewModel:
        if person:
            return PersonViewModel(
                id=person.id,
                name=person.name,
            )
    
    @staticmethod
    def to_view_models(persons: List[Person]) -> List[PersonViewModel]:
        person_vms = list()
        if persons:
            for p in persons:
                person_vms.append(PersonDomainToViewModel.to_view_model(p))
        return person_vms

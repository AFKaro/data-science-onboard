from application.view_models.movie_view_model import MovieViewModel
from application.auto_mapper.view_model_to_domain_mapping import (
    MovieViewModelToDomainMapping as DomainMapper,
)
from application.auto_mapper.domain_to_view_model_mapping import (
    MovieDomainToViewModel as ViewModelMapper,
)
from domain.interfaces.repository_interface import (
    RepositoryInterface,
)
from dataclasses import dataclass, field
from domain.models.movie import Movie
from infra.movie_db.movie_db_controller import MovieDBController
from typing import List
import logging
import json
import uuid


@dataclass(repr=False, eq=False)
class MovieAppService:
    movie_repository: RepositoryInterface = field(repr=False)
    movie_controller: MovieDBController = field(default=MovieDBController())

    def store_movies(self) -> bool:
        results = self.movie_controller.search_all()

        response = True

        for movie in results:
            if movie:
                response = self.movie_repository.add(movie)
                print(f"Movie Registred: {len(results)}")
                if response == False:
                    break

        return response

    def graphs_generate(self) -> bool:
        movies = self.movie_repository.get_all()
        print(len(movies))

    def get_all(self) -> List[MovieViewModel]:
        movies = self.movie_repository.get_all()
        movie_vms = ViewModelMapper.to_view_models(movies)
        return movie_vms

    def get_by_id(self, id: uuid.UUID) -> MovieViewModel:
        movies = self.movie_repository.get_by_id(id)
        movie_vm = ViewModelMapper.to_view_model(movies)
        return movie_vm

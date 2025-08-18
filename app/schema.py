import strawberry

from strawberry_django import mutations, field
from strawberry_django_extras.field_extensions import with_validation

from .types import (
    User,
    UserInput,
)


@strawberry.type
class Query:
    users: list[User] = field()


@strawberry.type
class Mutation:
    create_user: User = mutations.create(
        UserInput,
        extensions=[with_validation()]
    )


schema = strawberry.Schema(query=Query, mutation=Mutation)

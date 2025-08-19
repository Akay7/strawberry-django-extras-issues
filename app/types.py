from typing import Optional

from django.core.exceptions import ValidationError
from strawberry import auto

import strawberry_django
from django.contrib.auth import get_user_model




@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
    email: auto
    first_name: auto
    last_name: auto

    def validate(self, info):
        if self.first_name == self.last_name:
            raise ValidationError(
                "Firstname and lastname cannot be the same"
            )
        
    def validate_username(self, info, value: str, ) -> str:
        if get_user_model().objects.filter(email__startswith=value + "@").exists():
            raise ValidationError("Some user have similar email to your username")
        return value

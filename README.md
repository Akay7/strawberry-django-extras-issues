# Quick start

Install poetry

```shell
pip install poetry
```

Install project dependencies, run migrations, load test data and start development server.

```shell
poetry install
poetry run ./manage.py migrate
poetry run ./manage.py runserver
```

After that you have web server and graphql endpoint running at http://127.0.0.1:8000/graphql.

## Issue

Query

```json
mutation MyMutation ($username: String!, $firstName: String, $lastName: String) {
  createUser(input: {username: $username, password: "123", firstName: $firstName, lastName: $lastName}){
    id
  }
}
```

Variables

```json
{
  "username": "user2",
  "firstName": "Ivanov",
  "lastName": "Ivanov"
}
```

Will not have validations up until moment when changed settings to

```python
STRAWBERRY_DJANGO = {
    # "MUTATIONS_DEFAULT_ARGUMENT_NAME": "input",
    "MUTATIONS_DEFAULT_ARGUMENT_NAME": "data",
}
```
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

At async GQL endpoint

http://127.0.0.1:8000/graphql

* at the same time sync will works well http://127.0.0.1:8000/graphql/sync

Query

```json
mutation MyMutation ($username: String!, $firstName: String, $lastName: String, $email: String) {
  createUser(data: {username: $username, password: "123", firstName: $firstName, lastName: $lastName, email: $email}){
    id
  }
}
```

Variables

```json
{
  "username": "user",
  "firstName": "Vlad",
  "lastName": "Valov",
  "email": "user@example.com"
}
```

During creation on check

```python
    def validate_username(self, info, value: str, ) -> str:
        if get_user_model().objects.filter(email__startswith=value + "@").exists():
```

will be exception 

```json
{
  "data": null,
  "errors": [
    {
      "message": "You cannot call this from an async context - use a thread or sync_to_async.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "createUser"
      ]
    }
  ]
}
```
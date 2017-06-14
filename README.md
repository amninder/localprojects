# Local Projects


This project uses docker to containerize three services:

  - Django Web Service
  - REST API Service
  - Websocket
 

### Running locally with Docker
The migration is done as part of the Dockerfile and shouldn't need to be repeated (but it's ok to do so if you get an error).

Run the app:

```sh
$ docker-compose up
```

If migration required, you can run:

```sh
$ docker-compose run --rm web python manage.py migrate
```

Then create the superuser:
```sh
$ docker-compose run --rm web python manage.py createsuperuser
```

Tearing down all the images:
```sh
$ docker rm $(docker ps -a -q)
$ docker rmi $(docker images -q)
```

### API Endpoints

I use `httpie` for interaction. You can install it by `pip install httpie`
The result is seen at `http://localhost:8000/` and following are the enpoints to interact:

| Use | HTTP Verb | URL | Explaination| Example |
| ------ | ------ |------ |------ |------ |
| ref_questions | GET |`http://localhost:8000/ref_questions/`| Lists all reference questions|
| ref_questions by ID | GET |`http://localhost:8000/ref_questions/<id>/`| Lists reference questions by ID|
| ref_tokens | GET |`http://localhost:8000/ref_tokens/`| Lists all the reference tokens|
| ref_tokens | GET |`http://localhost:8000/ref_tokens/<id>`| Lists the reference tokens by the ID|
| ref_tokens | POST |`http://localhost:8000/ref_tokens/`| Creates new Ref Token| http --form POST http://localhost:8000/ref_tokens/ token="Immigration Services" no=-40 yes=10 |
| tokens | GET |`http://localhost:8000/tokens/`| Lists all the tokens|
| tokens | GET |`http://localhost:8000/tokens/<id>`| Lists tokens by ID|
| users | GET |`http://localhost:8000/users/`| Lists all the users with the questions with their attribute weightages|
| users | GET |`http://localhost:8000/users/<username>`| Returns the user of the username provided with the questions with their attribute weightages|
| users | POST |`http://localhost:8000/users/<username>/questions/<question_id>/answer/<yes or no>/`| Submits the answer to the question by id associated to the user by the username |http POST http://localhost:8000/users/root/questions/1/answer/yes/ |


### Usage

The admin can be accessed at `http://localhost:8000/admin/` with the login credentials created at the time of the `docker-compose run --rm web python manage.py createsuperuser`. There are following models:

* `Token References`: where all the tokens are defined with their weights.
* `Tokens`: where the token we want to track when the user submits the answer.
* `Question References`: where questions are defined and different tokens are associated to the questions
* `User Profile`: where User profile is created with the questions associated to the users.

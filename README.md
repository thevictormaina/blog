# Unload Blog App

## A blogging web application

### [Heroku Link](https://unload-blog.herokuapp.com/unload-blog-app) | [LucidCharts ERD](https://lucid.app/invitations/accept/9a035917-cd99-4d80-b9b3-4fe2e30e08b5) | [Figma Link](https://www.figma.com/file/cTHDwxqrcPu1CEUjUYbKzv/Blog-UI?node-id=1%3A136)

---
## Introduction

Unload is an online blogging platform where writers can create a blog. Others can read a writer's blogpost and leave comments. Anyone can be a writer on the platform by creating an account.

## Technologies Used

Unload is built on Flask, a Python microframework. The live app is deployed on Heroku, and Postgres is used to manage its database.

## Installation (Ubuntu)

You can run the app using a local server on your computer. You will need Git to clone the app from this repo. Since Unload also uses Python 3 and Postresql, you will need to install them on your machine.

```bash
$ sudo apt install git python3 postgresql
```

You can now clone the repository on your computer. Navigate into the new directory after the clone is complete.

```bash
$ git clone https://github.com/thevictormaina/blog.git
$ cd blog-app
```
As mentioned before, Unload runs on Flask and other Python modules. To install all the dependencies, you will need to create a virtual environment and activate it.

```bash
$ python3.6 -m venv virtual
$ source virtual/bin/activate
```

Note: Be sure to use your own preferred version of Python. You can confirm by running `$ python3 --version` on your terminal.

Next, install the dependencies from the `requirements.txt` file.

```bash
$ python3.6 -m pip install -r requirements.txt
```

Unload also makes use of a database, so you will need to create one using Postgres. You can find instrustions for creating a Postgresql user and password [here.](https://www.postgresql.org/docs/8.0/sql-createuser.html)

Enter Postgresql on your terminal using `$ psql`, then do

```postgres
username=# CREATE DATABASE blog_app;
username=# \q
```

To be able to send emails to users, the app will access to an email address. For simplicity's sake, a dummy Google account and password have already been created. The app looks for exported environment variables to run. To enable this, create a file in the app's root directory called `start.sh`.

```bash
$ touch start.sh
$ chmod a+x start.sh
```

Pitcher will need a secret key for an imported module called WTForms. It will also need to connect to the database you created. Go to `config.py` under the `DevCoonfig` class, and replace the `username` and `password` with your own.

Pitcher uses SQLAlchemy to make managing the database directly from the app easier. To update your database to work with this app's models, run the following on your terminal.

```bash
$ python3.6 manage.py db upgrade
```

Run the application.

```bash
$ ./start.sh
```
As long as the server is running, you can open it in the browser [using this link](http://127.0.0.1:5000).

## Tests
The app comes with some test modules. To run them, you will need to create another Postgresql database with the name `blog_app_test`. Then edit `config.py` match your own Postgres username and password. Change you `start.sh` to look like this.

```bash
...
python3.6 manage.py test
```

Now run `./start.sh` on your terminal.

## Known bugs
At the moment, writers can't delete blogposts or comments.

## [LICENSE](/LICENSE)

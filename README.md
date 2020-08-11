[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Hype-Board API
An API built using a backend Django server using a PostgreSQL database hosted on Heroku.

The Hype-Board server accepts HTTP requests from the client and sends back appropriate JSON responses for user authentication, posts, and comments.

The API enables users to:
  1. Sign-up, sign-in, change password, and sign-out of their accounts.
  2. Create, view, update, and delete their own posts.
  3. Create, view, update, and delete their own comments.
  4. View other users in the database

## Setup Instructions
1. Fork and clone this repository.
2. Run ```pipenv install``` to install all dependencies
3. Run ```pipenv shell``` to open up the development enviornment
4. Run ``` pipenv runserver``` to run the server

## Important Links
- Client Repo: https://github.com/Andrew-Chun/hype-board-client
- Deployed API: https://hype-board.herokuapp.com/
- Deployed Client: https://andrew-chun.github.io/hype-board-client/

## Planning Story
The MVP of this project originally encompassed users being able to CRUD posts.
This process included creating the model, serializing the model data, creating a url path for the resource, and defining different views for the response.

A one-to-many relationship was established between Users and Posts by defining ```owner``` (User) as a foreign key on the Post model.

A one-to-many relationship was established between Users and Comments by referencing User as a foreign key Comment model. Additionally, ```post_id``` as a foreign key on the Comments model to establish a relationship between Comments and Posts, as Posts can have many comments.

Finally, I added two GET views for Users in order to retrieve other users in the database.

## Technologies Used
- Python
- Django
- PostgreSQL
- Heroku

## Catalog of Routes
Verb         |	URI Pattern
------------ | -------------
POST | /sign-up/
POST  | /sign-in/
DELETE  | /sign-out/
PATCH  | /change-pw/
GET | /posts/
POST  |  /posts/
GET | /posts/:id/
DELETE  |  /posts/:id/
PATCH  |  /posts/:id/
GET | /comments/
POST | /comments/
GET | /comments/:id
DELETE | /comments/:id
POST | /comments/:id
GET  | /users/
GET | /users/:id/

## Entity Relationship Diagram
![Hype-Board ERD](https://i.imgur.com/ZZmVqvr.png)


## Future Iterations
-Adding topics/categories for posts

-Comments on comments

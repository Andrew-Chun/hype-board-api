[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Hype-Board API
An API built using a backend Django server using a PostgreSQL database hosted on Heroku.

The Hype-Board server accepts HTTP requests from the client and sends back appropriate JSON responses for user authentication, posts, and comments.

## Links
- Client Repo: https://github.com/Andrew-Chun/hype-board-client
- Deployed API: https://hype-board.herokuapp.com/
- Deployed Client: https://andrew-chun.github.io/hype-board-client/

## List of Technologies Used
- Python
- Django
- PostgreSQL
- Heroku

## Catalog of Routes for API
- path('posts/', Posts.as_view(), name='posts')
  - Methods: GET, POST
- path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail')
  - Methods: GET, DELETE, PATCH
- path('comments/', Comments.as_view(), name='comments')
  - Methods: GET, POST
- path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail')
  - Methods: GET, DELETE, PATCH
- path('sign-up/', SignUp.as_view(), name='sign-up')
  - Method: POST
- path('sign-in/', SignIn.as_view(), name='sign-in')
  - Method: POST
- path('sign-out/', SignOut.as_view(), name='sign-out')
  - Method: DELETE
- path('change-pw/', ChangePassword.as_view(), name='change-pw')
  - Method: PATCH
- path('users/', Users.as_view(), name='users')
  - Method: GET
- path('users/<int:pk>/', UserDetail.as_view(), name='user_detail')
  - Method: GET

## Setup and Installation Instructions


## Entity Relationship Diagram
[Hype-Board ERD](https://i.imgur.com/ZZmVqvr.png)


## Problems to be Solved in Future Iterations
-Adding topics/categories for posts

-Comments on comments

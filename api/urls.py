from django.urls import path
from .views.post_views import Posts, PostDetail
from .views.comment_views import Comments, CommentDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword, Users, UserDetail

urlpatterns = [
	# Restful routing
    path('posts/', Posts.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('comments/', Comments.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('users/', Users.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail')
]

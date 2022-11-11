from django.urls import path

from .views import home, PostUpdate, PostView, NewPost 
from django.contrib.auth.decorators import login_required

app_name = 'neditor'


urlpatterns = [
    path('',home),
    path('newpost/',login_required(NewPost.as_view()), name='new_post'),
    path('posts/<int:pk>/edit', login_required(PostUpdate.as_view()), name='post_edit'),
    path('posts/<int:pk>', PostView.as_view(), name='post_detail'),
]
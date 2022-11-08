from django.urls import path

from .views import home, PostUpdate, PostView, NewPost 

urlpatterns = [
    path('newpost/',NewPost.as_view(), name='new_post'),
    path('posts/<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
    path('posts/<int:pk>', PostView.as_view(), name='post_detail'),
]